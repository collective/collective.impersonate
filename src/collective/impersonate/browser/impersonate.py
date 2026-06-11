"""@@impersonate view handler."""

from plone import api


try:
    from Products.CMFPlone.interfaces import IUserGroupsSettingsSchema
except ImportError:
    # Plone 4.3 compatibility
    from plone.app.controlpanel.usergroups import IUserGroupsSettingsSchema

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PluggableAuthService.interfaces.plugins import IAuthenticationPlugin
from zope.component import getAdapter



class Impersonate(BrowserView):
    """@@impersonate view."""

    template = ViewPageTemplateFile("impersonate.pt")

    def __call__(self):
        self.actions()
        return self.template()

    def _get_jwt_plugin(self):
        """Find the JWT Authentication Plugin in acl_users."""
        acl_users = getToolByName(self.context, "acl_users")
        plugins = acl_users._getOb("plugins")
        authenticators = plugins.listPlugins(IAuthenticationPlugin)
        for _id, authenticator in authenticators:
            if authenticator.meta_type == "JWT Authentication Plugin":
                return authenticator
        return None

    def _create_auth_token(self, username):
        """Generate a JWT auth_token for the given user.

        This is needed for Volto (and other REST API consumers) which
        authenticate via the auth_token cookie (JWT Bearer token) rather
        than the __ac session cookie.

        The auth_token cannot be derived from the __ac cookie because they
        use different formats (mod_auth_tkt vs JWT), different signing
        secrets, and different algorithms.
        """
        plugin = self._get_jwt_plugin()
        if plugin is None:
            return None

        user = api.user.get(username=username)
        if user is None:
            return None

        payload = {"fullname": user.getProperty("fullname")}
        return plugin.create_token(user.getId(), data=payload)

    def actions(self):
        """Login the user"""
        if "username" in list(self.request.keys()):
            self.errors = {}
            username = self.request["username"].strip()
            if not api.user.get(username=username):
                self.errors["username"] = username
                return

            # Set the __ac session cookie (classic Plone UI)
            self.context.acl_users.session._setupSession(
                username, self.context.REQUEST.RESPONSE
            )

            # Set the auth_token JWT cookie (Volto / REST API)
            auth_token = self._create_auth_token(username)
            if auth_token:
                self.request.RESPONSE.setCookie(
                    "auth_token",
                    auth_token,
                    path="/",
                    secure=self.request.get("SERVER_URL", "").startswith("https"),
                    http_only=False,  # Volto reads this cookie client-side too
                    same_site="Lax",
                )

            self.request.RESPONSE.redirect(self.context.absolute_url())

    def users(self):
        """List all users on this site."""
        results = []
        for user in api.user.get_users():
            results.append(
                {"username": user.id, "fullname": user.getProperty("fullname")}
            )
        return results

    @property
    def many_users(self):
        return getAdapter(
            api.portal.get(),
            IUserGroupsSettingsSchema,
        ).many_users

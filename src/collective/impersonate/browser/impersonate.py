# -*- coding: utf-8 -*-
"""@@impersonate view handler."""

from plone import api

try:
    from Products.CMFPlone.interfaces import IUserGroupsSettingsSchema
except ImportError:
    # Plone 4.3 compatibility
    from plone.app.controlpanel.usergroups import IUserGroupsSettingsSchema
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getAdapter


class Impersonate(BrowserView):
    """@@impersonate view."""

    template = ViewPageTemplateFile("impersonate.pt")

    def __call__(self):
        self.actions()
        return self.template()

    def actions(self):
        """Login the user"""
        if "username" in list(self.request.keys()):
            self.errors = {}
            username = self.request["username"].strip()
            if not api.user.get(username=username):
                self.errors["username"] = username
                return

            self.context.acl_users.session._setupSession(
                username, self.context.REQUEST.RESPONSE
            )

            self.request.RESPONSE.redirect(api.portal.get().absolute_url())

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

# -*- coding: utf-8 -*-
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer


try:
    from plone.testing import zserver
except ImportError:
    from plone.testing import z2 as zserver  # noqa: F401


class CollectiveImpersonateLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import collective.impersonate

        self.loadZCML(package=collective.impersonate)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.impersonate:default")


COLLECTIVE_IMPERSONATE_FIXTURE = CollectiveImpersonateLayer()


COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_IMPERSONATE_FIXTURE,),
    name="CollectiveImpersonateLayer:IntegrationTesting",
)


COLLECTIVE_IMPERSONATE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_IMPERSONATE_FIXTURE,),
    name="CollectiveImpersonateLayer:FunctionalTesting",
)

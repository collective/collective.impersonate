# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.impersonate.testing import (
    COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING,
)  # noqa
from plone import api

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    # BBB for Plone 5.0 and lower.
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.impersonate is properly installed."""

    layer = COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer is None:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        else:
            self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.impersonate is installed."""
        if get_installer is None:
            is_installed = self.installer.isProductInstalled("collective.impersonate")
        else:
            is_installed = self.installer.is_product_installed("collective.impersonate")
        self.assertTrue(is_installed)

    def test_browserlayer(self):
        """Test that ICollectiveImpersonateLayer is registered."""
        from collective.impersonate.interfaces import ICollectiveImpersonateLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveImpersonateLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer is None:
            self.installer = api.portal.get_tool("portal_quickinstaller")
            self.installer.uninstallProducts(["collective.impersonate"])
        else:
            self.installer = get_installer(self.portal)
            self.installer.uninstall_product("collective.impersonate")

    def test_product_uninstalled(self):
        """Test if collective.impersonate is cleanly uninstalled."""
        if get_installer is None:
            is_installed = self.installer.isProductInstalled("collective.impersonate")
        else:
            is_installed = self.installer.is_product_installed("collective.impersonate")
        self.assertFalse(is_installed)

    def test_browserlayer_removed(self):
        """Test that ICollectiveImpersonateLayer is removed."""
        from collective.impersonate.interfaces import ICollectiveImpersonateLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveImpersonateLayer, utils.registered_layers())

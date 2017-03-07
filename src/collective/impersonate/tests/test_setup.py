# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.impersonate.testing import COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.impersonate is properly installed."""

    layer = COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.impersonate is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.impersonate'))

    def test_browserlayer(self):
        """Test that ICollectiveImpersonateLayer is registered."""
        from collective.impersonate.interfaces import (
            ICollectiveImpersonateLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveImpersonateLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_IMPERSONATE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.impersonate'])

    def test_product_uninstalled(self):
        """Test if collective.impersonate is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.impersonate'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveImpersonateLayer is removed."""
        from collective.impersonate.interfaces import \
            ICollectiveImpersonateLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveImpersonateLayer, utils.registered_layers())

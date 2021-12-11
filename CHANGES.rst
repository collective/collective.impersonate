Changelog
=========

1.4 (2021-12-11)
----------------

- Plone 6 compatibility -> remove <includeDependencies />
  [petschki]


1.3 (2020-10-07)
----------------

- Add support for Plone 5.2 and Python 3
  [cillianderoiste]

- Use explicit dependency on Products.GenericSetup >= 1.8.2
  [laulaz]

- Fix issue with Lineage subsites, where the `many_users` property couldn't be resolved due to a wrong adapter context.
  [thet]

- Added French translation
  [laulaz]

- minor markup cleanup [ajung]

- Plone 4.3 compatibility
  [petschki]

- Minor code cleanup: black, isort, travis fixes.
  [thet]


1.2 (2019-06-18)
----------------

- lists available users only if the "Many users?" box in Users and Groups control panel is not checked
  [tkimnguyen]


1.1.1 (2019-06-16)
------------------

- upgrade to Plone 5.1.5, add 'Framework :: Plone :: Addon' pypi classifier, tweak docs
  [tkimnguyen]


1.1 (2019-06-15)
----------------

- update docs to show Impersonate portal action
  [tkimnguyen]

- add user documentation
  [tkimnguyen]

- add Impersonate personal menu item for Manager role
  [tkimnguyen]

- fix buildout, isort fixes, flake8 fixes, Travis fixes
  [tkimnguyen]

- upgrade to Plone 5.0.10
  [tkimnguyen]

- tweak Travis xvfb start
  [tkimnguyen]

- fix test buildout
  [tkimnguyen]


1.0.1 (2017-03-07)
------------------

- Brownbag release.
  [zupo]


1.0 (2017-03-07)
----------------

- Initial release.
  [zupo]

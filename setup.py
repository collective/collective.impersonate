"""Installer for the collective.impersonate package."""

from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.impersonate",
    version="3.0.0.dev0",
    description="Allow administrator to impersonate another user, for "
    "debugging purposes.",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="NiteoWeb Ltd.",
    author_email="info@niteoweb.com",
    url="https://github.com/collective/collective.impersonate",
    license="GPL version 2",
    include_package_data=True,
    python_requires=">=3.10",
    zip_safe=False,
    install_requires=[
        "plone.api",
        "plone.app.layout",
        "z3c.jbot",
        "Products.GenericSetup",
        "Products.CMFPlone",
        "Zope",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.testing",
            "plone.browserlayer",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)

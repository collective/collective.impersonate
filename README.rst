======================
collective.impersonate
======================

Allow administrator to impersonate another user. Useful for verifying
workflow/permission set up on real content.


Installation
------------

Install collective.impersonate by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.impersonate


and then running ``bin/buildout``


Usage
-----

Install then head to http://<YOUR-PLONE-SITE>/@@impersonate. Enter a valid
user id and click Impersonate.

Logout when you are finished.


License
-------

The project is licensed under the GPLv2.

Based on the old niteoweb.loginas package:
https://pypi.python.org/pypi/niteoweb.loginas

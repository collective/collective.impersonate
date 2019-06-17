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

See the `docs`_ folder (or `on GitHub`_) for instructions on how to use this add-on.

.. _docs: docs/index.rst
.. _on GitHub: https://github.com/collective/collective.impersonate/blob/master/docs/index.rst


Wishlist
--------

- display users in batches (for sites with many users)

- autocomplete with search select2 widget for choosing the user to impersonate


License
-------

The project is licensed under the GPLv2.

Based on the old niteoweb.loginas package:
https://pypi.python.org/pypi/niteoweb.loginas

======================
collective.impersonate
======================

This add-on allows an administrator to impersonate another user.

This is useful for verifying workflows, permissions, and roles set up on real content and on live sites.

How to Impersonate a User
-------------------------

You must be logged in as a user with Manager or Site Administrator role.

Use the Impersonate item in your personal menu at the bottom of the toolbar.

.. image:: impersonate_menu_item.png
    :alt: screenshot of the Impersonate menu item
    :scale: 100 %

You will see a form that displays the users on your site.

.. image:: impersonate_form.png
    :alt: screenshot of the @@impersonate form
    :scale: 100 %

In the "Target user" field, enter the ID of the user you want to impersonate, then press the Impersonate button.

You will see the name of the impersonated user appear on the personal menu toolbar button in the bottom left corner of
your browser window.

.. image:: impersonating.png
    :alt: screenshot of Plone while impersonating a user
    :scale: 100 %

Site Interactions
-----------------

You can navigate throughout and interact with your site as the impersonated user.
Content items will be displayed according to the security settings of the impersonated user (roles, permissions, and
group memberships), and their workflow state.

How to Stop Impersonating a User
--------------------------------

Log out to stop impersonating a user. You can use Log Out in the personal menu toolbar button.

.. image:: impersonate_logout.png
    :alt: screenshot showing how to stop impersonating a user
    :scale: 100 %



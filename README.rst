haystack_static_pages
=====================

"Haystack Static Pages" is an extension library for Haystack.  Currently, it adds the ability to index static pages through the use of a `settings.py` variable and command extension.


Usage:
------

#. Setup and install Haystack.
#. Add haystack_extensions to your INSTALLED_APPS in `settings.py`
#. Add HAYSTACK_STATIC_PAGES to your `settings.py`.

::

    HAYSTACK_STATIC_PAGES = (
        'static-about_us',     # A named url
        'static-help',         # Another named url
        'http://example.com/', # A full url
    )

4. ./manage.py syncdb to create the necessary tables.
#. ./manage.py crawl_static_pages to populate the database with the static page content.  This is needed for Haystack to properly map the urls to the content. Output should indicate which pages were crawled and where, as well as the total number of pages found.
#. (If using the Solr backend) ./manage.py rebuild_solr_schema to create the Solr XML schema.  Be sure to copy the generated schema.xml into your Solr configuration.
#. ./manage.py reindex to create the search indexes used by Haystack.  You should see a note about how many static pages were indexed.  The number of static pages indexed should match the number of static pages created in the step above.

Notes:
------

* Each page indexed will have the following attributes available:

    * title -- The title as defined in a <title> tag
    * url -- The url of the page
    * description -- A short description as taken from any existing <meta name="description"> tag
    * content -- The page content.

* Because the `crawl_static_pages` command can only index content as rendered, it must be able to access the pages when run.  This means, that when using named urls, the site must be accessible at the location specified in `Site.get_current().domain`.
* The `-p` option can be used to specify the port number when executing the `crawl_static_pages` command.

Source
------

`github.com/trapeze/haystack-static-pages/ <http://github.com/trapeze/haystack-static-pages/>`_


Credits
-------

haystack-static-pages is maintained by `David Sauve <mailto:dsauve@trapeze.com>`_, and is funded by `Trapeze <http://www.trapeze.com>`_.

License
-------

haystack-static-pages is Copyright © 2009 David Sauve, Trapeze. It is free software, and may be redistributed under the terms specified in the LICENSE file. 

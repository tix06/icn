#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Benjamin Abel'
SITENAME = 'ICN'
SITEURL = 'http://benjaminabel.github.io/icn'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

PATH = 'content'

STATIC_PATHS = ['images', 'data']

DELETE_OUTPUT_DIRECTORY = True

# Adressage des articles
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'


# Extensions python markdown
MD_EXTENSIONS = ['codehilite(css_class=highlight)',
                 'extra',
                 'headerid',
                 'def_list',
                 ]
# Mon theme
THEME = '../lyceum-theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

PLUGIN_PATHS = ['../pelican-plugins']

# from pelican.readers import BaseReader
# from liquid_tags.notebook import NotebookReader

# READERS = {'html': None, 'ipynb': BaseReader}
READERS = {'html': None}


# Classer les pages dans des sous dossiers
USE_FOLDER_AS_CATEGORY = True

# Longueur du résumé

SUMMARY_MAX_LENGTH = 53

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# A list of tuples (Title, URL) for additional menu items to
# appear at the beginning of the main menu.
MENUITEMS = (('Github', 'https://github.com/benjaminabel/icn'),)

DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'))

# Social widget
SOCIAL = (('Github', 'https://github.com/benjaminabel'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# global metadata to all the contents
DEFAULT_METADATA = (('icn', 'Seconde'),)

# Plugins
PLUGINS = ['liquid_tags.notebook',
           'liquid_tags.img',
           'liquid_tags.video',
           'series',
           'tipue_search']

# Liquid tags
NOTEBOOK_DIR = 'notebooks'

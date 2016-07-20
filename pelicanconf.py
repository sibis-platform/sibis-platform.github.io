#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = "SRI International"
SITENAME = "Scalable Informatics for Biomedical Imaging Studies"
SITESUBTITLE = ""
SITEURL = ""

TIMEZONE = "America/Vancouver"

DEFAULT_LANG = "en"

conda_env = os.environ.get('CONDA_ENV_PATH', "")

# Theme
if conda_env == "":
  THEME = "/Users/nicholsn/Repos/pelican-themes/pelican-bootstrap3"
else
  THEME = conda_env + "/lib/python2.7/site-packages/pelican-themes/pelican-bootstrap3"

# Theme specific config
MENUITEMS = [['Scalable Informatics for Biomedical Imaging Studies', 'index.html'],
             ['About', 'pages/about.html'],
             ['Team', 'pages/team.html'],
             ['Contact', 'pages/contact.html']]
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = 'solarizedlight'
SITELOGO = "images/logo-header.png"
SITELOGO_SIZE = "60%"
HIDE_SITENAME = True
#DISPLAY_BREADCRUMBS = True
#DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = False
FAVICON = "images/favicon.png"
DISPLAY_ARTICLE_INFO_ON_INDEX = True
ABOUT_ME = ""
AVATAR = ""
CC_LICENSE = "CC-BY"
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
USE_PAGER = True
BOOTSTRAP_FLUID = True
RELATED_POSTS_MAX = 10
USE_OPEN_GRAPH = True

# Notebook Rendering
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
CUSTOM_CSS = 'static/custom.css'

# Template settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)
TAG_CLOUD_MAX_ITEMS = 20
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
HIDE_SIDEBAR = True

# Articles per page
DEFAULT_PAGINATION = 10
RECENT_POST_COUNT = 5

# Plugins
if conda_env == "":
  PLUGIN_PATHS = ["/Users/nicholsn/Repos/pelican-plugins"]
else
  PLUGIN_PATHS = [conda_env + "/lib/python2.7/site-packages/pelican-plugins"]

PLUGINS = ['related_posts', 'tipue_search', 'liquid_tags.img',
           'liquid_tags.video', 'liquid_tags.youtube',
           'liquid_tags.vimeo', 'liquid_tags.include_code',
           'liquid_tags.notebook']

# Static paths and cname mapping
PATH = "content"
STATIC_PATHS = ['images', 'extra/custom.css']
EXTRA_PATH_METADATA = {
                       'extra/custom.css': {'path': 'static/custom.css'}
                       }
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = ['.']


# Social widget
SOCIAL = (('Github', 'https://github.com/sibis-platform'),)

# Disqus config
DISQUS_SITENAME = ""

# Addthis
ADDTHIS_PROFILE = ""
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

# Github
GITHUB_USER = "sibis-platform"
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
ARTICLE_EDIT_LINK = 'https://github.com/sibis-platform/sibis-platform.github.io/blob/gh-pages/content/%(slug)s.md'

# Google registration
GOOGLE_SEARCH = ""
GOOGLE_ANALYTICS_UNIVERSAL = ""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
CATEGORY_FEED_ATOM = False
TRANSLATION_FEED_ATOM = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

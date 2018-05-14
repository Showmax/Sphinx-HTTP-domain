# -*- coding: utf-8 -*-
"""
    sphinx.domains.http
    ~~~~~~~~~~~~~~~~~~~

    Utilities for the HTTP domain.
"""
from __future__ import unicode_literals

import re
import unicodedata

import six

_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_strip_url_re = re.compile(r'[^\w\s/?=&#;{}-]')
_slugify_hyphenate_re = re.compile(r'[^\w]+')


def slugify(value, strip_re=_slugify_strip_re):
    """
    Normalizes string, converts to lowercase, removes non-alpha
    characters, and converts spaces to hyphens.

    From Django's "django/template/defaultfilters.py".
    """
    if not isinstance(value, six.text_type):
        value = six.text_type(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = strip_re.sub('', value).strip().lower()
    return _slugify_hyphenate_re.sub('-', value)


def slugify_url(value):
    """
    Normalizes URL, converts to lowercase, removes non-URL
    characters, and converts non-alpha characters to hyphens.
    """
    return slugify(value, strip_re=_slugify_strip_url_re)

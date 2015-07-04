# encoding=utf8
"""set default encoding format"""

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import os
import sys
import urllib.request

GITHUB_API = 'https://api.github.com/'

API_TOKEN = os.environ.get('GITHUB_TOKEN')

# UTILITY FUNCTIONS

# EXCEPTION


def exception():
    """runs everytime an exception is caught"""
    print("Enter a valid URL. For help, type 'cli-github -h'")
    sys.exit(0)


# URL PARSING

def url_parse(name):
    """parse urls with different prefixes"""
    position = name.find("github.com")
    if position >= 0:
        if position != 0:
            position_1 = name.find("www.github.com")
            position_2 = name.find("http://github.com")
            position_3 = name.find("https://github.com")
            if position_1*position_2*position_3 != 0:
                exception()
                sys.exit(0)
        name = name[position+11:]
        if name.endswith('/'):
            name = name[:-1]
        return name
    else:
        if name.endswith('/'):
            name = name[:-1]
        return name

# GET TO OBTAIN JSON


def get_req(url):
    """simple get request"""
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    try:
        response = urllib.request.urlopen(request).read().decode('utf-8')
        return response
    except urllib.error.HTTPError:
        exception()
        sys.exit(0)

# RETURNS 302


def geturl_req(url):
    """get request that returns 302"""
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    try:
        response_url = urllib.request.urlopen(request).geturl()
        return response_url
    except urllib.error.HTTPError:
        exception()
        sys.exit(0)

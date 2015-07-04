# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()
import os
import sys
import argparse
import json
import urllib.request
import base64
import dateutil.parser
from prettytable import PrettyTable

GITHUB_API = 'https://api.github.com/'

API_TOKEN = os.environ.get('GITHUB_TOKEN')

# MAIN

def main():
    parser = argparse.ArgumentParser(
            description='Github within the Command Line')
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-n', '--username', type=str,
                   help="Get repos of the given username")
    g.add_argument('-u', '--url', type=str,
                   help="Get repos from the user profile's URL")
    g.add_argument('-r', '--recursive', type=str,
                   help="Get the file structure from the repo link")
    g.add_argument('-R', '--readme', type=str,
                   help="Get the raw version of the repo readme from repo link")
    g.add_argument('-re', '--releases', type=str,
                   help="Get the list of releases from repo link")
    g.add_argument('-dt', '--tarball', type=str,
                   help="Download the tarball of the given repo")
    g.add_argument('-dz', '--zipball', type=str,
                   help="Download the zipball of the given repo")

    if len(sys.argv) == 1:
        parser.print_help()
        return
    args = parser.parse_args()

# URL

    if(args.url):
        name = url_parse(args.url)
        url = GITHUB_API + 'users/' + name + '/repos'

# USERNAME

    if(args.username):
        name = args.username
        url = GITHUB_API + 'users/' + name + '/repos'

# TREE

    if(args.recursive):
        name = url_parse(args.recursive)
        url = GITHUB_API + 'repos/' + name + '/branches/master'
        response = get_req(url)
        jsondata = json.loads(response)
        sha = jsondata['commit']['commit']['tree']['sha']
        url = GITHUB_API + 'repos/' + name + '/git/trees/' + sha + '?recursive=1'

# README

    if(args.readme):
        name = url_parse(args.readme)
        url = GITHUB_API + 'repos/' + name + '/readme'

# RELEASES

    if(args.releases):
        name = url_parse(args.releases)
        url = GITHUB_API + 'repos/' + name + '/releases'

# TARBALL/ZIPBALL

    if(args.tarball):
        key = '/tarball/'
        name = url_parse(args.tarball)
    if(args.zipball):
        key = '/zipball/'
        name = url_parse(args.zipball)
    url = GITHUB_API + 'repos/' + name + key + 'master'

# GET RESPONSES

# TARBALL/ZIPBALL

    if(args.tarball or args.zipball):
        response_url = geturl_req(url)
        n = name.find('/')
        name = name[n+1:]
        if(args.tarball):
            name = name+'.tar.gz'
        if(args.zipball):
            name = name+'.zip'
        print("\nDownloading " + name + '...\n')
        urllib.request.urlretrieve(response_url, name)
        print(name + ' has been saved\n')
        return

# OTHER OPTIONS

    response = get_req(url)
    jsondata = json.loads(response)

# USERNAME and URL

    if(args.url or args.username):
        x = PrettyTable([" Repository ", "★ Star"])
        x.align[" Repository "] = "l"
        for i in jsondata:
            x.add_row([i['name'], i['stargazers_count']])
        print(x)

# RECURSIVE TREE

    if(args.recursive):
        x = PrettyTable([" File/Folder ", " Size (Bytes) "])
        x.align[" File/Folder "] = "l"
        for i in jsondata['tree']:
            size = '-'
            path = i['path']+'/'
            if(i['type'] == 'blob'):
                size = i['size']
                path = path[:-1]
            x.add_row([path, size])
        print(x)

# README

    if(args.readme):
        print(base64.b64decode(jsondata['content']).decode('utf-8'))

# RELEASES

    if(args.releases):
        x = PrettyTable([" Release name ", " Release Date ", " Release Time "])
        for i in jsondata:
            ti = str(dateutil.parser.parse(i['published_at']))
            date = ti[:10]
            time = date[11:][:5] + ' UTC'
            x.add_row([i['tag_name'], date, time])
        print(x)

# UTILITY FUNCTIONS

# EXCEPTION

def exception():
	print("Enter a valid URL. For help, type 'cli-github -h'")
        sys.exit(0)


# URL PARSING

def url_parse(name):
	n = name.find("github.com")
        if(n >= 0):
            if(n != 0):
                n1 = name.find("www.github.com")
                n2 = name.find("http://github.com")
                n3 = name.find("https://github.com")
                if(n1*n2*n3 != 0):
                    exception()
                    sys.exit(0)
            name = name[n+11:]
            if name.endswith('/'):
                name = name[:-1]
            return name
        else:
            exception()
            sys.exit(0)

# GET TO OBTAIN JSON

def get_req(url):
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
    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    try:
        response_url = urllib.request.urlopen(request).geturl()
        return response_url
    except urllib.error.HTTPError:
        exception()
        sys.exit(0)

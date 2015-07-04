# encoding=utf8
"""set default encoding format"""

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

from .utils import url_parse, get_req, geturl_req
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
    """main function"""
    parser = argparse.ArgumentParser(
        description='Github within the Command Line')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--username', type=str,
                       help="Get repos of the given username")
    group.add_argument('-u', '--url', type=str,
                       help="Get repos from the user profile's URL")
    group.add_argument('-r', '--recursive', type=str,
                       help="Get the file structure from the repo link")
    group.add_argument('-R', '--readme', type=str,
                       help="Get the raw version of the repo readme from repo link")
    group.add_argument('-re', '--releases', type=str,
                       help="Get the list of releases from repo link")
    group.add_argument('-dt', '--tarball', type=str,
                       help="Download the tarball of the given repo")
    group.add_argument('-dz', '--zipball', type=str,
                       help="Download the zipball of the given repo")
    group.add_argument('-op', '--openfile', type=str,
                       help="Show the contents of the given file in a repo")

    if len(sys.argv) == 1:
        parser.print_help()
        return
    args = parser.parse_args()

# URL

    if args.url:
        name = url_parse(args.url)
        url = GITHUB_API + 'users/' + name + '/repos'

# USERNAME

    if args.username:
        name = args.username
        url = GITHUB_API + 'users/' + name + '/repos'

# TREE

    if args.recursive:
        name = url_parse(args.recursive)
        url = GITHUB_API + 'repos/' + name + '/branches/master'
        response = get_req(url)
        jsondata = json.loads(response)
        sha = jsondata['commit']['commit']['tree']['sha']
        url = GITHUB_API + 'repos/' + name + '/git/trees/' + sha + '?recursive=1'

# README

    if args.readme:
        name = url_parse(args.readme)
        url = GITHUB_API + 'repos/' + name + '/readme'

# RELEASES

    if args.releases:
        name = url_parse(args.releases)
        url = GITHUB_API + 'repos/' + name + '/releases'

# TARBALL/ZIPBALL

    if args.tarball or args.zipball:
        if args.tarball:
            key = '/tarball/'
            name = url_parse(args.tarball)
        if args.zipball:
            key = '/zipball/'
            name = url_parse(args.zipball)
        url = GITHUB_API + 'repos/' + name + key + 'master'

# OPEN ONE FILE

    if args.openfile:
        name = url_parse(args.openfile)
        position = name.find('/')
        user = name[:position+1]
        rest = name[position+1:]
        position = rest.find('/')
        repo = rest[:position+1]
        rest = rest[position+1:]
        url = GITHUB_API + 'repos/' + user + repo + 'contents/' + rest

# GET RESPONSES

# TARBALL/ZIPBALL

    if args.tarball or args.zipball:
        response_url = geturl_req(url)
        position = name.find('/')
        name = name[position+1:]
        if args.tarball:
            name = name+'.tar.gz'
        if args.zipball:
            name = name+'.zip'
        print("\nDownloading " + name + '...\n')
        urllib.request.urlretrieve(response_url, name)
        print(name + ' has been saved\n')
        return

# OTHER OPTIONS

    response = get_req(url)
    jsondata = json.loads(response)

# USERNAME and URL

    if args.url or args.username:
        table = PrettyTable([" Repository ", "★ Star"])
        table.align[" Repository "] = "l"
        for i in jsondata:
            table.add_row([i['name'], i['stargazers_count']])
        print(table)

# RECURSIVE TREE

    if args.recursive:
        table = PrettyTable([" File/Folder ", " Size (Bytes) "])
        table.align[" File/Folder "] = "l"
        for i in jsondata['tree']:
            size = '-'
            path = i['path']+'/'
            if i['type'] == 'blob':
                size = i['size']
                path = path[:-1]
            table.add_row([path, size])
        print(table)

# README

    if args.readme:
        print(base64.b64decode(jsondata['content']).decode('utf-8'))

# RELEASES

    if args.releases:
        table = PrettyTable([" Release name ", " Release Date ", " Release Time "])
        for i in jsondata:
            time = str(dateutil.parser.parse(i['published_at']))
            date = time[:10]
            time = date[11:][:5] + ' UTC'
            table.add_row([i['tag_name'], date, time])
        print(table)

# OPEN ONE FILE

    if args.openfile:
        try:
            print(base64.b64decode(jsondata['content']).decode('utf-8'))
            return
        except:
            print("\nDirectory URL was given, hence its contents will be displayed\n")
            table = PrettyTable(["Folder Contents"])
            for i in jsondata:
                table.add_row([i['name']])
            print(table)


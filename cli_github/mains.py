#! /usr/bin/env python3
# encoding=utf8

from __future__ import absolute_import
import os, argparse, json, base64
import urllib2, urllib
from prettytable import PrettyTable

GITHUB_API = u'https://api.github.com/'

API_TOKEN = os.environ.get(u'GITHUB_TOKEN')

def main():
    parser = argparse.ArgumentParser(description=u'Github within the Command Line')
    g=parser.add_mutually_exclusive_group()
    g.add_argument(u'-n',u'--username', type=unicode, 
            help = u"Get repos of the given username")
    g.add_argument(u'-u',u'--url', type=unicode,
            help = u"Get repos from the user profile's URL")
    g.add_argument(u'-r',u'--recursive',type=unicode,
            help = u"Get the file structure from the repo link")
    g.add_argument(u'-R',u'--readme',type=unicode,
            help = u"Get the raw version of the repo readme from repo link")
    args = parser.parse_args()
    
    if(args.url):
        name=args.url[19:]
        if name.endswith(u'/'):
                name = name[:-1]
        url = GITHUB_API + u'users/' +name + u'/repos'
        

    if(args.username):
        name=args.username
        url = GITHUB_API + u'users/' +name + u'/repos'

    if(args.recursive):
        name=args.recursive[19:]
        if name.endswith(u'/'):
                name = name[:-1]
        url = GITHUB_API + u'repos/' +name + u'/branches/master'
        request = urllib2.Request(url)
        request.add_header(u'Authorization', u'token %s' % API_TOKEN)
        try:
            response = urllib2.urlopen(request).read().decode(u'utf-8')
        except urllib2.HTTPError, err:
            print u'-'*150
            print u"Invalid Credentials. For help, type 'cli-github -h'"
            print u'-'*150
            return
 
        jsondata = json.loads(response)
        sha = jsondata[u'commit'][u'commit'][u'tree'][u'sha']
        url=GITHUB_API+u'repos/'+name+u'/git/trees/'+sha+u'?recursive=1'

    if(args.readme):
        name=args.readme[19:]
        if name.endswith(u'/'):
                name = name[:-1]
        url = GITHUB_API + u'repos/' +name + u'/readme'
        

    request = urllib2.Request(url)
    request.add_header(u'Authorization', u'token %s' % API_TOKEN)
    try:
        response = urllib2.urlopen(request).read().decode(u'utf-8')
    except urllib2.HTTPError, err:
        print u'-'*150
        print u"Invalid Credentials. For help, type 'cli-github -h'"
        print u'-'*150
        return
        
    jsondata = json.loads(response)
    if(args.url or args.username):
        x = PrettyTable([u" Repository ", u"★ Star"])
        for i in jsondata:
            x.add_row([i[u'name'],i[u'stargazers_count']])
        print x

    if(args.recursive):
        x = PrettyTable([u" File/Folder ", u" Size (Bytes) "])
        for i in jsondata[u'tree']:
            size=u'-'
            path=i[u'path']+u'/'
            if(i[u'type']==u'blob'):
                size=i[u'size']
                path=path[:-1]
            x.add_row([path,size])
        print x
            
    if(args.readme):
        print base64.b64decode(jsondata[u'content']).decode(u'utf-8');

#! /usr/bin/env python3

import os
import argparse
import json
import urllib.request
import base64

GITHUB_API = 'https://api.github.com/'

API_TOKEN = os.environ.get('GITHUB_TOKEN')

def main():
    parser = argparse.ArgumentParser(description='Github within the Command Line')
    g=parser.add_mutually_exclusive_group()
    g.add_argument('-n','--username', type=str, 
            help = "Get repos of the given username")
    g.add_argument('-u','--url', type=str,
            help = "Get repos from the user profile's URL")
    g.add_argument('-r','--recursive',type=str,
            help = "Get the file structure from the repo link")
    g.add_argument('-R','--readme',type=str,
            help = "Get the raw version of the repo readme from repo link")
    args = parser.parse_args()
    
    if(args.url):
        name=args.url[19:]
        if name.endswith('/'):
                name = name[:-1]
        url = GITHUB_API + 'users/' +name + '/repos'
        

    if(args.username):
        name=args.username
        url = GITHUB_API + 'users/' +name + '/repos'

    if(args.recursive):
        name=args.recursive[19:]
        if name.endswith('/'):
                name = name[:-1]
        url = GITHUB_API + 'repos/' +name + '/branches/master'
        request = urllib.request.Request(url)
        request.add_header('Authorization', 'token %s' % API_TOKEN)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        jsondata = json.loads(response)
        sha = jsondata['commit']['commit']['tree']['sha']
        url=GITHUB_API+'repos/'+name+'/git/trees/'+sha+'?recursive=1'

    if(args.readme):
        name=args.readme[19:]
        if name.endswith('/'):
                name = name[:-1]
        url = GITHUB_API + 'repos/' +name + '/readme'
        

    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    jsondata = json.loads(response)
    
    if(args.url or args.username):
        for i in jsondata:
            print('\t*'+i['name'])

    if(args.recursive):
        for i in jsondata['tree']:
            print(i['path'])
    
    if(args.readme):
        print(base64.b64decode(jsondata['content']).decode('utf-8'));
    

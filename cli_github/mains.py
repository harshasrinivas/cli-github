#! /usr/bin/env python3
# encoding=utf8

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import os, sys, argparse, json, urllib.request, base64
from prettytable import PrettyTable
from string import *


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
    
    if len(sys.argv)==1:
        parser.print_help()
        return

    args = parser.parse_args()
        
    if(args.url):
        name=args.url
        n=name.find("github.com")
        if(n>=0):
            if(n!=0):
                n1=name.find("www.github.com")
                n2=name.find("http://github.com")
                n3=name.find("https://github.com")
                if(n1*n2*n3!=0):
                    print('-'*150)
                    print("Enter a valid URL. For help, type 'cli-github -h'")
                    print('-'*150)
                    return
            name=args.url[n+11:]
            if name.endswith('/'):
                name = name[:-1]
            url = GITHUB_API + 'users/' +name + '/repos'
        else:
            print('-'*150)
            print("Enter a valid URL. For help, type 'cli-github -h'")
            print('-'*150)
            return

    if(args.username):
        name=args.username
        url = GITHUB_API + 'users/' +name + '/repos'

    if(args.recursive):
        name=args.recursive
        n=name.find("github.com")
        if(n>=0):
            if(n!=0):
                n1=name.find("www.github.com")
                n2=name.find("http://github.com")
                n3=name.find("https://github.com")
                if(n1*n2*n3!=0):
                    print('-'*150)
                    print("Enter a valid URL. For help, type 'cli-github -h'")
                    print('-'*150)
                    return
            name=args.recursive[n+11:]
            if name.endswith('/'):
                    name = name[:-1]
            url = GITHUB_API + 'repos/' +name + '/branches/master'
            request = urllib.request.Request(url)
            request.add_header('Authorization', 'token %s' % API_TOKEN)
            try:
                response = urllib.request.urlopen(request).read().decode('utf-8')
            except urllib.error.HTTPError as err:
                print('-'*150)
                print("Invalid Credentials. For help, type 'cli-github -h'")
                print('-'*150)
                return
        else:
            print('-'*150)
            print("Enter a valid URL. For help, type 'cli-github -h'")
            print('-'*150)
            return
 
        jsondata = json.loads(response)
        sha = jsondata['commit']['commit']['tree']['sha']
        url=GITHUB_API+'repos/'+name+'/git/trees/'+sha+'?recursive=1'

    if(args.readme):
        name=args.readme
        n=name.find("github.com")
        if(n>=0):
            if(n!=0):
                n1=name.find("www.github.com")
                n2=name.find("http://github.com")
                n3=name.find("https://github.com")
                if(n1*n2*n3!=0):
                    print('-'*150)
                    print("Enter a valid URL. For help, type 'cli-github -h'")
                    print('-'*150)
                    return
        
            name=args.readme[n+11:]
            if name.endswith('/'):
                    name = name[:-1]
            url = GITHUB_API + 'repos/' +name + '/readme'
        else:
            print('-'*150)
            print("Enter a valid URL. For help, type 'cli-github -h'")
            print('-'*150)
            return
        

    request = urllib.request.Request(url)
    request.add_header('Authorization', 'token %s' % API_TOKEN)
    try:
        response = urllib.request.urlopen(request).read().decode('utf-8')
    except urllib.error.HTTPError as err:
        print('-'*150)
        print("Invalid Credentials. For help, type 'clipy-github -h'")
        print('-'*150)
        return
        
    jsondata = json.loads(response)
    if(args.url or args.username):
        x = PrettyTable([" Repository ", "★ Star"])
        x.align[u" Repository "] = u"l"
        for i in jsondata:
            x.add_row([i['name'],i['stargazers_count']])
        print(x)

    if(args.recursive):
        x = PrettyTable([" File/Folder ", " Size (Bytes) "])
        x.align[u" File/Folder "] = u"l"
        for i in jsondata['tree']:
            size='-'
            path=i['path']+'/'
            if(i['type']=='blob'):
                size=i['size']
                path=path[:-1]
            x.add_row([path,size])
        print(x)
            
    if(args.readme):
        print(base64.b64decode(jsondata['content']).decode('utf-8'));


#`cli-github`

**A Command-Line Python Application to display Github from the CLI !**

Click [**here**](http://showterm.io/38d628a202209e1136afd#fast) to see it live in action!
-----------------------------------------------------------------------------------------

| Build Status |  Version |  Downloads  |
| ------------ | -------- |  ---------  |
| [![Build Status](https://travis-ci.org/harshasrinivas/cli-github.svg?branch=master)](https://travis-ci.org/harshasrinivas/cli-github) | [![PyPI version](https://badge.fury.io/py/cli_github.svg)](http://badge.fury.io/py/cli_github) | [![PyPi downloads](https://img.shields.io/pypi/dd/cli-github.svg)](https://pypi.python.org/pypi/cli-github)


##Version 1.0.5
* Fixed URL parsing bugs
* Left Indented repo names
* Fixed Python 2/3 compatibility issues
* Option to list releases of a user's repo

#Screenshots

`To fetch repos and stars using the username`

![Username](https://github.com/harshasrinivas/cli-github/blob/master/images/name.png)

`To fetch repos and stars using the profile URL`

![URL](https://github.com/harshasrinivas/cli-github/blob/master/images/url.png)

`To get all the files and folders within a repo from its link`

![Tree](https://github.com/harshasrinivas/cli-github/blob/master/images/tree.png)

`To get the RAW version of readme file from the repo link`

![Readme](https://github.com/harshasrinivas/cli-github/blob/master/images/readme.png)

`To get the list of releases of a user's repository`

![Releases](https://github.com/harshasrinivas/cli-github/blob/master/images/releases.png)


#Installation

##Using `pip`

`pip install cli-github`

##Get the latest build from the Source

* Clone the repo `git clone https://github.com/harshasrinivas/cli-github.git`
* Run `python setup.py install`

##Dependencies

* prettytable `pip install prettytable`
* future `pip install future`
* python-dateutil `pip install python-dateutil`

#Setting Up

**Github Token as Temporary Environment Variable**

`$ GITHUB_TOKEN=<your-token-with-quotes>`

**Github Token as Permanent Environment Variable**

`$ echo "export GITHUB_TOKEN=<your-token-with-quotes>" | sudo tee -a /etc/environment`

**Without saving your Environment Variable**

`$ cat cli_github/mains.py | sed -e "s/API_TOKEN = os.environ.get('GITHUB_TOKEN')/API_TOKEN = <your-token-with-quotes>/" > cli_github/mains.py`

<br>

#Options

```sh
-h, --help            show this help message and exit
-n USERNAME, --username USERNAME
                    Get the list of repositories of the given username
-u URL, --url URL 
                    Get repos from the user profile URL
-r RECURSIVE, --recursive RECURSIVE
                    Get the file structure from the repo link URL
-R README, --readme README
                    Get the raw version of the repository readme file from repo link URL
-re RELEASES, --releases RELEASES
                 	Get the list of releases from repo link
```



#Usage

Display the list of a user's repositories from the username, along with the number of stargazers

`$ cli-github -n harshasrinivas`

Display the list of a user's repositories from the profile URL, along with the number of stargazers

`$ cli-github -u https://github.com/harshasrinivas`

Display all the files and folders within a repository recursively from the repository URL, along with their sizes

`$ cli-github -r https://github.com/harshasrinivas/cli-github`

Get the RAW version of the readme file of a repository from the repository URL

`$ cli-github -R https://github.com/harshasrinivas/cli-github`

Get the list of releases from the user's repo link

`$ cli-github -re https://github.com/sananth12/ImageScraper`

#Live Demo

[**DEMO**](http://showterm.io/aaa79dee63aad0695e304#fast) : Display the list of a user's repositories from the username, along with the number of stargazers

[**DEMO**](http://showterm.io/5dc39b7fc3d7244577d2f#fast) : Display the list of a user's repositories from the profile URL, along with the number of stargazers

[**DEMO**](http://showterm.io/99e16e6ae35727999eb23#fast) : Display all the folders and files within a repository recursively from the repository URL, along with their sizes

[**DEMO**](http://showterm.io/820b37fab14c7ed4cf7ff#fast) : To get the RAW version of the readme file of a repository from the repository URL

[**DEMO**](http://showterm.io/24a6ceec356bb672ec24f#fast) : To get the list of releases from the user's repository URL

#Contribute

If you want to add features, improve them, or report issues, feel free to send a pull request.


#License

![GPL V3](https://raw.githubusercontent.com/harshasrinivas/cli-github/master/images/gpl.png)

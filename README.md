clipy-github
============

A Python App to display **Github from the command-line**


#INSTALLATION

##Using `PIP`

`pip3 install clipy_github`

##From the Source

* Clone the repo `git clone https://github.com/harshasrinivas/clipy-github.git`
* Run `python3 setup.py install`



#SETTING UP

##Github Token as Permanent Environment Variable

Set your Github Personal Access Token as the environment variable GITHUB_TOKEN

`echo "export GITHUB_TOKEN = <your-token-within-quotes>" >> /etc/environment`

##Github Token as Temporary Environment Variable

`GITHUB_TOKEN = <your-token-within-quotes>`

##Without saving your Environment Variable

Open the `clipy_github/mains.py` file

Change this line `API_TOKEN = os.environ.get('GITHUB_TOKEN')` to `API_TOKEN = <your-token-within-quotes> `



#OPTIONS

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
```



#USAGE

Display the list of a user's repositories from the username

`clipy-github -n harshasrinivas`

Display the list of a user's repositories from the profile URL

`clipy-github -u https://github.com/harshasrinivas`

Display all the files and folders within a repository recursively from the repository URL

`clipy-github -r https://github.com/harshasrinivas/clipy-github`

Get the RAW version of the readme file of a repository from the repository URL

`clipy-github -R https://github.com/harshasrinivas/clipy-github`



#CONTRIBUTE

If you want to add features, improve them, or report issues, feel free to send a pull request.

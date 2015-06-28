cli-github
============

A Python App to display **Github from the command-line**

Live Demo
=========

`DEMO <http://showterm.io/72aa0ffb05765f7ec92c0#fast>`__ : Display the list of a user's repositories from the username, along with the number of stargazers

`DEMO <http://showterm.io/813bc4e61fc9d752d2cb6#fast>`__ : Display the list of a user's repositories from the profile URL, along with the number of stargazers

`DEMO <http://showterm.io/459287d10701d531f3506#fast>`__ : Display all the folders and files within a repository recursively from the repository URL, along with their sizes

`DEMO <http://showterm.io/09286d1d9b333be0cc9cd#fast>`__ : To get the RAW version of the readme file of a repository from the repository URL

Installation
============

Using ``pip``
-------------

.. code:: sh

   $ pip install cli-github

From the Source
---------------

-  Clone the repo
   
   .. code:: sh
      
      $ git clone https://github.com/harshasrinivas/cli-github.git

-  Run 
   
   .. code:: sh
   
      $ python setup.py install

Dependencies
============

-  ``prettytable`` 
   
   .. code:: sh
   
      $ pip install prettytable

Setting Up
==========

**Github Token as Permanent Environment Variable**

Set your Github Personal Access Token as the environment variable
GITHUB\_TOKEN

.. code:: sh

   $ echo "export GITHUB_TOKEN = <your-token-with-quotes>" | sudo tee -a /etc/environment

**Github Token as Temporary Environment Variable**

.. code:: sh

   $ GITHUB_TOKEN = <your-token-with-quotes>

**Without saving your Environment Variable**

Open the file 

.. code:: sh

   $ cli_github/mains.py

Change this line 

.. code:: sh

   $ API_TOKEN = os.environ.get('GITHUB_TOKEN') to API_TOKEN = <your-token-with-quotes>

Options
=======

.. code:: sh

    -h, --help            show this help message and exit
    -n USERNAME, --username USERNAME
                        Get the list of repositories of the given username
    -u URL, --url URL 
                        Get repos from the user profile URL
    -r RECURSIVE, --recursive RECURSIVE
                        Get the file structure from the repo link URL
    -R README, --readme README
                        Get the raw version of the repository readme file from repo link URL

Usage
=====

Display the list of a user's repositories from the username

.. code:: sh

   $ cli-github -n harshasrinivas

Display the list of a user's repositories from the profile URL

.. code:: sh

   $ cli-github -u https://github.com/harshasrinivas

Display all the files and folders within a repository recursively from
the repository URL

.. code:: sh

   $ cli-github -r https://github.com/harshasrinivas/cli-github

Get the RAW version of the readme file of a repository from the
repository URL

.. code:: sh

   $ cli-github -R https://github.com/harshasrinivas/cli-github

Contribute
==========

If you want to add features, improve them, or report issues, feel free
to send a pull request.

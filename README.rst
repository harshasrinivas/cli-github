clipy-github
============

A Python App to display **Github from the command-line**

Installation
============

Using ``pip``
-------------

.. code:: sh

   $ pip3 install clipy_github

From the Source
---------------

-  Clone the repo
   
   .. code:: sh
      
      $ git clone https://github.com/harshasrinivas/clipy-github.git

-  Run 
   
   .. code:: sh
   
      $ python3 setup.py install

Setting Up
==========

**Github Token as Permanent Environment Variable**

Set your Github Personal Access Token as the environment variable
GITHUB\_TOKEN

.. code:: sh

   $ echo "export GITHUB_TOKEN = <your-token-within-quotes>" >> /etc/environment

**Github Token as Temporary Environment Variable**

.. code:: sh

   $ GITHUB_TOKEN = <your-token-within-quotes>

**Without saving your Environment Variable**

Open the file 

.. code:: sh

   $ clipy_github/mains.py

Change this line 

.. code:: sh

   $ API_TOKEN = os.environ.get('GITHUB_TOKEN') to API_TOKEN = <your-token-within-quotes>

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

   $ clipy-github -n harshasrinivas

Display the list of a user's repositories from the profile URL

.. code:: sh

   $ clipy-github -u https://github.com/harshasrinivas

Display all the files and folders within a repository recursively from
the repository URL

.. code:: sh

   $ clipy-github -r https://github.com/harshasrinivas/clipy-github

Get the RAW version of the readme file of a repository from the
repository URL

.. code:: sh

   $ clipy-github -R https://github.com/harshasrinivas/clipy-github

Contribute
==========

If you want to add features, improve them, or report issues, feel free
to send a pull request.

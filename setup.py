from setuptools import setup
import sys

setup(name = 'clipy-github',
      description = 'Github inside the Command Line',
      version = '0.1.0',
      author = 'Harsha Srinivas',
      author_email = '95harsha95@gmail.com',
      packages = ['clipy-github'],
      entry_points = {
          'console_scripts': ['clipy-github=clipy-github:main'],
      },
      url = 'https://github.com/harshasrinivas/clipy-github/',
      keywords = ['github', 'CLI', 'github-within-CLI', 'python'],
      install_requires = [
                  'argparse',
                  'urllib.request',
                  'base64',
                  'json',
      ],
      classifiers = [
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities'
      ],
      )

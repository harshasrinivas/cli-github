from setuptools import setup
import sys

setup(name = 'clipy-github',
      description = 'Github inside the Command Line',
      version = '0.1.2',
      author = 'Harsha Srinivas',
      author_email = '95harsha95@gmail.com',
      packages = ['clipy_github'],
      entry_points = {
          'console_scripts': ['clipy-github=clipy_github:main'],
      },
      install_requires = [      
               'prettytable',        
      ],
      url = 'https://github.com/harshasrinivas/clipy-github/',
      keywords = ['github', 'CLI', 'github-within-CLI', 'python'],
      classifiers = [
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities'
      ],
      )

from setuptools import setup
import sys

setup(name = 'cli-github',
      description = 'Github inside the Command Line',
      version = '1.0.1',
      license = 'GPL v3.0',
      author = 'Harsha Srinivas',
      author_email = '95harsha95@gmail.com',
      packages = ['cli_github'],
      entry_points = {
          'console_scripts': ['cli-github=cli_github:main'],
      },
      install_requires = [      
               'prettytable',        
      ],
      url = 'https://github.com/harshasrinivas/cli-github/',
      keywords = ['github', 'CLI', 'github-within-CLI', 'python'],
      classifiers = [
          'Operating System :: POSIX',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Utilities', 
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Version Control',
      ],
      )

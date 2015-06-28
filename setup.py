from setuptools import setup
import sys

setup(name = 'clipy-github',
      description = 'Github inside the Command Line',
      version = '0.1.4',
      license = 'GPL v3.0',
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

from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
  name = 'RokuController',         
  packages = ['RokuController'],   
  version = '1.0.2beta', 
  license='gpl-2.0',        
  description = 'An easy to use Roku cli interface.',   
  author = 'Levelfourtwenty',                
  author_email = 'level420@protonmail.com',     
  long_description=long_description,
  long_description_content_type="text/markdown",
  include_package_data=True,
  url = 'https://github.com/levelfourtwenty/RokuController/',  
  download_url = 'https://github.com/levelfourtwenty/RokuController/v_1.0.2beta.tar.gz',\
  keywords = ['Controller', 'Roku Cli', 'Roku'],
  install_requires=[            
          'requests',
          'curtsies',
	  'pyfiglet',

      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers', 
    'Topic :: Utilities',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',  
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
    entry_points = {
        'console_scripts': ['rokucontroller=RokuController.getuserinput:main'],
    }
)

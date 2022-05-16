from distutils.core import setup
setup(
  name = 'RokuController',         
  packages = ['RokuController'],   
  version = '0.2.5.9.1', 
  license='gpl-2.0',        
  description = 'An easy to use Roku cli interface.',   
  author = 'Levelfourtwenty',                
  author_email = 'level420@protonmail.com',     
  url = 'https://github.com/levelfourtwenty/RokuController/',  
  download_url = 'https://github.com/levelfourtwenty/RokuController/v_0.2.5.9.1.tar.gz',
  keywords = ['Controller', 'Roku Cli', 'Roku'],
  install_requires=[            
          'requests',
          'curtsies',
	  'pyfiglet',

      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
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

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Quick guide

INTRODUCTION
------------

This is a quick mockup sqlite3 database generator with the random data that you might need for your projects!

REQUIREMENTS
------------

* mimesis module(https://github.com/lk-geimfari/mimesis)

INSTALLATION
------------
Installation is simple with poetry toml file or via requirements.txt, whichever you prefer most
Poetry ex.:

 'poetry install'

requirements.txt:

 'pip install requirements.txt'
 
 
QUICK GUIDE
-------------
The usage of this quick script is very simple.

 How does it work - you can run it via
        poetry, ex. 
        
        'poetry run python run.py [database name] [number of people/values needed]'
  or install it python with virtual environment.
  
        'python names.py [database name] [number of people/values needed]'

It will create a mockup database for you with full name, country, city, postal code, address, region and telephone numbers.
Feel free to modify it however you want, but please, refer to documentation from Mimesis module.

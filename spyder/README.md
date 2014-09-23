Link Spyder
===========

Python script that uses Scrapy to find links from a list of hardcoded urls, saving the data to an Oracle
database via Django's Object-relational mapper (ORM), and a local .json file.

Additionally, this code generates json representation of the data, saving it to a data.json.

Example:

    obj = {"size": 200, # size of node
           "name": name, # scraped link name
           "children": [{"size": 50, # child links
                         "name": name, 
                         "children": [{"size": 50,
                                       "name": name}]}] # child child links, etc.
                                       
 Usage:
   Execute from command line:
     command prompt:> scrapy crawl link_spyder
     
     
NOTE: For information on Scrapy see: http://doc.scrapy.org/


Oracle database after population from link_spyder script:

![db](https://cloud.githubusercontent.com/assets/2049888/4366432/d46ac000-42be-11e4-95a0-dc93d07ded92.png)

Note that the initial empty database is created via Django (> python manage.py syncdb)

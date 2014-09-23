Link Spyder
===========

- A Scrapy web application that scrapes links from a webpage and saves the data to an Oracle backend.  
- Additionally, Link Spyder saves link data as a local json file (data.json). This file can be used to visualize link data.


----------


Python script that scrapes links from a list of hardcoded urls, saving the data to a Oracle
database via Django's Object-relational mapper (ORM), and a local .json file.

Additionally, this code generates json representation of the data, saving it 
to a data.json.

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

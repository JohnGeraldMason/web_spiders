'''
John Mason 08.2014

Link Spyder

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
'''

from scrapy.spider import Spider
from scrapy.selector import Selector
from spyder.items import ScrapedDataItem
from scrapy.spider import BaseSpider
import cx_Oracle
import datetime
import json, simplejson


class LinkSpider(BaseSpider):
    '''
    Spyder that scrapes links from a list of hardcoded urls, saving the data to a Oracle
    database via Django's Object-relational mapper (ORM), and a local .json file.
    '''
    
    name = "link_spyder" # name given to this spider - must be unique
    allowed_domains = ['dal.ca'] # do not search outside this domain
    start_urls = ['http://www.dal.ca/dept/its.html'] # list of urls to search


    def get_selection(self, sel, path):
        '''
        Tries to extract a value from given path.
        Returns either a value or an exception.
        '''
        
        try:
            val = sel.xpath(path).extract()
        except IndexError:
            val = 'IndexError'
            
        return val
        
        
    def parse(self, response):
        '''
        Processes the response and returns scraped data as DjangoItem object.
        '''
        
        children = [] # list of child links
        parent_node_weight = '20' # arbitrary weight - represents start_urls
        child_node_weight = '50' # arbitrary weight - these smaller nodes represent links scraped from the parent node
        
        for sel in response.xpath('//ul/li'):
            
            item = ScrapedDataItem() # database access via Django (DjangoItem)
            
            item['link'] = self.get_selection(sel, 'a/@href')[0]
            item['link_text'] = self.get_selection(sel, 'a/text()')[0]
            
            # save link data to database
            ScrapedDataItem(link = item['link'], link_text = item['link_text']).save()
            
            entry = {"name": item['link_text'], "size": child_node_weight}
            children.append(entry) #add json entry
            
        data_file = 'data.json' # this is the json file to create
        
        # open a file in write mode and save data to json file
        with open(data_file, mode='w') as feedsjson:
            feeds = {"name": self.start_urls[0], "children": children, "size": parent_node_weight}
            json.dump(feeds, feedsjson) # write json object to file
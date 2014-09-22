# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.contrib.djangoitem import DjangoItem
#from scrapy.item import Field
#from link_spyder.models import Person
from link_spyder.models import ScrapedData
#from scrapy.contrib.loader.processor import TakeFirst


class ScrapedDataItem(DjangoItem):
    '''
    # fields for this item are automatically created from the django model
    '''
    django_model = ScrapedData
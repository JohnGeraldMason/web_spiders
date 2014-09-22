from django.db import models
from scrapy.contrib.djangoitem import DjangoItem


class ScrapedData(models.Model):
    '''
    Contains data scraped from URL. Intended to be  populated via
    external scraper application.
    '''
    
    link = models.CharField(max_length=100, blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True, null=True)
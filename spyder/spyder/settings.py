# -*- coding: utf-8 -*-

# Scrapy settings for spyder project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'spyder'

SPIDER_MODULES = ['spyder.spiders']
NEWSPIDER_MODULE = 'spyder.spiders'

# TODO: Setup user agent
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_bot (+http://www.yourdomain.com)'

import sys
# Setting up django's project full path.
# eg., ***yourpath***/link_spyder_project"

# Setting up django's settings module name.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'link_spyder_project.settings'

ITEM_PIPELINES = {
    'spyder.pipelines.SpyderPipeline': 1000,
}
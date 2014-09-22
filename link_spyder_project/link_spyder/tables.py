import django_tables2 as tables
from link_spyder.models import ScrapedData
import itertools

    
class ScrapedDataTable(tables.Table):
    '''
    Model for creating the ScrapedData table.
    '''


    class Meta:
        model = ScrapedData
        attrs = {'class': 'table table-striped table-bordered'}
        # custom template - edited django-tables2's template as it display pagination correctly
        template = r'link_spyder/default_template.html'
        
# Create your views here.
from django.shortcuts import  render_to_response, render
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django_tables2 import RequestConfig
from tables import ScrapedDataTable
from link_spyder.models import ScrapedData


def home(request, template_name=r'link_spyder\link_spyder.html'):
    '''
    View for listing/sorting of link data
    '''
    
    my_list = ScrapedData.objects.all()

    # create table populated with user gist data
    table = ScrapedDataTable(my_list)  

    # the following call to 'RequestConfig' automatically obtains request.GET
    # values and updates the table, enabling data ordering and pagination
    RequestConfig(request, paginate={"per_page": 10}).configure(table)  
    
    d = dict(
        table = table
    )
    
    return render(request, template_name, d)
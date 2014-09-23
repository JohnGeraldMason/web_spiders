Web Spiders
===========

Practice/proof of concept code that includes:

Spyder
------
- A Scrapy web scraper that finds links from a webpage, and then saves the link data to an Oracle backend.
  - Additionally, Link Spyder saves link data as a local json file (data.json).


Link Spyder Project
-------------------
- Django webserver that reads link data (populated via web scraper) from a local Oracle database.


Link Visualizer
---------------

*In progress*

- An html/javascript Visualization of the scraped data contained in data.json (saved by Spyder - above). 
  - This implementation uses (D9) CodeFlower.js: http://redotheweb.com/CodeFlower/
  
- Example:
     This json file for '''http://www.dal.ca/dept/its.htm''':

    is visualized as the screenshot below:

  ![link_nodes](https://cloud.githubusercontent.com/assets/2049888/4366866/9bc95cd0-42c7-11e4-88a3-e272e4d5335a.png)


The centre node represents the url that was scraped,    http://www.dal.ca/dept/its.html. The surrounding nodes represent the links scraped. Hovering the mouse pointer over a will produce a popup displaying the link "name".

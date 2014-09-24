##Link Visualizor

[link](http://johnnymatrixxx.github.io/web_spiders)

A [link](http://example.com).

- An html/javascript Visualization of the scraped data contained in data.json (saved by Spyder - above). 
  - This implementation uses (D9) CodeFlower.js: http://redotheweb.com/CodeFlower/
  
####Example:

  - The json file from scraping '''http://www.dal.ca/faculty/computerscience.htm''', is visualized as the screenshot below:

  ![link_nodes](https://cloud.githubusercontent.com/assets/2049888/4366866/9bc95cd0-42c7-11e4-88a3-e272e4d5335a.png)


The centre node represents the url that was scraped, http://www.dal.ca/dept/its.html. The surrounding nodes represent the links scraped. Hovering the mouse pointer over a node will produce a popup displaying the link "name". Clicking and dragging a node results in a reshuffling of nodes. I made this because I thought it was neat, but this could have just as easily been a chart, a graph, a heat map, ... displayed as part of a dashboard, so I can claim some proof of concept value to this little project ;).

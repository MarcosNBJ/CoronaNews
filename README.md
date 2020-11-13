# Corona News

Expandable project to scrap the most recent news about Coronavirus from various trustable brazilian sites and present them all in one page, selecting them by region when wanted. 

This is built using [Scrapy](https://github.com/scrapy/scrapy) for scrapping and [Selenium](https://github.com/SeleniumHQ/selenium) for handling websites with javascript. There's a simple frontend built with Flask just to show how the news can be presented but anyone can also use the [ScrapyRT](https://github.com/scrapinghub/scrapyrt) endpoint to directly acess the JSON with the scrapped items and use it as desired.

## How to use it locally:

Soon, there will also be a deploy of this application running on Amazon's Elastic Container Service, for which the URL will be available here. Meanwhile, you can run the container locally 

```
docker-compose up
```
With the container up the frond-end will be accessible through localhost port 5000. If you want to change the URL of ScrapyRT's endpoint, you'll also have to change the value of the environment variable "SCRAPY_URL". 

If you desire to get just the scrapped JSON from ScrapyRT's endpoint, which by default will be at port 9080/crawl.json, the following arguments must be included in the request:
* start_requests=true
* spider_name=\<desired news provider>
* region=\<desired region> (Optional)
 
Example:
```
http://localhost:9080/crawl.json?start_requests=true&spider_name=g1&region=SP
```
## Running example:
![print](frontendPrint.png)

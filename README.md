# Web Scraping
This is an example of how to scrape web pages using Scrapy.  This project was part of a presentation I gave.  It has 2 scrapers (found in tutorial/tutorial/spiders/):

* quotes - pulls the html for 2 urls and prints it 
* charlotte - pulls the html for 2 urls, extracts the quote, author and tags for each quote and prints it


## To run the project
### Setup.  Install scrappy via the included requirements.txt

```
pip install -r requirements.txt
```

### Running the scraper
Run the scraper by typing `scrapy crawl <scraper_name>`.  Below is an example of how to run the charlotte scraper.

```
scrapy crawl charlotte
```


## To make your own Scrapy project 

### Create a new project

```
scrapy startproject tutorial
```


### Create a spider

Spiders are classes that you define and that Scrapy uses to scrape information from a website (or a group of websites). They must subclass scrapy.Spider and define the initial requests to make, optionally how to follow links in the pages, and how to parse the downloaded page content to extract data.  Here's how to create your own.  In this example its called charlotte.

```
cd tutorial/tutorial/spiders
touch charlotte_spider.py
```

### Test the spider.  

Change directory to the top directory scrapy/tutorial and run the spider
The command tells scrapy to crawl charlotte.  
It looks in the spiders directory (scrapy/tutorial/tutorial/spiders) for a class with 
a name attribute that matches the name of the spider passed to "scrapy crawl" in this case its "charlotte"

If you ran 'scrapy crawl bob' it would look for a class with the name attribute set to "bob"

```
cd ../../
scrapy crawl charlotte
```




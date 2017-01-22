####This spider just pulls back html for each url and throws it in the console

import scrapy

class QuotesSpider(scrapy.Spider): #Inhert from scrapy.Spider
    name = "quotes"


    #Create a method called start_requests that yeilds the urls to get the html from
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls: #iterate all over the urls 
            #yield has to do with generators which is beyond the scope of this lecture
            #for now you can think of it like "return"

            #tell scrapy to fetch the response (has the html) and pass it to parse when it comes back
            yield scrapy.Request(url=url, callback=self.parse) 


    #have your way with the HTML dsfds
    def parse(self, response): #response is the response from the urls fetch in start_requests
        print "************************************************"
        print response.url #url contains the url
        print "_________________"
        print response.body #body contains the html
        print "************************************************"


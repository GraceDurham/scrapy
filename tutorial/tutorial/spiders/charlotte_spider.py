####This spider just pulls back html for each url and throws it in the console

import scrapy

class CharlotteSpider(scrapy.Spider): #Inhert from scrapy.Spider
    name = "charlotte"


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


    def parse(self, response): #response is the response from the urls fetch in start_requests
        # Get the title
        print response.url

        ## Grab the response title text.  
        title = response.css('title::text').extract_first() 
        print title
        print "Here are a list of quotes:"
        print "_______________________________________\n\n"

        #get the divs with class quotes returns an array save to variable quote_divs
        quote_divs = response.css("div.quote")


        for quote_div in quote_divs:
            #extract the quote text
            quote = quote_div.css(".text::text").extract_first()
            print quote
            author =quote_div.css(".author::text").extract_first()
            print author
            tags = quote_div.css(".tag::text").extract()
            for tag in tags:
                print tag,
            
            print "\n\n******************************************************"



        print "\n\n"

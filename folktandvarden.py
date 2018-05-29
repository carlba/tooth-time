import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.folktandvardenstockholm.se/#last-min']

    def parse(self, response):
        yield response.css('div.has-help.cf').extract()



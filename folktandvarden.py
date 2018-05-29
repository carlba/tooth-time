import scrapy


class FolktandvardenSpider(scrapy.Spider):
    name = 'folktandvarden'
    start_urls = ['https://www.folktandvardenstockholm.se/#last-min']

    def parse(self, response):
        yield response.css('div.has-help.cf').extract()



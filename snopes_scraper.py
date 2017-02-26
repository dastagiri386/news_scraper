import scrapy

class SnopesItem(scrapy.Item):

    name = scrapy.Field()
    link = scrapy.Field()

class SnopesSpider(scrapy.Spider):
    name = "snopes_spider"
    d = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    start_urls = []
    base_string = 'http://www.snopes.com/2016/'
    for i in range(1, 13):
    	for j in range (1, d[i]+1):
    		start_urls.append(base_string + str(i) + '/' + str(j) + '/')

    def parse(self, response):
        for sel in response.xpath('//h2/a'):
            item = SnopesItem()
            item['name'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()

            yield item
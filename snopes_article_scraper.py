import scrapy

class NewsArticleItem(scrapy.Item):

    claim = scrapy.Field()
    rating = scrapy.Field()
    fact_checker = scrapy.Field()

class NewsArticleSpider(scrapy.Spider):
    name = "article_spider"
    start_urls = []

    f = open('snope.csv')
    l = f.readlines()
    f.close()

    for item in l:
        if item.startswith('http'):
            start_urls.append(item.split(',')[0])
    

    def parse(self, response):
        for sel in response.xpath('//body'):
            item = NewsArticleItem()
            item['claim'] = sel.xpath('//p[@itemprop="claimReviewed"]/text()').extract_first()
            if item['claim'] != None:
                item['claim'] = str(item['claim']).replace('\n', '').strip()
                item['rating'] = sel.xpath('//div[starts-with(@class, "claim")]/span/text()').extract_first()
                item['fact_checker'] = sel.xpath('//a[@class="author-link"]/text()').extract_first()
            else:
                print "claim not present"

            yield item
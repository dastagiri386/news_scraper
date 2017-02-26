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
        for sel in response.xpath('/html'):
            item = NewsArticleItem()
            item['claim'] = sel.xpath('//p[@itemprop="claimReviewed"]/text()').extract_first()
            item['rating'] = sel.xpath('//span[@itemProp="alternateName"]/text()').extract_first()
            item['fact_checker'] = sel.xpath('//a[@class="author-link"]/text()').extract_first()

            yield item
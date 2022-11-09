import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Shi300Spider(CrawlSpider):
    name = 'shi300'
    allowed_domains = ['shici.store']
    start_urls = ['https://shici.store/huajianji/www/list/%E5%94%90%E8%AF%97%E4%B8%89%E7%99%BE%E9%A6%96.html']
    lk1 = LinkExtractor(restrict_xpaths='//div[@class="ui selection list"]/div/p/a')
    # 不用解析首页，只管详情页
    rules = (
        Rule(lk1, callback='parse_item'),
    )

    def parse_item(self, response):
        href = response.xpath('//div[@class="inner-wrapper"]/div[@class="title"]/text()').extract_first().strip()
        print(href)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

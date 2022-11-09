import scrapy
from xiaoshuo17k.items import Xiaoshuo17KItem


class Xs17k2Spider(scrapy.Spider):
    name = 'xs17k2'
    allowed_domains = ['17k.com']
    start_urls = ['https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html']

    def parse(self, response, **kwargs):
        item = Xiaoshuo17KItem()
        tr_list = response.xpath('//table/tbody/tr')
        for tr in tr_list:
            num = tr.xpath('./td[1]/text()').extract_first()
            if not num:
                continue
            kind = tr.xpath('./td[2]/a/text()').extract_first()
            book_name = tr.xpath('./td[3]/span/a/text()').extract_first()
            item['num'] = num
            item['kind'] = kind
            item['book_name'] = book_name
            yield item
        hrefs = response.xpath('//div[@class="page"]/a/@href')
        for href in hrefs:
            href = href.extract()
            if href.startswith('javascript'):
                continue
            href = response.urljoin(href)
            yield scrapy.Request(
                url=href,
                method='get',
                callback=self.parse
            )




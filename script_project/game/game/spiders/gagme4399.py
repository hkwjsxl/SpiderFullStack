import scrapy
from game.items import GameItem


class Gagme4399Spider(scrapy.Spider):
    name = 'gagme4399'
    allowed_domains = ['4399.com']
    start_urls = ['https://www.4399.com/special/1.htm']

    def parse(self, response, **kwargs):
        item = GameItem()
        title_list = response.xpath('//div[@class="d_cen"]/ul/li/p[1]/a//text()')
        time_list = response.xpath('//div[@class="d_cen"]/ul/li/p[2]//text()')
        for title, time in zip(title_list, time_list):
            item['title'] = title.extract()
            item['time'] = time.extract()
            yield item




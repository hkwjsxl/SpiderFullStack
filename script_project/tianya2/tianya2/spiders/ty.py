import scrapy
import time
from scrapy_redis.spiders import RedisSpider
from tianya2.items import Tianya2Item


class TySpider(RedisSpider):
    name = 'ty'
    allowed_domains = ['bbs.tianya.cn']
    # start_urls = ['http://bbs.tianya.cn/']
    redis_key = 'ty_lst'

    def parse(self, response, **kwargs):
        tbodys = response.xpath('//div[@class="mt5"]/table/tbody')
        for tbody in tbodys:
            trs = tbody.xpath('./tr')
            for tr in trs:
                href = tr.xpath('./td/a/@href').extract_first()
                if not href:
                    continue
                href = response.urljoin(href)
                for i in range(3):
                    try:
                        yield scrapy.Request(
                            url=href,
                            callback=self.parse_detail,
                            meta={'href': href}
                        )
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(2)
        links = response.xpath('//div[@class="short-pages-2 clearfix"]/div/a/@href').extract()
        for link in links:
            if link.startswith('javascript'):
                continue
            link = response.urljoin(link)
            yield scrapy.Request(
                url=link,
                callback=self.parse,
            )

    def parse_detail(self, response, **kwargs):
        item = Tianya2Item()
        href = response.meta['href']
        texts = response.xpath('//div[@class="bbs-content clearfix"]//text()').extract()
        texts = ''.join(texts)
        texts.replace(' ', '').strip()
        item['texts'] = texts
        print(texts)
        yield item


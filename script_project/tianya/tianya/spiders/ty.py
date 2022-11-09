import scrapy
from redis import StrictRedis
from scrapy import signals
from tianya.items import TianyaItem
import time


class TySpider(scrapy.Spider):
    name = 'ty'
    allowed_domains = ['bbs.tianya.cn']
    start_urls = ['http://bbs.tianya.cn/list.jsp?item=free&order=1']
    page = 0

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def spider_opened(self, spider):
        self.conn = StrictRedis(password='20020224.')

    def spider_closed(self, spider):
        if self.conn:
            self.conn.close()

    def parse(self, response, **kwargs):
        if self.page == 3:
            exit('3页爬取成功')
        tbodys = response.xpath('//div[@class="mt5"]/table/tbody')
        for tbody in tbodys:
            trs = tbody.xpath('./tr')
            for tr in trs:
                href = tr.xpath('./td/a/@href').extract_first()
                if not href:
                    continue
                href = response.urljoin(href)
                if self.conn.sismember('ty_href_lst', href):
                    print('url 已存在!')
                    continue
                else:
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
                            time.sleep(3)
        links = response.xpath('//div[@class="short-pages-2 clearfix"]/div/a/@href').extract()
        for link in links:
            if link.startswith('javascript'):
                continue
            link = response.urljoin(link)
            self.page += 1
            yield scrapy.Request(
                url=link,
                callback=self.parse,
            )

    def parse_detail(self, response, **kwargs):
        item = TianyaItem()
        href = response.meta['href']
        self.conn.sadd('ty_href_lst', href)
        texts = response.xpath('//div[@class="bbs-content clearfix"]//text()').extract()
        texts = ''.join(texts)
        texts.replace(' ', '').strip()
        print(texts)
        item['texts'] = texts
        yield item





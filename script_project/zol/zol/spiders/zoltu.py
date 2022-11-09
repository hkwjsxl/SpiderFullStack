import scrapy
from zol.items import ZolItem


class ZoltuSpider(scrapy.Spider):
    name = 'zoltu'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/nb/']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//*[@class="pic-list2  clearfix"]/li')
        for li in li_list:
            href = li.xpath('./a/@href').extract_first()
            if not href.endswith('.html'):
                continue
            href = response.urljoin(href)
            yield scrapy.Request(
                url=href,
                method='get',
                callback=self.parse_sub,
            )

    def parse_sub(self, response, **kwargs):
        item = ZolItem()
        src = response.xpath('//img[@id="bigImg"]/@src').extract_first()
        img_name = src.split('/')[-1]
        item['img_name'] = img_name
        item['src'] = src

        yield item





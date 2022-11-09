import scrapy
from scrapy.http.response.html import HtmlResponse
from zhipin.req import SeleniumRequest


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/']

    def start_requests(self):
        yield SeleniumRequest(url='https://www.qq.com', dont_filter=True)
        # yield scrapy.Request(url='https://www.baidu.com')

    def parse(self, response: HtmlResponse, **kwargs):
        print(response.request.headers)

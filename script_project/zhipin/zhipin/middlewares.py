# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium.webdriver import Chrome
from zhipin.settings import USER_AGENTS
import random
from zhipin.req import SeleniumRequest
from scrapy.http.response.html import HtmlResponse


class ZhipinSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhipinDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def spider_opened(self, spider):
        self.driver = Chrome()
        self.driver.implicitly_wait(10)

    def spider_closed(self, spider):
        self.driver.close()

    def process_request(self, request, spider):
        if isinstance(request, SeleniumRequest):
            self.driver.get(request.url)
            page_source = self.driver.page_source
            res = HtmlResponse(
                url=request.url,
                status=200,
                body=page_source.encode('utf-8'),
                request=request
            )
            print('selenium')
            return res
        else:
            print('普通')
            return None
        # ua = random.choice(USER_AGENTS)
        # request.headers['User-Agent'] = ua

    def process_response(self, request, response, spider):

        return response


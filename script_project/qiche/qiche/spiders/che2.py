import scrapy
from scrapy.linkextractors import LinkExtractor


class Che2Spider(scrapy.Spider):
    name = 'che2'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']

    def parse(self, response, **kwargs):
        # lk1 = LinkExtractor(restrict_xpaths='//div[@id="listpagination"]')
        # lk1 = LinkExtractor(restrict_xpaths='//div[@class="viewlist_ul"]')
        # links = lk1.extract_links(response)
        # for link in links:
        #     print(link.url)
        #     print(link.text)
        lk2 = LinkExtractor(allow=r'beijing/a0_0msdgscncgpi1ltocsp\d+exx0')
        links2 = lk2.extract_links(response)
        for link in links2:
            print(link.url)
            print(link.text)

import scrapy
from caipiao.items import CaipiaoItem


class CaiSpider(scrapy.Spider):
    name = 'cai'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs']

    def parse(self, response, **kwargs):
        item = CaipiaoItem()
        tr_list = response.xpath('//*[@id="cpdata"]/tr')
        for tr in tr_list:
            qihao = tr.xpath('./td[1]/text()').extract_first()
            if not qihao:
                continue
            red_ball = tr.xpath('./td[@class="chartball01"]/text()').extract_first()
            blue_ball = tr.xpath('./td[@class="chartball02"]/text()').extract_first()
            item['qihao'] = qihao
            item['red_ball'] = red_ball
            item['blue_ball'] = blue_ball
            yield item

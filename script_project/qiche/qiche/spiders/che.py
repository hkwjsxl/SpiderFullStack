import scrapy
from lxpy import copy_headers_dict


class CheSpider(scrapy.Spider):
    name = 'che'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']

    che_info = {
        '表显里程': 'licheng',
        '上牌时间': 'time',
        '挡位/排量': 'pailiang',
        '车辆所在地': 'addr',
        '查看限迁地': 'xianqiandi',
    }

    def start_requests(self):
        cookies = 'fvlid=1659838529121mp3xpAdu9lJx; sessionid=3463785a-2719-48e5-8541-33177697c46a; area=130423; smidV2=20220807103029f4181d8bc28a834ccbe5d58a0f22f63100699d033837cba00; pcpopclub=6e166019808a40a6a85bcf65acd74b420e3cdcaa; clubUserShow=238869674|0|2|%e7%a7%a6%e7%9a%87%e5%b2%9b%e8%bd%a6%e5%8f%8b8374289|0|0|0|/g27/M0A/00/6C/120X120_0_q87_autohomecar__ChsEnV9HeGeARcQkAACbROlbgag975.jpg|2022-08-07 10:30:41|0; listuserarea=110100; sessionip=60.5.116.67; sessionvisit=f817582c-13f4-4da1-88b1-82dae2b3ee41; sessionvisitInfo=3463785a-2719-48e5-8541-33177697c46a|www.autohome.com.cn|100533; UsedCarBrowseHistory=0%3A44209229; usedcaruid=91ZmM3Kvte7X+7MPMWm/eQ==; memberPhoneInfo=%7C18533538210%7C1; userarea=110000; ahpvno=6; showNum=15; sessionuid=3463785a-2719-48e5-8541-33177697c46a'
        lst = cookies.split(';')
        cookies = {}
        for l in lst:
            k = l.split('=')[0]
            v = l.split('=')[1]
            cookies[k] = v
        yield scrapy.Request(
            url=self.start_urls[0],
            cookies=cookies,
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        href_list = response.xpath('//ul[@class="viewlist_ul"]/li/a/@href').extract()
        for href in href_list:
            href = response.urljoin(href)
            if 'topicm.che168.com' in href:
                continue
            yield scrapy.Request(
                url=href,
                callback=self.parse_detail
            )
        page_list = response.xpath('//div[@id="listpagination"]/a/@href').extract()
        for page in page_list:
            if page.startswith('javascript'):
                continue
            page_url = response.urljoin(page)
            yield scrapy.Request(
                url=page_url,
                callback=self.parse
            )

    def parse_detail(self, response, **kwargs):
        che_data = {
            'licheng': '未知',
            'time': '未知',
             'pailiang': '未知',
             'addr': '未知',
             'xianqiandi': '未知',
        }
        title = response.xpath('//div[@class="car-box"]/*[@class="car-brand-name"]/text()').extract_first()
        if not title:
            title = '未知'
        title = title.strip()
        p_list = response.xpath('//div[@class="car-box"]/ul[@class="brand-unit-item fn-clear"]/li/p//text()').extract()
        h4_list = response.xpath('//div[@class="car-box"]/ul[@class="brand-unit-item fn-clear"]/li/h4/text()').extract()
        data = {}
        for p, h4 in zip(p_list, h4_list):
            p = p.replace(' ', '').strip()
            h4 = h4.strip()
            if p in self.che_info.keys():
                k = self.che_info[p]
                che_data[k] = h4
            data[title] = che_data
        print(data)
        yield data


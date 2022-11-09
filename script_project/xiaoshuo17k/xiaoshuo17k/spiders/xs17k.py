import scrapy


class Xs17kSpider(scrapy.Spider):
    name = 'xs17k'
    allowed_domains = ['17k.com']
    start_urls = ['https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919']

    def start_requests(self):
        yield scrapy.Request(
            url='https://passport.17k.com/ck/user/login',
            method='post',
            body='loginName=18533538210&password=20020224.',
            callback=self.login_success
        )

    def login_success(self, response, **kwargs):
        yield scrapy.Request(
            url=self.start_urls[0],
            method='get',
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        data = response.json()['data']
        for i in data:
            print(i['bookName'])



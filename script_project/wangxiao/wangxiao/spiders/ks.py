import scrapy
import json


class KsSpider(scrapy.Spider):
    name = 'ks'
    allowed_domains = ['ks.wangxiao.cn']
    start_urls = ['https://ks.wangxiao.cn/']

    def parse(self, response, **kwargs):
        li_list = response.xpath('//ul[@class="first-title"]/li')
        for li in li_list:
            first_title = li.xpath('./p/span/text()').extract_first()
            second_title = li.xpath('./div/a/text()').extract_first()
            second_hrefs = li.xpath('./div/a/@href').extract()
            for second_href in second_hrefs:
                second_href = response.urljoin(second_href)
                # print(first_title, second_title, second_href)
                # https://ks.wangxiao.cn/TestPaper/list?sign=jz1
                # https://ks.wangxiao.cn/exampoint/list?sign=jz1
                second_href = second_href.replace('TestPaper', 'exampoint')
                yield scrapy.Request(
                    url='https://ks.wangxiao.cn/exampoint/list?sign=jz1',
                    callback=self.parse_second,
                    meta={
                        'first_title': '工程类',
                        'second_title': second_title,
                    }
                )
                return
                # yield scrapy.Request(
                #     url=second_href,
                #     callback=self.parse_second,
                #     meta={
                #         'first_title': first_title,
                #         'second_title': second_title,
                #         'second_href': second_href,
                #     }
                # )

    def parse_second(self, response, **kwargs):
        first_title = response.meta.get('first_title')
        second_title = response.meta.get('second_title')
        title_href_list = response.xpath('//div[@class="filter-item"]/a/@href').extract()
        for title_href in title_href_list:
            title_href = response.urljoin(title_href)
            yield scrapy.Request(
                url=title_href,
                callback=self.parse_third,
                meta={
                    'first_title': first_title,
                    'second_title': second_title,
                }
            )
            return

    def parse_third(self, response, **kwargs):
        first_title = response.meta.get('first_title')
        second_title = response.meta.get('second_title')
        chapter_items = response.xpath('//div[@class="panel-content"]/ul[@class="chapter-item"]')
        for chapter_item in chapter_items:
            section_point_items = chapter_item.xpath('.//ul[@class="section-point-item"]')
            if section_point_items:
                for section_point_item in section_point_items:
                    ul_list = section_point_item.xpath('./ancestor::ul[@class="chapter-item" or @class="section-item"]')
                    title_list = [first_title, second_title]
                    for ul in ul_list:
                        chapter_title = ''.join(ul.xpath('./li[1]//text()').extract()).replace(' ', '').strip()
                        title_list.append(chapter_title)
                    question_title = ''.join(section_point_item.xpath('./li[1]//text()').extract()).replace(' ', '').strip()
                    question_num = section_point_item.xpath('./li[2]//text()').extract_first().split('/')[1]
                    data_sign = section_point_item.xpath('./li[3]/span/@data_sign').extract_first()
                    data_subsign = section_point_item.xpath('./li[3]/span/@data_subsign').extract_first()
                    # print(title_list, question_num)
                    all_title = '/'.join(title_list)
                    # print(all_title, question_num)
                    # https://ks.wangxiao.cn/practice/listQuestions
                    cookies_dic = self.get_cookies()
                    data = {
                        'examPointType': "",
                        'practiceType': "2",
                        'questionType': "",
                        'sign': data_sign,
                        'subsign': data_subsign,
                        'top': question_num,
                    }
                    data = json.dumps(data)
                    yield scrapy.Request(
                        url='https://ks.wangxiao.cn/practice/listQuestions',
                        method='post',
                        callback=self.parse_question,
                        headers={'Content-Type': 'application/json; charset=UTF-8'},
                        cookies=cookies_dic,
                        body=data,
                        meta={
                            'question_dir': all_title,
                            'question_title': question_title,
                        }
                    )
                    # return
            else:
                title_list = [first_title, second_title]
                question_title = ''.join(chapter_item.xpath('./li[1]//text()').extract()).replace(' ', '').strip()
                question_num = chapter_item.xpath('./li[2]//text()').extract_first().split('/')[1]
                data_sign = chapter_item.xpath('./li[3]/span/@data_sign').extract_first()
                data_subsign = chapter_item.xpath('./li[3]/span/@data_subsign').extract_first()
                all_title = '/'.join(title_list)
                cookies_dic = self.get_cookies()
                data = {
                    'examPointType': "",
                    'practiceType': "2",
                    'questionType': "",
                    'sign': data_sign,
                    'subsign': data_subsign,
                    'top': question_num,
                }
                data = json.dumps(data)
                yield scrapy.Request(
                    url='https://ks.wangxiao.cn/practice/listQuestions',
                    method='post',
                    callback=self.parse_question,
                    headers={'Content-Type': 'application/json; charset=UTF-8'},
                    cookies=cookies_dic,
                    body=data,
                    meta={
                        'question_dir': all_title,
                        'question_title': question_title,
                    }
                )
                    # return
            # return

    def parse_question(self, response, **kwargs):
        question_dir = response.meta.get('question_dir')
        question_title = response.meta.get('question_title')
        # print(question_dir, question_title)
        # print(response.json())
        data_list = response.json().get('Data')
        for data in data_list:
            questions = data.get('questions')
            if questions:
                for question in questions:
                    question_info = self.get_question_info(question)
                    # print(question_info)
                    yield {
                        'question_dir': question_dir,
                        'question_title': question_title,
                        'question_info': question_info,
                    }
            else:
                materials = data.get('materials')
                for material in materials:
                    material_content = material.get('material').get('content')
                    questions = material.get('questions')
                    lst = []
                    for question in questions:
                        question_info = self.get_question_info(question)
                        lst.append(question_info)
                    question_info = '材料：' + material_content + '\n' + ''.join(lst)
                    # print(question_info)
                    yield {
                        'question_dir': question_dir,
                        'question_title': question_title,
                        'question_info': question_info,
                    }

    def get_question_info(self, question):
            title = question.get('content')
            options = question.get('options')
            option_lst = []
            for option in options:
                option_title = option.get('content')
                is_right = option.get('isRight')
                option_name = option.get('name')
                if is_right:
                    option_lst.append(option_name + '.' + option_title + '  (正确)' + '\n')
                else:
                    option_lst.append(option_name + '.' + option_title + '\n')
            text_analysis = question.get('textAnalysis')
            # print(title + '\n' + ''.join(option_lst) + '解析：' + text_analysis + '\n\n')
            return title + '\n' + ''.join(option_lst) + '解析：' + text_analysis + '\n'

    def get_cookies(self):
        cookies = 'mantis6894=d40cea5db57a4465a1384796c4797224@6894; sign=jz1; wxLoginUrl=https%3A%2F%2Fks.wangxiao.cn%2Fexampoint%2Flist%3Fsign%3Djz1%26subsign%3D22c51d8d3ccb4e309a60; userInfo=%7B%22userName%22%3A%22pc_503293580%22%2C%22token%22%3A%227f36fe73-195a-44c8-aaac-eb2d44cd9b5a%22%2C%22headImg%22%3Anull%2C%22nickName%22%3A%22185****8210%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%221z64NaUKVORPu2zayMp%2FjA%3D%3D%22%2C%22passwordCookies%22%3A%22c0WJgMqEJgm6kUD64502MQ%3D%3D%22%7D; token=7f36fe73-195a-44c8-aaac-eb2d44cd9b5a; UserCookieName=pc_503293580; OldUsername2=1z64NaUKVORPu2zayMp%2FjA%3D%3D; OldUsername=1z64NaUKVORPu2zayMp%2FjA%3D%3D; OldPassword=c0WJgMqEJgm6kUD64502MQ%3D%3D; UserCookieName_=pc_503293580; OldUsername2_=1z64NaUKVORPu2zayMp%2FjA%3D%3D; OldUsername_=1z64NaUKVORPu2zayMp%2FjA%3D%3D; OldPassword_=c0WJgMqEJgm6kUD64502MQ%3D%3D; pc_503293580_exam=fangchan'
        cookies = cookies.split(';')
        cookies_dic = {}
        for cookie in cookies:
            k = cookie.split('=')[0]
            v = cookie.split('=')[1]
            cookies_dic[k] = v
        return cookies_dic





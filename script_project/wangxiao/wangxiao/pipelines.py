from itemadapter import ItemAdapter
import os
from lxml import etree
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class WangxiaoPipeline:
    def process_item(self, item, spider):
        question_dir = item['question_dir']
        question_title = item['question_title']
        question_info = item['question_info']
        file_path = question_dir + '/' + question_title
        # print(question_dir, question_title)
        # print(question_info)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(file_path + '/' + question_title + '.md', 'a', encoding='utf-8') as f:
            for line in question_info:
                f.write(line)
        # print(question_title, '下载完成')
        return item


# 管道
class DownImgPipline(ImagesPipeline):
    # 发送请求
    def get_media_requests(self, item, info):
        question_dir = item['question_dir']
        question_title = item['question_title']
        question_info = item['question_info']
        tree = etree.HTML(question_info)
        srcs = tree.xpath('//img/@src')
        for src in srcs:
            yield scrapy.Request(
                url=src,
                meta={
                    'question_dir': question_dir,
                    'question_title': question_title,
                    'src': src,
                }
            )

    # 存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        question_dir = request.meta['question_dir']
        question_title = request.meta['question_title']
        src = request.meta['src']
        file_name = src.split('/')[-1]
        real_path = question_dir + '/' + question_title + '_images' + '/' + file_name
        return real_path

    # 对item进行更新
    def item_completed(self, results, item, info):
        # print(results)
        try:
            if results:
                for result in results:
                    if result[0]:
                        dic = result[1]
                        url = dic['url']
                        path = dic['path']
                        lst = path.split('/')[-2:]
                        real_path = '../' + lst[0] + '/' + lst[1]
                        item['question_info'] = item['question_info'].replace(url, real_path)
                    return item
        except Exception as e:
            print(e)
        return item



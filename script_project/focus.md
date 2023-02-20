## scrapy下载图片

~~~python
IMAGES_STORE = './'

from scrapy.pipelines.images import ImagesPipeline

# 管道
class DownImgPipline(ImagesPipeline):
    # 发送请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['src'])

    # 存储路径
    def file_path(self, request, response=None, info=None, *, item=None):
        file_path = 'zol_file'
        file_name = item['img_name']
        real_path = os.path.join(file_path, file_name)
        item['file_path'] = real_path
        return real_path

    # 对item进行更新
    def item_completed(self, results, item, info):
        print(results)
        return item
~~~

## 运行

~~~python
from scrapy.cmdline import execute
execute('scrapy crawl ---'.split())
~~~

## 代码提示

~~~python
from scrapy.http.response.html import HtmlResponse
response: HtmlResponse
~~~

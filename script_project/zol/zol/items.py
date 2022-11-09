# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_name = scrapy.Field()
    src = scrapy.Field()
    file_path = scrapy.Field()

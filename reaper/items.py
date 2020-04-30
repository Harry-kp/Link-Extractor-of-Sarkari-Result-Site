# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
#from scrapy_djangoitem import DjangoItem
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class SarkariResult(scrapy.Item):
    Name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    Link = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    Last_Date = scrapy.Field(

        output_processor=TakeFirst()
    )

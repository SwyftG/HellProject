# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose,Join, Compose
import re

class HellprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TtmjTvPlayItem(scrapy.Item):
    tv_play_name = scrapy.Field()
    tv_play_rank = scrapy.Field()
    tv_play_category = scrapy.Field()
    tv_play_state = scrapy.Field()
    tv_play_update_day = scrapy.Field()
    tv_play_return_date = scrapy.Field()
    tv_play_counting_data = scrapy.Field()
    tv_play_url = scrapy.Field()

class JavpopItem(scrapy.Item):
    video_url = scrapy.Field()
    video_title = scrapy.Field()
    video_num = scrapy.Field()
    video_img_poster = scrapy.Field()
    video_img_screenshot = scrapy.Field()
    video_tags = scrapy.Field()
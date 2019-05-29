# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/4/28 6:47 PM'
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


def get_video_num(data_value):
    return data_value[0][1:-1]

class JavpopLoader(ItemLoader):
    video_title_out = TakeFirst()
    video_url_out = TakeFirst()
    video_num_out = Compose(get_video_num)
    video_img_poster_out = Join()
    # video_img_screenshot_out = Join()
    # video_tags_out = Join()

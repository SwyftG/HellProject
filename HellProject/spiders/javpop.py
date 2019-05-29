# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import *
import re


class PlayrankingSpider(CrawlSpider):
    name = 'javpop2'
    allowed_domains = ['javpop.com']
    root_url = "http://javpop.com/"
    start_urls = ['http://javpop.com/category/idol']

    rules = (
        Rule(LinkExtractor(allow='.*\.html', restrict_xpaths='//div[@class="entry"]//li/a[1]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="wp-pagenavi"]/a[contains(.,"Next")]')),
    )

    def parse_item(self, response):
        item = JavpopItem()
        page_url = response.url
        page_title = response.xpath('//div[@class="box-b"]/h1/text()').extract_first()
        re_pattern = '\[.*\]'
        page_num_temp_list = re.findall(re_pattern, page_title)
        if page_num_temp_list:
            page_num = page_num_temp_list[0][1:-1]
        page_img_poster = response.xpath('//div[@class="box-b"]/div[@class="entry"]/p[@class="poster"]/img/@src').extract()
        page_img_screenshot = response.xpath('//div[@class="box-b"]/div[@class="entry"]/p[@class="screenshot"]/img/@src').extract()
        page_tag_list = response.xpath('//div[@class="box-b"]/div[@class="entry"]/div[@class="post-meta"]/div/p/a/text()').extract()
        item['video_title'] = page_title
        item['video_url'] = page_url
        item['video_num'] = page_num
        item['video_img_poster'] = page_img_poster
        item['video_img_screenshot'] = page_img_screenshot
        item['video_tags'] = page_tag_list
        print(item)





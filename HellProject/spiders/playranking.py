# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from ..items import *
import re
from urllib.parse import quote


class PlayrankingSpider(CrawlSpider):
    name = 'playranking'
    allowed_domains = ['www.ttmeiju.me']
    # start_urls = ['http://www.ttmeiju.me/']
    root_url = "http://www.ttmeiju.me/"
    start_urls = ['http://www.ttmeiju.me/index.php/summary/index/p/1.html']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="pagination"]//a[@class="next"]'), callback='parse_item'),
    )

    def parse_start_url(self, response):
        self.parse_top_three(response)
        self.parse_normal_item(response)
        print(response.url)

    def parse_item(self, response):
        self.parse_normal_item(response)
        print(response.url)


    def parse_top_three(self,response):
        top_3_div_list = response.xpath('//div[@class="ranktop3"]').extract()
        for div_item in top_3_div_list:
            tv_item = TtmjTvPlayItem()
            selector = Selector(text=div_item)
            tv_item['tv_play_rank'] = selector.xpath('//div[@class="ranknum"]/text()').extract_first()
            tv_item['tv_play_name'] = selector.xpath('//div[@class="mjtit"]//a/text()').extract_first()
            play_info = selector.xpath('//div[@class="mjinfo"]').extract()
            play_info_list = self.remove_html_tag(play_info)
            tv_info_list = play_info_list[0].split('/')
            for index, info_item in enumerate(tv_info_list):
                if index == 0:
                    tv_item['tv_play_category'] = info_item
                elif index == 1:
                    tv_item['tv_play_state'] = info_item
                elif index == 2:
                    tv_item['tv_play_state'] = info_item
            tv_item['tv_play_return_date'] = play_info_list[1]
            tv_item['tv_play_url'] = self.root_url + selector.xpath('//div[@class="mjtit"]//a/@href').extract_first()[1:]
            print(tv_item)

    def remove_html_tag(self, play_info):
        result = list()
        html_tag_pattern = re.compile('<[^>]+>')
        for item in play_info:
            result.append(html_tag_pattern.subn('', item)[0])
        return result

    def parse_normal_item(self, response):
        tr_list = response.xpath('//tr[contains(@class, "Scontent")]').extract()
        for content in tr_list:
            tv_item = TtmjTvPlayItem()
            selector = Selector(text=content)
            td_list = selector.xpath('//td/text()').extract()
            tv_name = selector.xpath('//td[@align="left"]//a/text()').extract_first()
            tv_item['tv_play_name'] = tv_name
            for index, td_item in enumerate(td_list):
                td_item = td_item.replace('\t', '').strip()
                if index == 0:
                    tv_item['tv_play_rank'] = td_item
                elif index == 1:
                    tv_item['tv_play_category'] = td_item
                elif index == 2:
                    tv_item['tv_play_state'] = td_item
                elif index == 3:
                    tv_item['tv_play_update_day'] = td_item
                elif index == 4:
                    tv_item['tv_play_return_date'] = td_item
                elif index == 5:
                    tv_item['tv_play_counting_data'] = td_item
            # xpath 取属性用 @+属性名
            tv_item['tv_play_url'] = self.root_url + selector.xpath('//td[@align="left"]//a/@href').extract_first()[1:]

            print(tv_item)
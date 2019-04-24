# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from ..items import *
from urllib.parse import quote


class PlayrankingSpider(CrawlSpider):
    name = 'playranking'
    allowed_domains = ['www.ttmeiju.me']
    # start_urls = ['http://www.ttmeiju.me/']
    root_url = "http://www.ttmeiju.me/"
    start_urls = ['http://www.ttmeiju.me/index.php/summary/index/p/1.html']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="pagination"]//a[@class="next"]'), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        print(response.url)
        print(response.url)
        print(response.url)


    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        name_list = response.xpath('//td[@align="left"]//a/text()').extract()
        # tr_list = response.xpath('//tr[contains(@class, "Scontent")]')   111
        tr_list = response.xpath('//tr[contains(@class, "Scontent")]').extract()
        for content in tr_list:
            # name = content.xpath('//td[@align="left"]//a/text()').extract() 111
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

            # print(name)
            # print(rank)
        # print(response.url)
        # print(name_list)
        # print(tr_list)

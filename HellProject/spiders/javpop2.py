# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from ..utils import get_config
from ..rules import rules


class JavpopSpider(CrawlSpider):
    name = 'javpop'
    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'datetime':
                self.start_urls = list(eval('urls.' + start_urls.get('name'))(start_urls.get('date')))
        self.allowed_domains = config.get('allowed_domains')
        super(JavpopSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'), **{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            # yield loader.load_item()
            print(loader.load_item())



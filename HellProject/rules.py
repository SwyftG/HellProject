# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2019/5/28 11:35 PM'
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'javpop': (
        Rule(LinkExtractor(allow='.*\.html', restrict_xpaths='//div[@class="entry"]//li/a[1]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="wp-pagenavi"]/a[contains(.,"Next")]')),
    )
}
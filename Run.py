# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2018/5/11 上午11:27'

import sys
from scrapy import cmdline
from HellProject.utils import get_config
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import os

def run_spider():
    # cmdline.execute("scrapy crawl playranking".split())
    cmdline.execute("scrapy crawl javpop2".split())

def run_spider_by_json():
    name = "javpop"
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'jxxpop')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    # run_spider()
    run_spider_by_json()
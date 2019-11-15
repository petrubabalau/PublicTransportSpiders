# -*- coding: utf-8 -*-
import scrapy


class TramsSpiderSpider(scrapy.Spider):
    name = 'trams_spider'
    allowed_domains = ['www.stbsa.ro']
    start_urls = ['http://www.stbsa.ro/']

    def parse(self, response):
        self.logger.info("Starting spider..")

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from w3lib.html import remove_tags


class TramsSpiderSpider(scrapy.Spider):
    name = 'trams_spider'
    allowed_domains = ['www.stbsa.ro']
    start_urls = ['http://www.stbsa.ro/v_tramvai.php']

    def parse(self, response):
        self.logger.info("Starting spider..")
        tram_lines = response.xpath(
            './/select[@name="tlin1"]/option/@value').getall()
        # Remove 0 from the tram_lines list.
        tram_lines.remove('0')

        for line in tram_lines[:1]:
            formdata = {'tlin1': line}
            yield FormRequest.from_response(response,
                                            formdata=formdata,
                                            callback=self.parse_line)

    def parse_line(self, response):
        title = response.xpath('..//h3').get()
        title = remove_tags(title).strip()
        self.logger.info(title)
        type_ = response.xpath('..//table//table//table[2]//tr[2]/td').get()
        type_ = remove_tags(type_).strip()
        self.logger.info(type_)

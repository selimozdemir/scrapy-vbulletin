# -*- coding: utf-8 -*-
import scrapy


class HukukiSpider(scrapy.Spider):
    name = 'hukuki'
    allowed_domains = ['hukuki.net']
    # start_urls = ['http://www.hukuki.net/archive/index.php?f-26-p-1.html']

    fid = 86
    total = 8

    def start_requests(self):
        base = 'http://www.hukuki.net/archive/index.php?f-{:d}-p-{:d}.html'

        for i in range(1,self.total+1):
            yield scrapy.Request(url=base.format(self.fid, i), callback=self.parse)

    def parse(self, response):
        for link in response.css('#content > ol > li'):
            yield {'threads': link.css('a::attr(href)').extract_first()}

        # for next_page in response.css('div#pagenumbers > a'):
        #     yield response.follow(next_page, self.parse)

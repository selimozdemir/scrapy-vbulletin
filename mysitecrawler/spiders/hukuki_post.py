# -*- coding: utf-8 -*-
import json

import scrapy


class HukukiPostSpider(scrapy.Spider):
    name = 'hukuki-post'
    allowed_domains = ['hukuki.net']
    # start_urls = ['http://hukuki.net/']
    ids = [26,72,73,86]

    def start_requests(self):
        for id in self.ids:
            with open("threadlinks_{:d}.json".format(id), "r") as f:
                threadlinks = f.read()
                threadlinks = json.loads(threadlinks)


            for link in threadlinks:
                thread = link.get("threads")
                yield scrapy.Request(url=thread, callback=self.parse)

    def parse(self, response):
        posts = []
        for post in response.css('.post .posttext'):
            posts.append({'post': post.css("div::text").extract() })

        yield { 'title' : response.css('title::text').extract(), 'posts': posts }


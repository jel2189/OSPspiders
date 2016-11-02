# -*- coding: utf-8 -*-
import scrapy


class HccsSpider(scrapy.Spider):
    name = "hccs"
    allowed_domains = ["http://learning.hccs.edu/resources_search_results.html"]
    start_urls = (
        'http://learning.hccs.edu/resources_search_results.html/',
    )

    def parse(self, response):
        return scrapy.FormRequest.from_response(
		response,
		formname = 'search',
		formdata = {'checkbox':'Animation',}
	)

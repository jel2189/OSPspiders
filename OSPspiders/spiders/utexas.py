# -*- coding: utf-8 -*-
import scrapy


class UtexasSpider(scrapy.Spider):
	name = "utexas"
	allowed_domains = ["https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/"]
	start_urls = (
			'https://utdirect.utexas.edu/apps/student/coursedocs/nlogon/',
		     )

	def parse(self, response):
		item = PageItem(url=allowed_domains[0], spider_name=name)		
		print(item)
		return scrapy.FormRequest.from_response(
				response,
				formdata={'semester':'20152'},
				)

# -*- coding: utf-8 -*-
import scrapy
import syllascrape

class UFLSpider(scrapy.Spider):
	name = "ufl"
	allowed_domains = ["http://syllabus.ufl.edu"]
	start_urls = (
			'http://syllabus.ufl.edu',
		     )

	def parse(self, response):
		css = response.css('html').extract()
		print(css)
		return

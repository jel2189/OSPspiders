# -*- coding: utf-8 -*-
import scrapy


class UFLSpider(scrapy.Spider):
	name = "ufl"
	allowed_domains = ["syllabus.ufl.edu"]
	start_urls = (
			'syllabus.ufl.edu',
		     )

	def parse(self, response):
		return

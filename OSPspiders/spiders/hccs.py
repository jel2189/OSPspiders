# -*- coding: utf-8 -*-
import scrapy
import syllascrape

class HccsSpider(scrapy.Spider):
	name = "hccs"
	allowed_domains = ["learning.hccs.edu","http://learning.hccs.edu/resources_search_results.html"]
	start_urls = (
			'http://learning.hccs.edu/resources_search_results.html/',
		     )

#All posted syllabi on HCCS database have "syllabus" in document title, so search for "syllabus"
	def parse(self, response):
		return scrapy.FormRequest(
				response.url,
				formdata = {'SearchableText':'Syllabus'},
				method = 'POST',
				callback = self.parseResults,
				)

	def parseResults(self, response):
		print(response.css('html').extract())
		return

# -*- coding: utf-8 -*-
import scrapy


class LonestarSpider(scrapy.Spider):
	name = "lonestar"
	custom_settings = {"COOKIES_ENABLED":True,
		"COOKIES_DEBUG":True,
		"DOWNLOADER_MIDDLEWARES":{
			'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':700,
		}} 
	allowed_domains = ["https://my.lonestar.edu/psp/porguest/EMPLOYEE/CAMP/c/LSC_SYL.LSC_SYL_SRCH.GBL?&"]
	start_urls = (
			'https://my.lonestar.edu/psp/porguest/EMPLOYEE/CAMP/c/LSC_SYL.LSC_SYL_SRCH.GBL?&',
		     )

	def parse(self, response):
		print('hello!!!!!!')
		#print(response.css('#LSC_SYL_SRCH_VW_DESCR'))
		print(response.css('html').extract())
		request1 = scrapy.FormRequest(
			response.url,
			formdata = {'LSC_SYL_SRCH_VW_DESCR':'a'},
#clickdata = {'ICSearch':'Search'},
			callback = self.parsePage,
			)
		return

	def parsePage(self,response): 
		wholePage = response.css('html').extract()
		print(wholePage)
		return

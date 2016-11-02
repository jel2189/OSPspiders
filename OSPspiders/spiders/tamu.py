# -*- coding: utf-8 -*-
import scrapy

class TamuSpider(scrapy.Spider):
	name = "tamu"
	allowed_domains = ["http://www.tamu.edu"]
	start_urls = (
			'https://compass-ssb.tamu.edu/pls/PROD/bwckschd.p_disp_dyn_sched',
		     )
	
#	def parse_termSelect(self, response):
#			print('parse function')
#			termForm = scrapy.FormRequest.from_response(
#				response,
#				formdata = {'p_term':'201631'},
#				#callback = self.parse_subjSelect	
#			)
#			return termForm
#	
#	def parse_subjSelect(self, response):
#		print('sel_subject function')
#		return scrapy.FormRequest.from_response(
#			termForm.response,
#			formdata = {'sel_subj':'ACCT'},
#			callback = self.scrape
#		)
#	def scrape(self, response):
#		print('we made it!')
	
	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			formdata={'p_term':'201631'},
			callback=self.sel_subject
		)
	def sel_subject(self,response):
		return scrapy.FormRequest.from_response(
			response,
			formdata={'sel_subj':'ACCT'},
			callback=self.finish
		)
	def finish(self, response):
		print("Tell me something good!")
		return 0


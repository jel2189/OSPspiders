# -*- coding: utf-8 -*-

# Turns out this isn't necessary

# import json
# import scrapy
# from scrapy.selector import Selector
# from syllascrape.items import PageItem 

# class UCFSpider(scrapy.spiders.Spider):
#     name = "ucf"
#     allowed_domains = ["ucf.edu"]

#     start_urls_type_1 = (
#         "http://philosophy.cah.ucf.edu/",
#         "http://theatre.cah.ucf.edu/",
#         "http://music.cah.ucf.edu/",
#         "http://mll.cah.ucf.edu/",
#         "http://writingandrhetoric.cah.ucf.edu/",
#         "http://svad.cah.ucf.edu/",
#         "http://middleeasternstudies.cah.ucf.edu/",
#         "http://american.cah.ucf.edu/courses/",
#         "http://english.cah.ucf.edu/courses.php"
#     )

#     start_urls_type_2 = (
#         "http://africana.cah.ucf.edu/courses/",
#     )

#     def start_requests(self):
#         def start_form_requests(response):
#             url = response.meta["base_url"] + "common/courses.php"

#             terms = response.css("#terms option::attr(value)").extract()[1:]
#             print("1",response.css("#terms"))
#             for term in terms:
#                 yield scrapy.FormRequest(
#                     url,
#                     formdata={
#                         "cr": "",
#                         "term": term,
#                         "pf": "",
#                         "did": "20",
#                     },
#                     method='POST',
#                     meta={
#                         "depth": 1,
#                         "hops_from_seed": 1,
#                         "source_url": response.url,
#                         "source_anchor": "",
#                     },
#                     callback=self.parse
#                 )

#         for base_url in UCFSpider.start_urls:
#             yield scrapy.Request(
#                 base_url + "courses.php", 
#                 callback=start_form_requests,
#                 meta={"base_url":base_url},
#             )

#     def parse(self, response):
#         file_urls = []

#         jsonResponse = json.loads(response.body_as_unicode())
#         courses = jsonResponse["Response"]["Results"]
#         for course in courses:
#             syllabus = course["syllabus"]
#             if syllabus != "Unavailable":
#                 syllabus_link = Selector(text=syllabus)
#                 syllabus_href = syllabus_link.css("a::attr(href)").extract_first()
#                 syllabus_anchor = syllabus_link.css("a::text").extract_first()
#                 if syllabus_href:
#                     meta = {
#                         'source_url': response.url,
#                         'source_anchor': syllabus_anchor,
#                         'depth': response.meta['depth'] + 1,
#                         'hops_from_seed': response.meta['hops_from_seed'] + 1,
#                     }
#                     file_urls.append((syllabus_href,meta))

#         yield PageItem(
#             url=response.url,
#             content=response.body,
#             headers=response.headers,
#             status=response.status,
#             source_url=response.meta.get('source_url'),
#             source_anchor=response.meta.get('source_anchor'),
#             depth=response.meta.get('depth'),
#             hops_from_seed=response.meta.get('hops_from_seed'),
#             file_urls=file_urls,
#         )

# Database URLs:
# http://philosophy.cah.ucf.edu/courses.php type1
# http://theatre.cah.ucf.edu/courses.php type1
# http://music.cah.ucf.edu/courses.php type1
# http://mll.cah.ucf.edu/courses.php type1
# http://history.cah.ucf.edu/courses.php type1
# http://writingandrhetoric.cah.ucf.edu/courses.php type1
# http://svad.cah.ucf.edu/courses.php type1
# http://middleeasternstudies.cah.ucf.edu/courses.php type1 
# http://sciences.ucf.edu/anthropology/about/syllabi/ Handled by syllascrape

# Doc URLs
# http://www.ist.ucf.edu/grad/syllabi.html Broken
# https://physics.cos.ucf.edu/main/wp-content/uploads/2015/07/ast5765-Fall-2015-syllabus-1_Harrington.pdf Broken
# http://africana.cah.ucf.edu/courses/ type2
# http://american.cah.ucf.edu/courses/ type2 
# http://english.cah.ucf.edu/courses.php type1
# http://flstudies.cah.ucf.edu/courses/ type2
# http://history.cah.ucf.edu/courses.php
# http://judaicstudies.cah.ucf.edu/courses.php
# http://las.cah.ucf.edu/courses/
# http://middleeasternstudies.cah.ucf.edu/courses.php
# http://mll.cah.ucf.edu/courses.php
# http://music.cah.ucf.edu/courses.php
# http://philosophy.cah.ucf.edu/courses.php
# http://tandt.cah.ucf.edu/syllabi.php handled by syllascrape
# http://wgst.cah.ucf.edu/academics/courses/
# http://writingandrhetoric.cah.ucf.edu/courses.php
# https://biology.cos.ucf.edu/undergraduate-program/syllabus/ Handled by syllascrape
# https://biology.cos.ucf.edu/undergraduate-program/syllabus/2015-2016/ Handled by syllascrape
# https://biology.cos.ucf.edu/undergraduate-program/syllabus/2014-2015/ Handled by syllascrape
# https://biology.cos.ucf.edu/undergraduate-program/syllabus/2013-2014/ Handled by syllascrape
# http://www.creol.ucf.edu/Academics/Courses/ Handled by syllascrape
# http://theatre.cah.ucf.edu/staff.php?id=363 Included in previous URL
# http://www.cah.ucf.edu/common/files/syllabi/

# Mixed URLs:
# https://www.cohpa.ucf.edu/socialwork/syllabi-old/summer-2012/ Handled by syllascrape

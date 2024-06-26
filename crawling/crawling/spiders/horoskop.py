
import scrapy

from .. items import HoroskopItem
from app.models import Horoskop

from scrapy.spiders import CrawlSpider


class VodolijaSpider(scrapy.Spider):
    name = 'vodolija'

    allowed_domains = ["horoskopius.com"]
    start_urls = [
        "https://horoskopius.com/dnevni-horoskop/vodolija"
    ]


    def parse(self, response):

        item = HoroskopItem()
        item['znak'] = response.css('h2.sppb-addon-title::text').get().strip()
        item['dnevni'] = response.css('div.article-details p::text').get().strip()
        yield item


                # Dnevni horoskop
        # if "dnevni-horoskop" in response.url:
        #     yield {
        #         'dnevni': response.css('div.article-details p::text').get()
        #     # yield from self.parse_dnevni_horoskop(response)
        #     }

        # def parse_item(self, response):

        #     i = HoroskopItem()
        #     i['znak'] = response.css('h2.sppb-addon-title::text').get()
        #     i['dnevni'] = response.css('div.article-details p::text').get()

        #     return i


# class RottenTomatoesSpider(CrawlSpider):

#     name = 'rottentomatoes'
#     allowed_domains = ["horoskopius.com"]
#     start_urls = [
#         "https://horoskopius.com/dnevni-horoskop/vodolija"
#     ]


#     def parse(self, response):
#             # Dnevni horoskop
#         if "dnevni-horoskop" in response.url:
#             yield {
#                 'dnevni': response.css('div.article-details p::text').get()
#             }


    # def parse_item(self, response):

    #     i = HoroskopItem()
    #     i['znak'] = response.css('h2.sppb-addon-title::text').get()
    #     i['dnevni'] = response.css('div.article-details p::text').get()

    #     yield i


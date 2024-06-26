

import scrapy
from scrapy_djangoitem import DjangoItem

from app.models import Horoskop


# class CrawlingItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class HoroskopItem(DjangoItem):
    django_model = Horoskop



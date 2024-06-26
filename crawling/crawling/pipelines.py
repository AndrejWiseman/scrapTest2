# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from app.models import Horoskop


def clean_znak(param):
    return param.strip() if param else ""

def clean_dnevni(param):
    return param.strip() if param else ""

class CrawlingPipeline(object):
    def process_item(self, item, spider):
        znak = clean_znak(item.get('znak', ''))
        dnevni = clean_dnevni(item.get('dnevni', ''))

        if znak and dnevni:
            Horoskop.objects.create(
                znak=znak,
                dnevni=dnevni,
            )
        return item


# class CrawlingPipeline:
#     def process_item(self, item, spider):
#         return item
    
# def clean_znak(param):
#     return param

# def clean_dnevni(param):
#     return param


# class CrawlingPipeline(object):

#     def process_item(self, item, spider):
#         znak = clean_znak(item['znak'])
#         dnevni = clean_dnevni(item['dnevni'])


#         Horoskop.objects.create(
#             znak=znak,
#             dnevni=dnevni,
#         )
        
#         return item
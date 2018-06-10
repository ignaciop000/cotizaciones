# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class CotizacionesPipeline(object):

    def __init__(self):
	    self.file = codecs.open('data/dolar.json', 'a+', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, indent=4)
        self.file.seek(-2,2)           
        self.file.truncate()
        self.file.write(',')
        self.file.write("\n")
        self.file.write('    ')
        self.file.write(line)
        self.file.write("\n")
        self.file.write(']')
        return item

    def close_spider(self, spider):
        self.file.close()
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CotizacionesItem(scrapy.Item):
    dia = scrapy.Field()
    cotizacion_compra = scrapy.Field()
    cotizacion_venta = scrapy.Field()
    pass

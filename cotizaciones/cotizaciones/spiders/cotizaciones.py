import scrapy
import datetime
import json
from cotizaciones.items import CotizacionesItem
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.http import FormRequest
from scrapy.http import Request
from pprint import pprint

class cotizacionesSpider(scrapy.Spider):
    name = "cotizaciones"
    start_urls = ["https://www.lanacion.com.ar"]

    def parse (self,response):
	    with open ('data/dolar.json','r') as jsonFile:
		    data = json.load(jsonFile)
		    jsonFile.close()
	    number = len(data)
	    ultimoRegistroDia = data[number-1]['dia'][0]
	    ultimoRegistroCompra = data[number-1]['cotizacion_compra'][0]
	    ultimoRegistroVenta = data[number-1]['cotizacion_venta'][0]
	    now = datetime.datetime.now()
	    fecha = now.strftime("%d-%m-%y")
	    fechaArray = fecha.split(",")
	    agarraCompra = response.xpath(".//*[@id='dcompraHome']//text()").extract()
	    agarrarVenta = response.xpath(".//*[@id='dventaHome']//text()").extract()
	    compra =''.join(str(x) for x in agarraCompra).rstrip()
	    compra = compra[:-1]
	    compraSinComa = compra.replace(',','.')
	    venta = ''.join(str(x) for x in agarrarVenta).rstrip()
	    venta = venta[:-1]
	    ventaSinComa = venta.replace(',','.')

	    
	    if (ultimoRegistroDia==fecha):
		    with open('data/dolar.json','r+') as jsonFile:
			    data = json.load(jsonFile)

			    data[number-1]['cotizacion_compra'] = [compraSinComa]
			    data[number-1]['cotizacion_venta'] = [ventaSinComa]
		    
		    with open('data/dolar.json','w+') as jsonFile:
			    jsonFile.write(json.dumps(data, indent=4))
			    jsonFile.close()
	    else:
		    cotizacionitem = CotizacionesItem()
		    cotizacionitem ['dia'] = fechaArray
		    cotizacionitem ['cotizacion_compra'] = [compraSinComa]
		    cotizacionitem ['cotizacion_venta'] = [ventaSinComa]
		    yield cotizacionitem

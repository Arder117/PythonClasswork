# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ItcastItem(scrapy.Item):
   city_name = scrapy.Field()
   minimum_temperature = scrapy.Field()
   maximum_temperature = scrapy.Field()

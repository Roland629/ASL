import scrapy

class KallofemScraperItem(scrapy.Item):
    termeknev = scrapy.Field()
    ar = scrapy.Field()
    kep_url = scrapy.Field()

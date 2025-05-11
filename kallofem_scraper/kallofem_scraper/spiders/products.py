import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["kallofem.hu"]
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        for product in response.css('.termekdoboz'):
            yield {
                'termeknev': product.css('.termeknev::text').get().strip(),
                'ar': product.css('.ar .brutto::text').get().strip(),
                'kep_url': response.urljoin(product.css('img::attr(src)').get()),
            }

        next_page = response.css('.lapozo a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

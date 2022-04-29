import Scrapy as Scrapy
import scrapy

class ClothesScrapeSpider(scrapy.Spider):
    name = 'clothes_scrape'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/']
    def parse(self, response):
        articles = response.xpath("//article")
        for article in articles:
            yield {
                'title': article.xpath(".//h3/a/@title").get(),
                'image': response.urljoin(article.xpath(".//div[@class='image_container']/a/img/@src").get()),
                'price': article.xpath(".//h5[@class='price_color']/text()").get(),
                'description': article.xpath(".//h4/a/@title").get()
            }
            next_page = response.xpath("//li[@class='next']/a/@span").get()
            if next_page:
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)










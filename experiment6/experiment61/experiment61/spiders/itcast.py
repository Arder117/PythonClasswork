import scrapy
import scrapy
from ..items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["www.weather.com.cn"]
    start_urls = ["http://www.weather.com.cn/shandong/index.shtml"]

    def parse(self, response):
        strin=''
        for each in response.xpath("//*[@id='forecastID']/dl"):
            name = each.xpath("./dt/a/text()").extract()
            max = each.xpath("./dd/a/b/text()").extract()
            min = each.xpath("./dd/a/span/text()").extract()
            strin+=(str(name)+' '+str(min)+'~'+str(max)+'\n')
        with open('weather.txt', 'w', encoding='utf-8') as fp:
            fp.write(strin)
        pass
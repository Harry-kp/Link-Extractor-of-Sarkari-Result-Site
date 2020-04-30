from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from reaper.items import SarkariResult


class Spider1(Spider):
    name = "latestJobs"
    start_urls = [
                  'https://www.sarkariresult.com/latestjob.php',

                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                loader.add_value('Last_Date','NaN')
            yield loader.load_item()


class Spider2(Spider):
    name = "admission"
    start_urls = [
                   'https://www.sarkariresult.com/admission.php',
                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[0:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                pass
            yield loader.load_item()


class Spider3(Spider):
    name = "admitCard"
    start_urls = [
                   'https://www.sarkariresult.com/admitcard.php',

                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[0:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                pass
            yield loader.load_item()


class Spider4(Spider):
    name  ="answerKey"
    start_urls = [
                  'https://www.sarkariresult.com/answerkey.php',
                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[0:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                pass
            yield loader.load_item()


class Spider5(Spider):
    name = "result"
    start_urls = [
                    'https://www.sarkariresult.com/result.php',
                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                pass
            yield loader.load_item()


class Spider6(Spider):
    name = "syllabus"
    start_urls = [
                  'https://www.sarkariresult.com/syllabus.php',
                  ]

    def parse(self, response):

        for li in response.xpath('//div[@id ="post"]//li')[0:61]:
            loader = ItemLoader(item=SarkariResult(), selector=li, response = response)
            loader.add_xpath('Name', './/text()')
            loader.add_xpath('Link', './/a/attribute::href')
            try:
                text = li.xpath('.//text()').getall()[1]
                i = text.find(':')
                loader.add_value('Last_Date',text[i+2:i+12])
            except:
                pass
            yield loader.load_item()



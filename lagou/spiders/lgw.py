# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
#from lagou.items import LagouItem

class LgwSpider(scrapy.Spider):
    name = "lgw"
    allowed_domains = ["https://www.lagou.com/"]
    start_urls = (
      'https://www.lagou.com/zhaopin/Java/',
    )

    def parse(self, response):
        #1.爬取所以url连接
       #url =response.xpath('//div[@class="menu_box"]/div[@class="menu_main job_hopping"]/a/@href').extract()
       #for daurl in url:
          # print daurl
           #yield Request(url=daurl,callback=self.parse_dd,dont_filter = True)
   # def parse_dd(self,response):
        lianjie = response.xpath('//div[@class="list_item_top"]')
        for dizhi in lianjie:
            item = LagouItem()
            item["hangye"] =dizhi.xpath('./div[@class="position"]/div[@class="p_top"]/a/h2/text()').extract()
            item["xinzi"] =dizhi.xpath('./div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/text()').extract()
            item["jingyan"] =dizhi.xpath('./div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/span[@class="money"]/text()').extract()
            item["gongsi"] =dizhi.xpath('./div[@class="company"]/div[@class="company_name"]/a/text()').extract()
            yield item
        page = response.xpath('//div[@class="item_con_pager"]/div[@class="pager_container"]/a/@href').extract()[-1]
        if page!='javascript:;':
            yield Request(url=page,callback=self.parse_dd,dont_filter = True)








# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from scrapy.conf import settings


class MiddlewaretestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

#User-agent
class UAMiddleware(object):
    user_agent_list = settings['USER_AGENT_LIST']

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        request.headers['User-Agent'] = ua

#ip
class ProxyMiddleware(object):
    ip_list = settings['IP_LIST']

    def process_request(self, request, spider):
        ip = random.choice(self.ip_list)
        request.meta['proxy'] = ip

from selenium import webdriver
from scrapy.http import HtmlResponse
class JSPageMiddleware(object):

    #通过chrome 动态访问
    def process_request(self,request,spider):
        if spider.name =="qicha":
            spider. browser.get(request.url)
            import time
            time.sleep(3)
            print "访问：{0}".format(request.url)
            #spider.browser.find_element_by_xpath('//div[@class="bottom hide"]/a[@class="link"]').click()

            spider.browser.find_element_by_xpath('//div[@class="form-group has-feedback m-l-lg m-r-lg m-t-xs m-b-none"]/input[@name="nameNormal"]').send_keys("你自己的账号")
            spider.browser.find_element_by_xpath('//div[@class="form-group has-feedback m-l-lg m-r-lg m-t-xs m-b-none"]/input[@name="pwdNormal"]').send_keys("你自己的密码")
            time.sleep(9)
            #spider.browser.find_element_by_xpath('//div[@class="m-l-lg m-r-lg m-t-lg"]/button[@class="btn  btn-primary     m-t-n-xs btn-block btn-lg font-15"]').click()
            return HtmlResponse(url=spider.browser.current_url,body=spider.browser.page_source,encoding="utf-8")
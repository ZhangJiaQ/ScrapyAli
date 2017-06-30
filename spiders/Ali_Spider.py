# -*- coding: utf-8 -*-
import re
from urllib import parse
from scrapy.http import Request
from scrapy.loader import ItemLoader

from AliSpider.AliSpider.items import AliSpiderInfoItem
import scrapy


class AliSpiderSpider(scrapy.Spider):
    name = 'Ali_Spider'
    allowed_domains = ['https://m.1688.com/']
    start_urls = ['http://m.1688.com/offer_search/-BEC6.html']

    header = {
        'Host': 'm.1688.com',
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:54.0) Gecko/20100101 Firefox/54.0",
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Connection': 'keep-alive',
    }
    i = 2
    # 模拟请求下一页需要发送的数据
    data_content = {"spm": "a26g8.7662790.0.0.wtBMQr",
                    "type": "offer",
                    "keywords": "酒",
                    "beginPage": i,
                    "pageSize": '10',
                    "userAgent": "Mozilla/5.0+(X11;+Ubuntu;+Linux+i686;+rv:54.0)+Gecko/20100101+Firefox/54.0",
                    "offset": '1',
                    "boxSrc": ""}

    def parse(self, response):
        
        response_text = response.text
        #获取所有商品URL
        url_nodes = response.css('.wsw-sync-offerbox .wsw-offer a::attr(href)').extract()

        #print (len(url_nodes))
        #获取每个商品URL提交给goods_page_parse进行解析
        for i in range(0,len(url_nodes)):
            c = re.search(r'&ui=(.*)&ut', url_nodes[i])
            d = re.search(r'offer/(.*).html',url_nodes[i])
            if c:
                goods_url = 'https://m.1688.com/offer/{0}.html'.format(c.group(1))
                yield Request(url=goods_url,headers=self.header, callback=self.goods_page_parse)
            if d:
                goods_url = 'https://m.1688.com/offer/{0}.html'.format(d.group(1))
                yield Request(url=goods_url,headers=self.header, callback=self.goods_page_parse)
                
        #验证是否还有下一页,如果有的话提交翻页数据,并获取下一页的数据继续进行解析
        match_obj = re.match(r'.*<div class="wsw-sync-offerbox wsw-offers">.*', response_text, re.DOTALL)
        if match_obj:
            self.data_content["beginPage"]+=1
            yield scrapy.FormRequest(url=self.start_urls,headers=self.header, formdata=self.data_content)

    def goods_page_parse(self, response):
        #对商品详情页面进行解析,找出店铺联系方式页面,并跳转
        html_scripy = response.css('script::text').extract()
        #"memberId":"b2b-1695311802"
        for i in range(0,len(html_scripy)):
            company_match = re.search(r'.*memberId":"(.*?)".*',html_scripy[i])
            if company_match:
                company_s_url = company_match.group(1)
                company_url = 'https://m.1688.com/winport/{0}.html'.format(company_s_url)
                yield Request(company_url,headers= self.header, callback=self.contact_page_parse)

    
    def contact_page_parse(self,response):
        #对店铺联系方式页面进行解析,并提交给ItemLoader
        # phone_num = response.css('.phone::text').extract()[0]
        # company_information = response.css('.info-container span::text').extract()
        item_loader = ItemLoader(item=AliSpiderInfoItem(), response=response)
        item_loader.add_css("company_name", ".info-container span::text")
        item_loader.add_css("phone_num", ".phone::text")
        item_loader.add_css("address", ".info-container span::text")
        item_loader.add_value("company_url", response.url)

'''
['13602416403', '020-38342466']
'''


'''
['广州南傲贸易有限公司', '招商代理', '广东 广州市天河区', '全国酒类批发、进口葡萄酒批发、全国招商代理、进口红酒批发', 
'47条', '5', '王汉弟', '广东广州市天河区思成路35号03栋B座6层', '总人数52人，\n                  \n                  办公面积428m',
 '\n                  \t\n                  \t线上平台3家\n                  \t', '\n                  \t\n                  \
 t\n                  \t\t\n                  ', '\n                  \t\n                  \t自有品牌(\n\t\t\t\t  \t\n\t\t\t\
 t  \t\tAOYO、\n\t\t\t\t  \t\n\t\t\t\t  \t\t傲鱼、\n\t\t\t\t  \t\n\t\t\t\t  \t\t傲鱼aoyo、\n\t\t\t\t  \t\n\t\t\t\t  \t\t南傲nan
 ao\n\t\t\t\t  \t)', '\n\t\t\t\t  \t\n\t\t\t\t  \t\n\t\t\t\t  ', '\n                  自营进出口\n                  \n         
          \n                  \n                  ，采购地区：智利\n                  \n                  ', '广州南傲贸易有限公司'
          , '中国广东广州天河区新塘街沐陂西街21号大院B303房', '2011年05月13日', '电子产品批发;电子产品零售;汽车零配件零售;工艺品批发;汽车零
          配件批发;工艺美术品零售;计算机零售;服装批发;计算机批发;服装零售;技术进出口;货物进出口（专营专控商品除外）;预包装食品零售;酒类零售;预包
          装食品批发;酒类批发;(依法须经批准的项目，经相关部门批准后方可开展经营活动)〓', '440106000427271', '王汉弟', '有限责任公司(自然人
          投资或控股)', '2011-05-13 至 长期', '广州市天河区工商行政管理局']
'''

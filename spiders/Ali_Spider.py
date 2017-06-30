# -*- coding: utf-8 -*-
import re
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
        url_nodes = response.css('.wsw-sync-offerbox .wsw-offer a::attr(href)').extract()
        match_obj = re.match(r'.*<div class="wsw-sync-offerbox wsw-offers">.*', response_text, re.DOTALL)
        for i in range(0,len(match_obj)):
            if match_obj[i].startwith('//'):
                pass
            else:
                yield scrapy.Request(url=url_nodes[i],headers= self.header,callback= self.goods_page_parse)


    def goods_page_parse(self,response):

        html_scripy = response.css('script::text').extract()
        #"memberId":"b2b-1695311802"
        for i in range(0,len(html_scripy)):
            re.compile(r'.*memberId":"(.*)".*')



    def contact_page_parse(self,response):
        pass


            # yield scrapy.Request(captcha_url, headers=self.header, meta={"post_data": post_data},
#                      callback=self.login_after_captcha)
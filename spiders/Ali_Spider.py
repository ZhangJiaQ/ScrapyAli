# -*- coding: utf-8 -*-
import scrapy


class AliSpiderSpider(scrapy.Spider):
    name = 'Ali_Spider'
    allowed_domains = ['https://www.1688.com/']
    start_urls = ['http://https://www.1688.com//']

    def __init__(self):
        login_url = "https://login.taobao.com/member/login.jhtml"


        post = {
        'TPL_username':"3382315515@qq.com",
        'TPL_password':"",
        'ncoSig':"",
        'ncoSessionid':"",
        'ncoToken':"5c9fef9151a9e242cc67dfaa2e7be080343572d1",
        'slideCodeShow':"false",
        'useMobile':"false",
        'lang':'zh_CN',
        'loginsite':"0",
        'newlogin':"0",
        'TPL_redirect_url':"https://i.taobao.com/my_taobao.htm?spm=a21bo.50862.1997525045.1.zjLxRC&nekot=anVkZ2V6aGFuZzEyMzEy1498712372655",
        'from':"tb",
        'fc':"default",
        'style':"default",
        'css_style':"",
        'keyLogin':"false",
        'qrLogin':"true",
        'newMini':"false",
        'newMini2':"false",
        'tid':"",
        'loginType':"3",
        'minititle':"",
        'minipara':"",
        'pstrong':"",
        'sign':"",
        'need_sign':"",
        'isIgnore':"",
        'full_redirect':"",
        'sub_jump':"",
        'popid':"",
        'callback':"",
        'guf':"",
        'not_duplite_str':"",
        'need_user_id':""
        'poy':"",
        'gvfdcname':"10",
        'gvfdcre':"68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D61317A30322E312E3735343839343433372E372E4F467232464B26663D746F70266F75743D7472756526726564697265637455524C3D6874747073253341253246253246692E74616F62616F2E636F6D2532466D795F74616F62616F2E68746D25334673706D253344613231626F2E35303836322E313939373532353034352E312E7A6A4C7852432532366E656B6F74253344616E566B5A325636614746755A7A45794D7A457931343938373132333732363535",
        'from_encoding':""
        'sub':""
        'TPL_password_2':"645866a455bd96801ebefcb34bab0…53ec2f0517b9a493027753467ef9"
        loginASR
        "1"
        loginASRSuc
        "1"
        allp
        ""
        oslanguage
        "en-US"
        sr
        "1920*1080"
        osVer
        ""
        naviVer
        "firefox|54"
        osACN
        "Mozilla"
        osAV
        "5.0+(X11)"
        osPF
        "Linux+i686"
        miserHardInfo
        ""
        appkey
        ""
        nickLoginLink
        ""
        mobileLoginLink
        "https://login.taobao.com/memb…1498712372655&useMobile=true"
        showAssistantLink
        ""
        ua
        "095#6ULoTEoJRYoocERZoooooPLeI…O+apJxU+Zb/oEPjY/SWFTPuRNVY="
        um_token
        "HV01PAAZ0b8706ce3ad59c8259548c0d0000d242"
        }





    def parse(self, response):
        pass

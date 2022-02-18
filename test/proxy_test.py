#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : proxy_test.py
# @Description:
# @Time       : 2022-2-18 上午 11:05
# @Author     : Hou

import urllib, urllib3, sys
from urllib import request
import ssl


host = 'https://so.gushiwen.cn/'
path = '/mingjus/'
method = 'GET'
appcode = 'e5942dc2eedb4f0da8c7f98206ed966a'
querys = 'targetUrl=http%253A%252F%252F43.226.153.108%252Fcomposite%252Fmytest'
bodys = {}
url = host + path + '?' + querys

req = request.Request(url)
req.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = request.urlopen(req, context=ctx)
content = response.read()
if (content):
    print(content)
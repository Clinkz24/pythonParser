# -*- coding: utf-8 -*-
import string
import stringprep
import httplib2
import json
import sys

bsams = 0
while(1):
    print("输入查询单词")
    queryword = input()
    if queryword == '@sams@':
        if bsams == 1:
            bsams = 0
        elif bsams == 0:
            bsams = 1
        else:
            bsams = 0
        continue
    url = "http://xtk.azurewebsites.net/BingDictService.aspx?Word="
    url+=queryword
    h = httplib2.Http()
    resp, content = h.request(url)
    result_obj = json.loads(content.decode('utf-8'))
    source_word=result_obj["word"]
    defs=[]
    defs = result_obj["defs"]
    samples=result_obj["sams"]
    print("原词:", source_word)
    print("释义:")
    for single_defs in defs:
        print("(属性:", single_defs["pos"], ")含义:", single_defs["def"])
    if bsams:
        print("例句:")
        for single_sams in samples:
           print("英:", single_sams["eng"])
           print("汉:", single_sams["chn"])
    print("结束")




class get_ip:
    def get_ip():
        url = "https://ipip.yy.com/get_ip_info.php"
        h = httplib2.Http()
        resp, content = h.request(url)
        source_str = content.decode('utf-8')
        pos = source_str.find('=')
        pos2 = source_str.find(';')
        json_str = source_str[pos + 2 : pos2]
        result_obj = json.loads(json_str)
        ip = result_obj["cip"]
        return ip
print("本地IP:", get_ip.get_ip())





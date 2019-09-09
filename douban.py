#爬取豆瓣电影网的排名
# coding=utf-8
import urllib.request
import re
import os
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400"

}
## https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1
url=("https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=80")
req = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(req).read().decode()
# "title":"肖申克的救赎"   "rating":["9.7","50"]
tad1 = r'"rating":\["(.*?)","\d+"\]'
tad2 = '"title":"(.*?)"'
defen = re.compile(tad1, re.I)
name = re.compile(tad2, re.I)
data1 = defen.findall(data)
data2 = name.findall(data)
for i in range(len(data2)):
    print("排名：", i+1, "电影名：",data2[i],"豆瓣评分：", data1[i])

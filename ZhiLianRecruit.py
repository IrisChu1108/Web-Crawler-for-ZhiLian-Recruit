# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
#用来创建excel文档并写入数据
import xlwt




#获取网页的源码
def get_content():
    #网址
    url = 'https://xiaoyuan.zhaopin.com/full/538/0_0_160000_1_0_0_0_1_0'
    #打开网址
    a = urllib.request.urlopen(url)
    #读取源代码并转为unicode
    html = a.read().decode('utf-8')
    return html

#正则匹配要爬取的内容
def get(html):
    #正则匹配式
    reg = re.compile(r'class="searchResultJobName">.*?<a joburl href="//(.*?)" class="fl __ga__fullResultcampuspostname_clicksfullresultcampuspostnames_001">(.*?)</a>.*?<p class="searchResultCompanyname"><span>(.*?)</span>.*?<span>发布时间：<em>(.*?)</em></span>.*?职责描述：<span>(.*?)</span>',re.S)
    #进行匹配
    items = re.findall(reg,html)
    #print(items)
    #计算匹配到的数目（一整条记录算一个）
    items_length = len(items) 
    return items,items_length

#爬取到的内容写入excel表格
def excel_write(items,index):
    #将职位信息写入excel,item为tuple元组
    for item in items:
        #共五个信息，写五列
        for i in range(0,5):
            #print item[i]
            #.write（行，列，数据）
            ws.write(index,i,item[i])
        #每成功写入一条就输出对应的行编号
        print(index)
        #index+1，写下一行
        index+=1

#excel名称
newTable="智联招聘岗位爬虫结果.xls"
#创建excel文件，声明编码为utf-8
wb = xlwt.Workbook(encoding='utf-8')
#创建表格
ws = wb.add_sheet('sheet1')
#表头信息
headData = ['url','职位','公司','发布时间','职责描述']
#写入表头信息
for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))

#从第2行开始写入
index = 1
#爬取信息
items,items_length = get(get_content())
#写入excel
excel_write(items,index)
#保存excel
wb.save(newTable)
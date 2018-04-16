#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import urllib,http.cookiejar,gzip,re
from io import BytesIO



cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def main():
	#for i in range(1, len(sys.argv)):
    	id=sys.argv[1]
    	fund=work(id)
    	print('卡号为%s的余额为%s元' %(id,fund))

def work(id):
	get(url(0),header(0))
	po(url(1),{},header(1))
	content=po(url(2),postdata(id),header(2))
	str=re.findall('value=\"(\d+\.\d{2}).*元',content,re.S)
	#str=re.findall('玉林高级中学.*缴费金额.*\"(\d+\.\d{2}).*元',content)
	return str
	

def get(url,header):
	req=urllib.request.Request(url,headers=header)
	r = opener.open(req)
	buff = BytesIO(r.read()) # 把content转为文件对象
	f = gzip.GzipFile(fileobj=buff)
	return f.read().decode('utf-8')

def po(url,postdata,header):
	req = urllib.request.Request(url,postdata,header)
	r = opener.open(req)
	buff = BytesIO(r.read()) # 把content转为文件对象
	f = gzip.GzipFile(fileobj=buff)
	return f.read().decode('utf-8')

def postdata(cardID):
	return urllib.parse.urlencode({	
'MERCHANT':'05013|玉林高级中学一卡通|7614|0|请输入学号，核对姓名、缴费金额后缴费。|学号||0|||0||450000000|||||1011111111|100019|11|||玉林市|450900',
'COMM':cardID,
'RE1CON':'',
'RE2CON':'',
'BANK_COD':'450000',
'OPUN_COD':'450900',
'BUTTON_IMG':'',
'BUTTON_URL':'',
'SEQUENCE_NAME':'',
'REMARK1':'',
'REMARK2':'',
'PAGE1':'',
'PAGE2':'',
'TYPE1':'0',
'DETAIL_FLAG':'1011111111',
'TYPE2':'0',
'BILL_NAME':'学号',
'BILL_COMM':'请输入学号，核对姓名、缴费金额后缴费。',
'BILL_FLAG':'0',
'TXCODE':'NMJ002',
'BILL_ITEM':'05013',
'OPUN_NAME':'玉林市',
'BANK_NAME':'广西区',
'BIll_MERCHANT':'7614',
'MERCHANT_NAME':'玉林高级中学一卡通',
'AMT_FLAG':'1',
'CUST_FALG':'',
'BIll_CODE':'100019',
'BILL_TYPE':'500',
'BRAN_NO':'450000000',
'PAY_TYPE':'11',
'CTPPARAM':'',
'BEGIN_TIME':'',
'END_TIME':'',
'HOLIDAY_BEGIN_TIME':'',
'HOLIDAY_END_TIME':'',
'VIEW_FLAG':'9',
'history_0':'',
'history_1':'',
'history_2':'',
'history_3':'',
'history_4':'',
'history_5':'',
'history_6':'',
'history_7':'',
'history_8':'',
'history_9':''
}).encode('utf-8')

def url(index):
	url=('http://life.ccb.com/cn/paymentv3/mobile/item_detail/201509260725204147.html?selectedCity=%E7%8E%89%E6%9E%97%E5%B8%82,450900,%E5%B9%BF%E8%A5%BF%E5%8C%BA,450000','http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&TXCODE=NMJ10Z&DCRINDEX=201509260725204147&BILL_TYPE=500&BILL_ITEM=05013&selectedCity=%E7%8E%89%E6%9E%97%E5%B8%82,450900,%E5%B9%BF%E8%A5%BF%E5%8C%BA,450000','http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5')
	return url[index]

def header(index):
	header = ({
'Host':'life.ccb.com',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0(Linux;Android6.0.1;HUAWEIRIO-AL00Build/HuaweiRIO-AL00)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.109MobileSafari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9'},{
'Host':'life.ccb.com',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0(Linux;Android6.0.1;HUAWEIRIO-AL00Build/HuaweiRIO-AL00)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.109MobileSafari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Referer':' http://life.ccb.com/cn/paymentv3/mobile/item_detail/201509260725204147.html?selectedCity=%E7%8E%89%E6%9E%97%E5%B8%82,450900,%E5%B9%BF%E8%A5%BF%E5%8C%BA,450000'},{
'Host':'life.ccb.com',
'Connection':'keep-alive',
'Content-Length':'1309',
'Cache-Control':'max-age=0',
'Origin':'http://life.ccb.com',
'Upgrade-Insecure-Requests':'1',
'Content-Type':'application/x-www-form-urlencoded',
'User-Agent':'Mozilla/5.0(Linux;Android6.0.1;HUAWEIRIO-AL00Build/HuaweiRIO-AL00)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.109MobileSafari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer':'http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9'
})
	return header[index]


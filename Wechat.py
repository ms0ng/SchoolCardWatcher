#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import itchat

bot=itchat.new_instance()

class Wechat(object):
	
	def send_debug(s,text):
		bot.send(text, toUserName='filehelper')
	
	def send(s,text,account):
		s.hold_text=text
		#获取微信号为account的账号
		fri = bot.search_friends(wechatAccount=account)
		#获取备注，昵称，微信号中任意一个匹配account的账号,优先匹配查找到的第一个
		#删除#fri的警号 # 就可以了
		#fri = bot.search_friends(name=account)[0]
		fri.send(text)
		
	def keep_login(s):
		bot.check_login()
	
	def lc():
		print('log in successfully!')
	
	def qrcb(uuid, status, qrcode):
		f=open('./QR.PNG','wb')
		f.write(qrcode)
		f.close()
	
	def logout(s):
		bot.logout()
	
	@bot.msg_register(itchat.content.TEXT)
	def reply(msg):
		if msg.text == '刷新':
			return s.hold_text
			
	def __init__(s,user,login):
		if login==0:
			bot.auto_login(enableCmdQR=True,qrCallback=Wechat.qrcb,hotReload=True,loginCallback=Wechat.lc,statusStorageDir=user+'.pkl')
		else:
			bot.auto_login(enableCmdQR=login,hotReload=True,loginCallback=Wechat.lc,statusStorageDir=user+'.pkl')
		

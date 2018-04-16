#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import Wechat,Watcher,time,sys

card=sys.argv[1]
sendto=sys.argv[2]
logintype=sys.argv[3] #0 or another number
user=sys.argv[4]

def main():
	bot=Wechat.Wechat(user,logintype)
	mny=Watcher.work(card)
	if float(mny)<50.0:
		bot.send('[自动监控]校园卡卡号%s的余额为%s元，请及时充值' %(card,mny),sendto)

main()
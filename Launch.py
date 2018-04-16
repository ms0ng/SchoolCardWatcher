#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import Wechat,Watcher,sys

#card=sys.argv[1]
#sendto=sys.argv[2]
#logintype=sys.argv[3] #0 or another number
#user=sys.argv[4]

def main():
	bot=Wechat.Wechat(user,logintype)
	mny=Watcher.work(card)
	if float(mny)<50.0:
		bot.send('[自动监控]校园卡卡号%s的余额为%s元，请及时充值' %(card,mny),sendto)

def main_test():
	user='x'
	card=''
	logintype=0
	bot=Wechat.Wechat(user,logintype)
	mny=Watcher.work(card)
	print('%s的余额%s' %(card,mny))
	bot.send_debug('[自动监控]校园卡卡号为%s的余额剩余%s元，请及时充值' %(card,mny))

main_test()
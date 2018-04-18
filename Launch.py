#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import Wechat,Watcher,time
from configparser import Configparser



def main():
	cfg=Configparser()
	cfg.read('Config.cfg',encoding='utf-8')
	card=str(cfg.get('global','card'))
	sendto=str(cfg.get('global','sendto'))
	logintype=cfg.getint('global','logintype')
	user=str(cfg.get('global','user'))
	min_balance=cfg.get('global','min_Balance')
	
	bot=Wechat.Wechat(user,logintype)
	last_time=time.time()
	while(True):
		bot.keep_login()
		if (time.time()-last_time)<(60*60*24) :
			time.sleep(60*5)
			continue
		mny=Watcher.work(card)
		if float(mny)<min_balance:
			bot.send('[自动监控]校园卡卡号%s的余额为%s元，请及时充值' %(card,mny),sendto)
		last_time=time.time()

def main_test(): #已经没什么卵用的测试函数
	user='x'
	card=''
	logintype=0
	bot=Wechat.Wechat(user,logintype)
	mny=Watcher.work(card)
	print('%s的余额%s' %(card,mny))
	bot.send_debug('[自动监控]校园卡卡号为%s的余额剩余%s元，请及时充值' %(card,mny))

main()

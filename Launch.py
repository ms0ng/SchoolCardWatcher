#-*- coding: utf-8 -*-

#encoding=utf-8

#coding:utf-8
import Wechat,Watcher,time,sys
from configparser import ConfigParser



def main():
	cfg=ConfigParser()
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

def main_test(): 
	if len(sys.argv)>1 :
		card=str(sys.argv[1])
		mny=Watcher.work(card)
		print('卡号%s的余额为%s元' %(card,mny))
		exit()

main_test()
main()

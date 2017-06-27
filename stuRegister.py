# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''

@author: Administrator
'''
#import MySQLdb
import urllib2
import json
import sys
import time

#TEST_HOST_SHARK = 'pk.shark.unlun.vip';
#ONLINE_HOST_SHARK = 'stuapi.knowbox.cn';
TEST_HOST_SHARK = 'qa.knowbox.cn:8001';

TEST_HOST_SERVERNEW = 'betassapinew.knowbox.cn:9001';
#ONLINE_HOST_SERVERNEW = 'ssapinew.knowbox.cn';

def postRegister(mobile, password, username):
	uri = '/user/auth/register-create';
	url = 'https://'+TEST_HOST_SHARK+uri;
	nowtime = time.localtime()
	verifyCode = nowtime.tm_mon * nowtime.tm_mday + 1024
	
	postParam = {
		"source":"androidRCStudent",
		"version":309,
		"channel":"Knowbox",
		"deviceId":"866947027337893",
		"deviceVersion":"5.0.2",
		"deviceType":"PLK-UL00",
		"token":"",
		"transaction":"register",
		"username":username,
		"mobile":mobile,
		"password":password,
		"code":verifyCode
	};
	requestUrl = urllib2.Request(url)
	header_contentType = ('Content-Type','application/json')  
	openUrl = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	openUrl.addheaders.append(header_contentType)
	response = openUrl.open(requestUrl,json.dumps(postParam))
	resultData = json.load(response)
	print(resultData['code'])
	if 'token' in resultData :
		return resultData
	elif resultData['code'] == 20000:
		print('Parameters error.')
		sys.exit(0)
	elif resultData['code'] == 20002:
		print(mobile + ' has already registered.')
		sys.exit(0)
	else:
		print('Register failed!');
		return None

if __name__=='__main__':
	studentToRegister= [str(mobile) for mobile in range(15900000020,15900000060)];
	for student in studentToRegister:
		studentInfo = postRegister(student,'aaaassss', student[7:]);
		if studentInfo is not None and studentInfo['code'] == 99999:
			print('Registered Succeed. Student info :\n');
			print(json.dumps(studentInfo));
'''	student = '15900000022'
	studentInfo = postRegister(student,'aaaassss', 'ABC');
	if studentInfo is not None and studentInfo['code'] == 99999:
		print('Registered Succeed. Student info :\n');
		print(json.dumps(studentInfo));
'''
# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''

@author: Administrator
'''
#import MySQLdb
import urllib2
import json
import sys

#TEST_HOST_SHARK = 'pk.shark.unlun.vip';
TEST_HOST_SHARK = 'stuapi.knowbox.cn';
#TEST_HOST_SHARK = 'qa.knowbox.cn:8001';

#TEST_HOST_SERVERNEW = 'betassapinew.knowbox.cn:9001';
TEST_HOST_SERVERNEW = 'ssapinew.knowbox.cn';

def postLogin(loginName,password):
    uri = '/user/auth/login';
    url = 'http://'+TEST_HOST_SHARK+uri;
    postParam = {"password":password,
                 "version":"2.8.1",
                 "source":"iPhoneRCStudent",
                 "loginName":loginName,
                 "transaction":"login"};
    
        
    requestUrl = urllib2.Request(url)
    #requestData = urlencode(postParam)
    header_contentType = ('Content-Type','application/json')  
    openUrl = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    openUrl.addheaders.append(header_contentType)
    response = openUrl.open(requestUrl,json.dumps(postParam))
    resultData = json.load(response)
    
    if 'token' in resultData and 'studentID':
        return {'token':resultData['token'],
                'data':resultData['studentID']}
    else:
        print('Login failed!');
        return None


'''
Required params:
    joinData = {
        classcode:string,
        token:string,
        transaction=joinClass}
'''
def postJoinClass(joinData):
    uri = '/kclass/class/join';
    url = 'http://'+TEST_HOST_SHARK+uri;
    postParam = {"classcode":joinData['classcode'],
                 "token":joinData['token'],
                 "transaction":"joinClass"};
    
        
    requestUrl = urllib2.Request(url)
    #requestData = urlencode(postParam)
    header_contentType = ('Content-Type','application/json')  
    openUrl = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    openUrl.addheaders.append(header_contentType)
    response = openUrl.open(requestUrl,json.dumps(postParam))
    resultData = json.load(response)
    return resultData



if __name__=='__main__':
    
    studentToJoin = [str(mobile) for mobile in range(15900000001,15900000005)];
    for student in studentToJoin:
        studentInfo = postLogin(student,'aaaassss');
        if studentInfo is not None:
            classCode = sys.argv[1];
            joinData = {"classcode":classCode,
                         "token":studentInfo['token'],
                         "transaction":"joinClass"};
            joinResult = postJoinClass(joinData)
            print student;
    
    
    

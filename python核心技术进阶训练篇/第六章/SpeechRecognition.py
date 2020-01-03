#coding:utf-8
import urllib.parse
import urllib.request
import json

#录音
##from record import Record
##record = Record(channels=1)
audioData = r'e:\Downloads\16k.wav'
speech_data = open(audioData,'rb')

#获取token
API_KEY = 'vW8uMI2OzqebGLBMvK7TfSNs'
SECRET_KEY = 'V6YFqN6w6T3CyrlMsjkl8IkYbaKgBGRS'
authUrl = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
response = urllib.request.urlopen(authUrl)
res = json.loads(response.read())
token = res["access_token"]

#语音识别
cuid = '123456qweasd'
srvUrl = "http://vop.baidu.com/server_api" + "?cuid=" + cuid + "&token=" + token
httpHeader = {
    'Content-Type':'audio/wav;rate=16000',
    }

req = urllib.request.Request(srvUrl,speech_data,headers=httpHeader)
response = urllib.request.urlopen(req)
res = json.loads(response.read())
text = res["result"][0]

print('\n识别结果：' + text)

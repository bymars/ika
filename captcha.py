import urllib.request
import hashlib
from datetime import *
import json

class Captcha(object):
    def http_request(self, url, paramDict):
        post_content = ''
        for key in paramDict:
            post_content = post_content + '%s=%s&'%(key,paramDict[key])
        post_content = post_content[0:-1]
        post_content = urllib.parse.urlencode(paramDict).encode(encoding='UTF8')
        #print post_content
        req = urllib.request.Request(url, data=post_content)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        #proxy_handler = urllib.request.ProxyHandler({'http': 'child-prc.intel.com:913'})
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())  
        response = opener.open(req, post_content)
        return response.read()

    def http_upload_image(self, url, paramKeys, paramDict, filebytes):
        timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        boundary = '------------' + hashlib.md5(timestr.encode('utf8')).hexdigest().lower()
        boundarystr = '\r\n--%s\r\n'%(boundary)
        
        bs = b''
        for key in paramKeys:
            bs = bs + boundarystr.encode('ascii')
            param = "Content-Disposition: form-data; name=\"%s\"\r\n\r\n%s"%(key, paramDict[key])
            #print param
            bs = bs + param.encode('utf8')
        bs = bs + boundarystr.encode('ascii')
        
        header = 'Content-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/gif\r\n\r\n'%('sample')
        bs = bs + header.encode('utf8')
        
        bs = bs + filebytes
        tailer = '\r\n--%s--\r\n'%(boundary)
        bs = bs + tailer.encode('ascii')
        
        import requests
        headers = {'Content-Type':'multipart/form-data; boundary=%s'%boundary,
                   'Connection':'Keep-Alive',
                   'Expect':'100-continue',
                   }
                   
        proxies = {
                   'http': 'http://child-prc.intel.com:913'
        }
        #response = requests.post(url, params='', data=bs, headers=headers, proxies=proxies)
        response = requests.post(url, params='', data=bs, headers=headers)
        return response.text
        
    def recognize(self, image_bytes):
        paramDict = {}
        result = ''
        paramDict['username'] = 'bymars1025'
        paramDict['password'] = 'zhy1016.'
        paramDict['typeid'] = 2000
        paramDict['timeout'] = 120
        paramDict['softid'] = 43048
        paramDict['softkey'] = '9638071b71f241e982985db704f37a95'
        paramKeys = ['username',
             'password',
             'typeid',
             'timeout',
             'softid',
             'softkey'
            ]
        result = self.http_upload_image("http://api.ruokuai.com/create.json", paramKeys, paramDict, image_bytes)
        json_obj = json.loads(result)
        return json_obj
        
    def reporterror(self, id):
        paramDict = {}
        result = ''
        paramDict['username'] = 'bymars1025'
        paramDict['password'] = 'zhy1016.'
        paramDict['softid'] = 43048
        paramDict['softkey'] = '9638071b71f241e982985db704f37a95'
        paramDict['id'] = id
        result = self.http_request('http://api.ruokuai.com/reporterror.json', paramDict)
        print(result)
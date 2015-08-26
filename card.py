#! /usr/bin/env python
import time
import urllib.request
import http.cookiejar
import json
import threading
from captcha import Captcha

lock = threading.RLock()

class Card(threading.Thread):
    def __init__(self, card_id, user_list, callback, i):
        threading.Thread.__init__(self)
        
        self.url_get = 'http://hao.17173.com/gift-captcha.html?refresh=1&gift_id=%d&_=%d'
        self.url_img = 'http://hao.17173.com%s'
        self.url_submit = 'http://hao.17173.com/gift-qiang-%d.html'
        self.card_id = card_id
        self.user_list = user_list
        self.callback = callback
        
        self.captcha = Captcha()
        self.i = i

        webCookie = http.cookiejar.CookieJar()
        cookie_handler = urllib.request.HTTPCookieProcessor(webCookie)
        self.openner = urllib.request.build_opener(cookie_handler)
        #proxy_handler = urllib.request.ProxyHandler({'http': 'child-prc.intel.com:913'})
        #self.openner = urllib.request.build_opener(cookie_handler, proxy_handler)

        self.thread_stop = False 

    def run(self):
        for index, user in enumerate(self.user_list):
            lock.acquire()
            if user['state'] > 0:
                lock.release()
                continue
            else:
                user['state'] = 1
                lock.release()
            user['state'] = 1
            self.callback(index)
            self.login(user['username'], user['password'])
            user['state'] = 2
            self.callback(index)
            retry = 0
            while not user['card_no'] and retry < 3:
                img_url = self.get_captches()
                result = self.identify_captchas(img_url)
                user['card_no'] = self.submit_captchas(result)
                retry += 1
            user['state'] = 3
            self.callback(index)
        
    def stop(self):
        self.thread_stop = True
        
    def login(self, username, password):
        print('\tlogin: %s ---- %s' % (username, password))

    def get_captches(self):
        time_stamp = int(time.time())
        response = self.openner.open(self.url_get % (self.card_id, time_stamp))
        data = response.read().decode()
        json_obj = json.loads(data)
        img_url = 'http://hao.17173.com' + json_obj["url"]
        print("\tget_captchas: img: %s" % img_url)
        return img_url
        
    def identify_captchas(self, img_url):
        response = self.openner.open(img_url)
        image_bytes = response.read()
        result = self.captcha.recognize(image_bytes)
        return result
    
    def submit_captchas(self, captcha):
        values = {'verifyCode':captcha['Result']}
        url_values=urllib.parse.urlencode(values).encode(encoding='UTF8')
        response = self.openner.open(self.url_submit % (self.card_id), url_values)
        data = response.read().decode()
        json_obj = json.loads(data)
        if int(json_obj['flag']) == 1:
            return json_obj['cardInfo']['card_number']
        else:
            self.captcha.reporterror(captcha['Id'])
            return ''

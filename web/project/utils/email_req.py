#!/usr/bin/env python
# encoding: utf-8
import requests
__author__ = 'younglee'

class PlainEmail:
    def __init__(self):
        self.verify_url = 'http://younglee.sinaapp.com/email/plain'

    def sendPlainEmail(self, destination, title, content):
        data = {'destination': destination, 'title': title, 'content': content}
        req = requests.post(self.verify_url, data = data)
        if req.status_code == 200:
            resp = req.json()
            return resp.get('status', 500)
        else:
            return 500

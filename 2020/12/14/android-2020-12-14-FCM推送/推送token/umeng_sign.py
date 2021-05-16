# -*- coding=utf-8 -*-

import hashlib
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def md5(s):
    m = hashlib.md5(s)
    return m.hexdigest()


appkey = '6006cef6f1eb4f3f9b66f9ef'
app_master_secret = 'sjgds8ymgye0kqeabpfbpnxkoax4amlb'
timestamp = '1611131716846'
method = 'POST'
url = 'http://msg.umeng.com/api/send'
params = {
    "appkey": "6006cef6f1eb4f3f9b66f9ef",
    "timestamp": "1611132496855",
    "type": "customizedcast",
    "alias": "ay1530603084806fwthz",
    "alias_type": "TUYA_SMART",
    "payload":
        {
            "display_type": "message",
            "body":
                {
                    "custom": "ttttttttt555555"
                }
        },
    "description": "alias-Android"
}
post_body = json.dumps(params)
print post_body
sign = md5('%s%s%s%s' % (method, url, post_body, app_master_secret))
print sign

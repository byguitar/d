# encoding: utf-8

import os
import requests
import json

# 文档：https://developer.github.com/v3/repos/#create
def create_repo(access_token, name, org=None):
    # if org:
    #     cmd = 'http POST https://api.github.com/user/orgs/%s/repos?access_token=%s name=%s' % (org, access_token, name)    
    # else:
    #     cmd = 'http POST https://api.github.com/user/repos?access_token=%s name=%s' % (access_token, name)
    # data = json.loads(os.popen(cmd).read())

    payload = json.dumps(
        {'name': name}
    )

    if org:
        url = 'https://api.github.com/orgs/%s/repos?access_token=%s' % (org, access_token)
    else:
        url = 'https://api.github.com/user/repos?access_token=%s&name=lll' % (access_token)

    try:
        r = requests.post(url, data = payload)
        print(r.status_code)
        if r.status_code >= 200 and r.status_code < 300:
            return r.json()
        raise Exception(r.text)
    except Exception as err:
        raise Exception(err)
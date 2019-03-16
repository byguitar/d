# encoding: utf-8

import os
import github.github_helper as _github_helper

access_token = 'd35b701be8a3efa6035ad608545c24a8b6e66c23'

def clone():
    # clone
    os.system('git clone --bare https://github.com/QiuZhiFei/dddd.git')

    # create repo
    os.system('http POST https://api.github.com/user/repos?access_token=d35b701be8a3efa6035ad608545c24a8b6e66c23 name=d')

    # path
    os.system('cd dddd.git')

    # add repo
    os.system('git remote add new https://github.com/QiuZhiFei/d.git')

    # push
    os.system('git push new --mirror')

    #wiki
    os.system('git clone --bare https://github.com/QiuZhiFei/dddd.wiki.git')


def migrate(url, org=None):
    name = url.split('/')[-1].split('.')[0]

    # clone
    os.system('git clone --bare %s' % url)

    # create repo
    if org:
        os.system('http POST https://api.github.com/user/repos?access_token=d35b701be8a3efa6035ad608545c24a8b6e66c23 name=d')
    else:
        os.system('http POST https://api.github.com/user/orgs/%s/repos?access_token=d35b701be8a3efa6035ad608545c24a8b6e66c23 name=d')


# clone()
# url = 'https://github.com/QiuZhiFei/dddd.git'
# migrate(url)


# _github_helper.create_repo(access_token, 'zhifei', 'byguitar')
_github_helper.create_repo(access_token, 'zhifei', 'byguitar')
# _github_helper.create_repo(access_token, 'llll')
# _*_ coding: utf-8 _*_
# @time     : 2019/04/12
# @Author   : Amir
# @Site     : 
# @File     : ch_login.py
# @Software : PyCharm

from flask import url_for,redirect,session
from functools import wraps


def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))
    return check_login

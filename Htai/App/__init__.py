# _*_ coding: utf-8 _*_
# @time     : 2019/04/12
# @Author   : Amir
# @Site     : 
# @File     : __init__.py.py
# @Software : PyCharm

from App.ext import init_ext
from App.settings import envs
from App.user_views import init_blue
from flask import Flask


def create_app():
    app = Flask(__name__,
                template_folder=settings.TEMPLATE_FOLDER,
                static_folder=settings.STATIC_DIR)
    # 初始化配置
    app.config.from_object(envs.get('develop'))

    # 初始化蓝图
    init_blue(app)

    # 初始化第三方插件
    init_ext(app)
    return app
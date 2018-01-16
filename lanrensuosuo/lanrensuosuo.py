#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#from sys import stdout
#from asyncio.log import logger
#import logging
import datetime
from functools import wraps
from html import escape

from flask import Flask, render_template, url_for, redirect, request, flash, sessions, make_response, current_app, \
    session, abort
from static.manage import login as l, typeaction, user
from static.manage import manage as m

app = Flask(__name__)
app.debug = True
app.config['DEBUG'] = True
#session的key
app.secret_key = 'lanrensousuo.com'

# 后台管理系统
@app.route('/houtaiguanli')
def login():
    #判断是否登录过
    if l.isLogin():
        return redirect('/manage')
    return  render_template("manage/login.html")

@app.route('/dologin',methods=['POST'])
def dologin():
    if request.method == 'POST':
        if l.do_the_login()>0 :
            flash('')
            return redirect('/manage')
            #return redirect( url_for( 'manage' ) )
        else :
            flash('用户名或者密码错误！')
            return redirect('/houtaiguanli')

#验证登录的装饰器
def checkLogin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if l.isLogin() is True:
            return func(*args, **kwargs)
        else:
            return redirect('/houtaiguanli')
    return wrapper

@app.route('/manage',methods=['GET'])
@app.route('/manage/<int:page>')
@checkLogin
def manage(page=1):
    return render_template("manage/manage.html",clist = m.getLsit(page) )

@app.route('/cdelete',methods=['POST','GET'])
def cdelete():
    m.delete()
    return redirect('/manage')

@app.route('/type',methods=['GET'])
@checkLogin
def type():
    return render_template("manage/type.html" ,clist = typeaction.getLsit() )

@app.route('/tdelete',methods=['POST','GET'])
@checkLogin
def tdelete():
    typeaction.delete()
    return redirect('/type')
@app.route('/tadd',methods=['POST','GET'])
@checkLogin
def tadd():
    issubmit = request.values.get('issubmit')
    if issubmit:
        result = typeaction.add()
        if result:
            flash('添加成功')
        else:
            flash('添加失败')
        return redirect('/tadd')
    else:
        return render_template("manage/tadd.html")

@app.route('/tupdate/<int:id>',methods=['POST','GET'])
@checkLogin
def tupdate(id=0):
    issubmit = request.values.get('issubmit')
    if issubmit:
        result = typeaction.update( id )
        if result:
            flash('修改成功')
        else:
            flash('修改失败')
        return redirect('/type')
    else:
        return render_template("manage/tupdate.html",row = typeaction.getRow(id))


@app.route('/users',methods=['GET'])
@checkLogin
def users():
    return render_template("manage/user.html",lists = user.getLsit() )

# 修改用户
@app.route('/uupdate/<int:id>',methods=['POST','GET'])
@checkLogin
def uupdate(id=0):
    issubmit = request.values.get('issubmit')
    if issubmit:
        result = user.update(id)
        if result:
            flash('修改成功')
        else:
            flash('修改失败')
        return redirect( url_for( '.uupdate',id= id))
    else:
        return render_template("manage/user/uupdate.html", row=user.getRow(id))
# 删除用户
@app.route('/udelete',methods=['POST','GET'])
@checkLogin
def udelete():
    user.delete()
    return redirect('/users')

@app.route('/uadd',methods=['POST','GET'])
@checkLogin
def uadd():
    issubmit = request.values.get('issubmit')
    if issubmit:
        result = user.add()
        if result:
            flash('添加成功')
        else:
            flash('添加失败')
        return redirect('/uadd')
    else:
        return render_template("manage/user/uadd.html")










#前台页面

@app.route('/',methods=['POST','GET'])
@app.route('/<int:id>',methods=['POST','GET'])
def index( id = 1 ):

    return render_template("protal/index.html",clist = typeaction.getLsit(), urls = m.getListByid( id ) )

@app.route("/about")
def about():
    return render_template("protal/about.html",clist = typeaction.getLsit(),)



if __name__ == '__main__':
    app.run()

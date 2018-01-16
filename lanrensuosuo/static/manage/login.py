#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import datetime
import hashlib
from flask import request, app, render_template, make_response, session, url_for, redirect
import MySQLdb
import sqlalchemy

#提交登录
from static.utils.UserModel import User


def do_the_login():
    username = request.form['username']
    password = request.form['password']

    if username=="" or password=="":
        return 0
    password_md5 = md5( password.encode('utf-8') )
    b = User()
    user = b.getUser( "username='"+username+"' and password = '"+password_md5+"'" )
    if user :
        #resp = make_response("")
        # outdate = datetime.datetime.today() + datetime.timedelta(days=30)
        # resp.set_cookie('username', user.username.encode('utf-8'), expires=outdate)
        # resp.set_cookie('userId', (str(user.id)).encode('utf-8'), expires=outdate)
        # resp.set_cookie('mail',user.mail.encode('utf-8'), expires=outdate)
        session['username'] = user.username
        session['userId'] = ( str( user.id ) )
        session['mail'] = user.mail
        return 1
    else:
        return 0
#是否已登录
def isLogin():
    username = None #request.cookies.get('username')
    userId = None
    mail = None
    if 'username' in session:
        username = session['username']
    if 'userId' in session:
        userId = session['userId']
    if 'mail' in session:
        mail = session['mail']
    if username:
        return True
    else :
        return False


def md5(str):
    if  str :
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

if __name__ == '__main__':
    resp = make_response("hel")
    outdate = datetime.datetime.today() + datetime.timedelta(days=30)
    resp.set_cookie('username2', "niao", expires=outdate)
    resp.set_cookie('userId2', "nihaoa", expires=outdate)
    resp.set_cookie('mail2',"llslsksks", expires=outdate)
    username = request.cookies.get('username2')
    userId = request.cookies.get('userId2')
    mail = request.cookies.get('mail2')
    print(username)
    print(userId)
    print(mail)


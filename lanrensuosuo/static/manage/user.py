#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math

import time

from flask import request

from static.manage.login import md5
from static.utils.ContentModel import Content

#查询列表
from static.utils.Page import get_page
from static.utils.TypeModel import Type
from static.utils.UserModel import User


def getLsit():
    user = User()
    clist = user.getList("select * from lr_user")
    #if clist:
        #for index, li in enumerate(clist):
            # time_local = time.localtime(li[2])
            # dt = time.strftime("%Y-%m-%d", time_local)
            # listLi = list( li ) #转为列表更新值
            # listLi[2] = dt
            # clist[index]  = tuple( listLi ) #转成元组赋予列表
    datas = {
        'list': clist
    }

    return datas
def getRow( id ):
    type = User()
    row = type.getRow("id = {0}".format(id))
    return row
def update( id ):
    username = request.form['username']
    password = request.form['password']
    mail = request.form['mail']
    if username == "" or password == "" or mail == "":
        return False
    type = User()
    sql = "id = {0}".format(id)
    password =  md5( password.encode('utf-8') )
    type.update(id,sql,username,password,mail);
    return True

def delete():
    id = request.form['ids']
    user = User()
    user.delete( id );
    #content.delete("delete from lr_content where id in ("+id+")");
def add():
    username = request.form['username']
    password = request.form['password']
    mail = request.form['mail']
    if username == "" or password == "" or mail == "":
        return False

    type = User()
    type.username = username
    type.password = md5( password.encode('utf-8') )
    type.mail = mail
    type.add()

    return True


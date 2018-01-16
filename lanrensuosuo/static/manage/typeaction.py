#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math

import time

from flask import request

from static.utils.ContentModel import Content

#查询列表
from static.utils.Page import get_page
from static.utils.TypeModel import Type


def getLsit():
    type = Type()
    clist = type.getList("select * from lr_sort")
    if clist:
        for index, li in enumerate(clist):
            time_local = time.localtime(li[2])
            dt = time.strftime("%Y-%m-%d", time_local)
            listLi = list( li ) #转为列表更新值
            listLi[2] = dt
            clist[index]  = tuple( listLi ) #转成元组赋予列表
    datas = {
        'list': clist
    }

    return datas
def getRow( id ):
    type = Type()
    row = type.getRow("id = {0}".format(id))
    return row
def update( id ):
    name = request.form['name']
    if name == "":
        return False
    type = Type()
    sql = "id = {0}".format(id)
    type.update(id,sql,name);
    return True

def delete():
    id = request.form['ids']
    type = Type()
    type.delete( id );
    #content.delete("delete from lr_content where id in ("+id+")");
def add():
    name = request.form['name']
    if name == "":
        return False

    type = Type()
    type.parentid = 0
    type.ctime = int(time.time())
    type.name = name
    type.typeid = 1
    type.add()

    return True


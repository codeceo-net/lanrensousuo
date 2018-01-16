#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import math

import time

from flask import request, url_for

from static.utils.ContentModel import Content

#查询列表
from static.utils.Page import get_page


def getLsit(page=1):
    limit_start = (page - 1) * 20  # 起始

    show_shouye_status = 0  # 显示首页状态
    if page > 1:
        show_shouye_status = 1

    content = Content()

    total = int(math.ceil(content.getCount("") / 20))  # 总页数

    dic = get_page(total, page)
    clist = content.getList("select * from lr_content  limit {0},20".format(limit_start))
    if clist:
        for index, li in enumerate(clist):
            time_local = time.localtime(li[3])
            dt = time.strftime("%Y-%m-%d", time_local)
            listLi = list( li ) #转为列表更新值
            listLi[3] = dt
            clist[index]  = tuple( listLi ) #转成元组赋予列表
    datas = {
        'list': clist,
        'page': page,
        'total': total,
        'dic_list': dic,
        'show_shouye_status':show_shouye_status
    }

    return datas
def getListByid( id = 1 ):
    content = Content()
    clist = content.getList("select * from lr_content where sortid = {0}  limit 0,10000".format(id))
    print(clist)
    if clist:
        for index, li in enumerate(clist):
            listLi = list( li ) #转为列表更新值
            listLi[5] = url_for("static",filename='uploads/'+listLi[5])
            clist[index]  = tuple( listLi ) #转成元组赋予列表
    return clist

def delete():
    id = request.form['ids']
    content = Content()
    content.delete( id );
    #content.delete("delete from lr_content where id in ("+id+")");


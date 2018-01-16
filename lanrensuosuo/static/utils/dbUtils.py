#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, mapper
# 数据库类
class Db:
    #def __init__(self):

    @staticmethod
    def getDB():
        engine = create_engine("mysql://root:123456@127.0.0.1:3306/lanrensousuo?charset=utf8", encoding="utf-8",
                               echo=True)
        Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
        Session = Session_class()  # 生成session实例，相当于游标
        return Session




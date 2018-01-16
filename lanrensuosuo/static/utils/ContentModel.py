#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from static.utils.dbUtils import Db
class Content( declarative_base() ):
    __tablename__ = 'lr_content'
    id = Column(Integer, Sequence('id'), primary_key=True)
    title = Column(String)
    url = Column(String)
    ctime = Column(Integer)
    sortid = Column(Integer)
    img = Column(String)
    session = None
    def __init__(self):
        self.session = Db.getDB();

    def __repr__(self):
        return ""

    def getList(self,sql):
        #my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        my_user = self.session.execute( text( sql ) ).fetchall() # 查询
        self.session.close()
        return my_user
    def getCount(self, sql ):
        count = self.session.query(Content).filter( text(sql) ).count()
        self.session.close()
        return count
    def delete(self,sql):
        self.session.query(Content).filter(Content.id.in_( sql )).delete(synchronize_session=False)
        self.session.commit()
        self.session.close()
        return True

#模块使用
con = Content()
coount = con.getCount("id=3")
print( coount )

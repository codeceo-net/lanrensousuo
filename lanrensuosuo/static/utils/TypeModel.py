#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from static.utils.dbUtils import Db
class Type( declarative_base() ):
    __tablename__ = 'lr_sort'
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String)
    ctime = Column(Integer)
    typeid = Column(Integer)
    parentid = Column(Integer)
    session = None
    def __init__(self):
        self.session = Db.getDB();

    def __repr__(self):
        return "<lr_sort(id='%d', name='%s')>" % (
        self.id, self.name)

    def getList(self,sql):
        #my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        my_user = self.session.execute( text( sql ) ).fetchall() # 查询
        self.session.close()
        return my_user
    def getCount(self, sql ):
        count = self.session.query(Type).filter( text(sql) ).count()
        self.session.close()
        return count
    def delete(self,sql):
        self.session.query(Type).filter(Type.id.in_( sql )).delete(synchronize_session=False)
        self.session.commit()
        self.session.close()
        return True
    def add(self):
        self.session.add(self)
        self.session.commit()
        self.session.close()
        return True

    def getRow(self, sql):
        # my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        row = self.session.query(Type).filter(text( sql )).first()  # 查询
        self.session.close()
        return row
    def update(self, id, sql,name ):
        row = self.session.query(Type).filter(text( sql )).first()  # 查询
        row.name = name
        self.session.commit()
        self.session.close()
        return True
type = Type()
li = type.getRow(" id= 1 ")
print(li.id)
print(111)
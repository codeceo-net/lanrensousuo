#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from sqlalchemy import Column, Integer, String, Sequence, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from static.utils.dbUtils import Db
class User( declarative_base() ):
    __tablename__ = 'lr_user'
    id = Column(Integer, Sequence('id'), primary_key=True)
    username = Column(String)
    password = Column(String)
    mail = Column(String)
    session = None
    def __init__(self):
        self.session = Db.getDB();

    def __repr__(self):
        return "<lr_user(id='%d', username='%s', password='%s', mail='%s')>" % (self.id, self.username, self.password,self.mail)

    def getUser(self,sql):
        #my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        my_user = self.session.query(User).filter(text(sql)).first()  # 查询
        self.session.close()
        return my_user
    def getList(self,sql):
        #my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        my_user = self.session.execute( text( sql ) ).fetchall() # 查询
        self.session.close()
        return my_user
    def delete(self,sql):
        self.session.query(User).filter(User.id.in_( sql )).delete(synchronize_session=False)
        self.session.commit()
        self.session.close()
        return True
    def add(self):
        self.session.add( self )
        self.session.commit()
        self.session.close()
    def getRow(self, sql):
        # my_user = self.session.query(User).filter_by(text( sql )).first()  # 查询
        row = self.session.query(User).filter(text( sql )).first()  # 查询
        self.session.close()
        return row
    def update(self, id, sql,username,password,mail ):
        row = self.session.query(User).filter(text( sql )).first()  # 查询
        row.username = username
        row.password = password
        row.mail = mail
        self.session.commit()
        self.session.close()
        return True
if __name__ == '__main__':
    b = User()
    user = b.getUser( "username='lisu860619' and id =1 " )
    print(user)
#coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:1a2b3c4d5f@47.97.86.161:3306/test?charset=utf8", max_overflow=5,encoding='utf-8')
Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'
    rid = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
    role_name = Column(String(10))
    user = relationship('User',backref='role_back')
    def __repr__(self):
        output = "(%s,%s)" %(self.rid,self.role_name)
        return output

class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(10),nullable=False)
    role = Column(Integer,ForeignKey('role.rid'))  #外键关联
    def __repr__(self):
        output = "(%s,%s,%s)" %(self.nid,self.name,self.role)
        return output

# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# #
# ##添加角色数据
# session.add(Role(role_name='dba'))
# session.add(Role(role_name='sa'))
# session.add(Role(role_name='net'))
#
# ##添加用户数据
# session.add_all([
#     User(name='fuzj',role='1'),
#     User(name='jie',role='2'),
#     User(name='张三',role='2'),
#     User(name='李四',role='1'),
#     User(name='王五',role='3'),
#     User(name='王刘',role='3'),
# ])
# session.commit()
# session.close()

roles =  session.query(Role).all()
print(roles[0])
print(roles[0].user)


users =  session.query(User).all()
print(users[0])
print(users[0].role_back)
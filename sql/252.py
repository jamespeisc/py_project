import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Date,Enum
from sqlalchemy.orm import declarative_base

# connstr = '{}://username:pwd@ip:port/databasename?key=value'.format(
connstr = '{}://{}:{}@{}:{}/{}'.format(
'mysql+pymysql',
'root','web123',
'192.168.56.101',3310,
'test'
)

engine = create_engine(connstr,echo=True)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student' # 请手动指定表名

    id = Column(Integer,primary_key=True,autoincrement=True)
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<student {} {} {}>".format(self.id,self.name,self.age)

s1 = Student()
s1.age = 20
s1.name='tom'

print(s1)

s2 = Student(id =5,name='jerry')
s2.age = 30

print(s2)

Base.metadata.create_all(bind=engine) # 创建表
# Base.metadata.drop_all()
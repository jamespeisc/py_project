from sqlalchemy import create_engine, Column, Integer, String, Date, Enum

from sqlalchemy.orm import declarative_base, sessionmaker

# connstr = '{}://username:pwd@ip:port/databasename?key=value'.format(
connstr = '{}://{}:{}@{}:{}/{}'.format(
'mysql+pymysql',
'root', 'web123',
'192.168.56.101', 3310,
'test'
)

engine = create_engine(connstr, echo=True)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'  # 请手动指定表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<student {} {} {}>".format(self.id, self.name, self.age)


Base.metadata.create_all(bind=engine)  # 创建表
# Base.metadata.drop_all()

Session = sessionmaker(bind=engine)  # Session类
session = Session()  # session实例

s1 = Student(name='tom')
s1.age = 20

session.add(s1)

s2 = Student()
s2.id = 10
s2.name = 'jerry'
s2.age = 18

session.add(s2)

try:
    session.commit()
except Exception as e:
    print(e)
    session.rollback()


query = session.query(Student)

print(type(query))

for student in query:
    print(student) # 都是行数据
# 改数据需要先查询
student = session.query(Student).get(10) # 主键查询
print(student)

student.age = 38
session.add(student)
session.commit()

print(student)

# 以下为insert
student = Student()
student.id = 10
student.name = 'sam'
student.age = 58
print(student)
session.add(student)

try:
    session.commit()
except Exception as e:
    print(e,'~~~~~~~~~')
    session.rollback()
print(student) # 被认为是新数据


# 删除数据,需要先查询

student = session.query(Student).get(10)
session.delete(student)
try:
    session.commit()
except Exception as e:
    print(e,'~~~~~~~~~')
    session.rollback()
print(student) # 被认为是新数据


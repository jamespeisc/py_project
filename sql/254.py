from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import enum

# connstr = '{}://username:pwd@ip:port/databasename?key=value'.format(

connstr = '{}://{}:{}@{}:{}/{}'.format(
    'mysql+pymysql',
    'root', 'web123',
    '192.168.56.101', 3310,
    'test'
)
engine = create_engine(connstr, echo=True)
Base = declarative_base()
# Base.metadata.create_all(bind=engine)  # 创建表
Session = sessionmaker(bind=engine)  # Session类
session = Session()  # session实例


class Gender(enum.Enum):
    M = 'M'
    F = 'F'


class Employee(Base):
    __tablename__ = 'employees'  # 请手动指定表名
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    hire_date = Column(Date, nullable=False)


def __repr__(self):
    return "<emp {} {} {}>".format(self.emp_no, self.first_name, self.last_name
                                   )


def show(emps):
    for x in emps:
        print(x)
    print('xxxxxxxxxx', end='\n\n')


from sqlalchemy import and_, or_, not_

# 与
query = session.query(Employee).filter(Employee.emp_no > 10016).filter(Employee.emp_no < 10019)
show(query)
query = session.query(Employee).filter((Employee.emp_no > 10016) & (Employee.emp_no < 10019))
show(query)
query = session.query(Employee).filter(and_(Employee.emp_no > 10016, Employee.emp_no < 10019))
show(query)
# 或
query = session.query(Employee).filter((Employee.emp_no > 10016) | (Employee.emp_no < 10019))
show(query)
query = session.query(Employee).filter(or_(Employee.emp_no > 10016, Employee.emp_no < 10019))
show(query)
# 非
query = session.query(Employee).filter(not_(Employee.emp_no > 10016))
show(query)

query = session.query(Employee).filter(~(Employee.emp_no > 10016))
show(query)

query = session.query(Employee).filter(Employee.emp_no.in_([10015, 10018]))

query = session.query(Employee).filter(Employee.emp_no.like('P%'))

query = session.query(Employee).filter(Employee.last_name.like('P%')).order_by(Employee.emp_no.desc()).limit(2).offset(
    3)

show(query)

print(query, '!!!!!!!!')
print(query.all())  # 消费者方法
print(query.first())  # 找到第一行
print(query.one())  # 找到仅有一个

print(query.count())
print(len(list(query)))
print(query.scalar())  # 返回元组的第一个元素

session.query(Employee).filter(Employee.emp_no > 100018).delete()

# 聚合分组

from sqlalchemy import func

query = session.query(func.count(Employee.emp_no)).scalar()
query = session.query(func.avg(Employee.emp_no)).scalar()

query = session.query(func.max(Employee.emp_no)).scalar()

query = session.query(func.min(Employee.emp_no)).scalar()

query = session.query(func.count(Employee.emp_no))  # 推荐

print(session.query(Employee.gender, func.count(Employee.emp_no)).group_by(Employee.gender).all())


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(Integer, primary_key=True)
    dept_name = Column(String(40), nullable=False)

    def __repr__(self):
        return "<Dept {} {}>".format(self.dept_no, self.dept_name)


departments = relationship('Dept_emp')


class Dept_emp(Base):
    __tablename__ = 'dept_emp'
    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True)
    dept_no = Column(Integer, ForeignKey('departments.dept_no'), primary_key=True, ondelete='CASCADE')
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)


# join 查询

query = session.query(Employee, Dept_emp).filter(Employee.emp_no == 10010).filter(Employee.emp_no == Dept_emp.emp_no)

print(query)

query = session.query(Employee).join(Dept_emp).filter(Employee.emp_no == 10010).filter(
    Employee.emp_no == Dept_emp.emp_no)

# 需要用员工表作为主表

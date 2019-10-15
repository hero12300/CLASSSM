# IPython log file

from sqlalchemy import create_engine, Column, Integer, String, VARCHAR,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship,  backref
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(mysql://'root:@localhost/shiyanlou?charset=utf8',encoding='utf-8')
engine = create_engine("mysql://root:@localhost/shiyanlou?charset=utf8",encoding='utf-8')
session = sessionmaker(engine)()
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    def __repr__(self):
        return"<User(name=%s)>" % self.name
    
class Lab(Base):
    __tablename__ = 'lab'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer,ForeignKey('course.id'))
    course = relationship('Course',backref='labs')
    def __repr__(self):
        return '<Lab(name=%s)>'% self.name
    
class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer,ForeignKey('user.id'))
    teacher = relationship('User')
    def __repr__(self):
        return '<Course(name=%s)'% self.name
    
class Path(Base):
    __tablename__ = 'path'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64), nullable=False)
    config = Column(VARCHAR(128))
    def __repr__(self):
        return'<Path(name=%s)'%self.name
    
course = session.query(Course).first()
lab1 = Lab(name='ORM 基础',course_id=course.id)
lab2 = Lab(name='关系数据库',course=course)
session.add(lab1)
session.add(lab2)
session.commit()
get_ipython().magic('logstart hahah.py')
get_ipython().magic('logstop')

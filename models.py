from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Table, Column, BigInteger, Unicode, Float, Numeric, Integer, ForeignKey

db = SQLAlchemy()

class STUDENT(db.Model):
    __tablename__ = 'STUDENT'
    __table_args__ = {'extend_existing': True}
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(50))
    age = Column(Unicode(50))
    level = Column(Unicode(50))

class user_table(db.Model):
    __tablename__ = 'user_table'
    __table_args__ = {'extend_existing': True}
    ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(50))
    email = Column(Unicode(50))
    password = Column(Unicode(50))

class ROLE(db.Model):
    __tablename__ = 'ROLE'
    __table_args__ = {'extend_existing': True}
    ID = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(Unicode(50))
    id_user = Column(
        Integer,
        ForeignKey('user_table.ID', ondelete='CASCADE'),
        nullable=False,
    )

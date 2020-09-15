from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(DateTime)
    price = Column(Float)

    def __repr__(self):
        return "<Book(title='{}',author='{}',pages={},published={},price={})>" \
        .format(self.title,self.author,self.pages,self.published,self.price)
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
import os
from datetime import datetime

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR,'pini.db')
Base=declarative_base()

# engine = create_engine('sqlite:///pini.db', echo = True)
engine=create_engine(connection_string,echo=True)
Session=sessionmaker()

# print(connection_strings)
class datas(Base):
   __tablename__='pini_data'
   id=Column(Integer(),primary_key=True)
   group=Column(String(25),nullable=False)
   year=Column(String(25),nullable=False)
   inflation=Column(String(25),nullable=False)
   added_on=Column(DateTime(),default=datetime.utcnow)

   def __repr__(self):
      return f"<datas group={self.group} year={self.year} inflation={self.inflation}"

# newuser=datas(id=1,group='kani',year='2025',inflation='2005')
# print(newuser)
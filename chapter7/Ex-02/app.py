from models import Base, Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

#create engine
db_uri = 'sqlite:///Ex2.db'
engine = create_engine(db_uri, echo=False)

#Create All Table
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''
user = Member(
    name='Test2',
    description='Prachinburi',
    vip=True,
    join_date=datetime.datetime.now(),
    number=45.0
)
'''
#session.add(user)


#obj = session.query(Member).filter(Member.id==1).first()
#session.delete(obj)

session.query(Member).filter(Member.id==2).update({Member.name:"Johnson"})


session.commit()
#print(user)
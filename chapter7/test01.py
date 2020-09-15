import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

#Base.metadata.drop_all(engine)
Base.metadata.crete_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#for isinstance in session.query(User).order_by(User.id):
#    print(instance.name, instance.fullname)

#for isinstance in session.query(User).filter(User.name.in(('user1','user2'))):
#    print(instance.name, instance.fullname)

user1 = User(name='user1',fullname='Ed Jones',nickname='ed')
#user1 = User(name='user2',fullname='TEd Jones',nickname='Ted')
#user3 = User(name='user3',fullname='STEd Jones',nickname='STed')
#user4 = User(name='user4',fullname='WTEd Jones',nickname='WTed')

session.add(user1)
session.commit()


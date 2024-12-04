import bcrypt
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

def register(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username=username, password=hashed_password)
    session.add(user)
    session.commit()
    print("User registered successfully!")

def login(username, password):
    user = session.query(User).filter_by(username=username).first()
    if user and bcrypt.checkpw(password.encode(), user.password):
        print("Login successful!")
        return True
    print("Invalid credentials!")
    return False

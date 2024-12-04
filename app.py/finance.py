from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.auth import Base, session

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    type = Column(String, nullable=False)  # Income or Expense
    description = Column(String)

Base.metadata.create_all()

def add_transaction(user_id, amount, category, trans_type, description=""):
    transaction = Transaction(user_id=user_id, amount=amount, category=category, type=trans_type, description=description)
    session.add(transaction)
    session.commit()
    print("Transaction added successfully!")

def view_transactions(user_id):
    transactions = session.query(Transaction).filter_by(user_id=user_id).all()
    for t in transactions:
        print(f"{t.type} | {t.amount} | {t.category} | {t.description}")

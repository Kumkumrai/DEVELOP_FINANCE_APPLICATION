from unittest.mock import Base
from requests import session
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Transaction, func


class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String, nullable=False)
    limit = Column(Float, nullable=False)

Base.metadata.create_all()

def set_budget(user_id, category, limit):
    budget = Budget(user_id=user_id, category=category, limit=limit)
    session.add(budget)
    session.commit()
    print(f"Budget set for {category}: {limit}")

def check_budget(user_id):
    budgets = session.query(Budget).filter_by(user_id=user_id).all()
    for budget in budgets:
        spent = session.query(func.sum(Transaction.amount))\
                       .filter_by(user_id=user_id, category=budget.category, type="Expense").scalar() or 0
        if spent > budget.limit:
            print(f"Exceeded budget for {budget.category}: Spent {spent} > Limit {budget.limit}")

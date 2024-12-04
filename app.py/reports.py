from sqlalchemy import func
from app.finance import Transaction, session 

def generate_report(user_id, period="monthly"):
    query = session.query(Transaction.type, func.sum(Transaction.amount), Transaction.category)\
                   .filter(Transaction.user_id == user_id)\
                   .group_by(Transaction.type, Transaction.category)

    print(f"Financial Report ({period.capitalize()}):")
    for row in query:
        print(f"{row[0]} - {row[1]} in {row[2]}")

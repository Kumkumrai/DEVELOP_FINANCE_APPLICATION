from sqlalchemy import func
from app.finance import Transaction, session  # Ensure proper import

def generate_report(user_id, period="monthly"):
    # Build the query to aggregate the data
    query = session.query(
                Transaction.type,
                func.sum(Transaction.amount).label('total_amount'),
                Transaction.category
            )\
            .filter(Transaction.user_id == user_id)  # Filter by user_id
    
    # Handle periods (monthly, yearly, etc.) - just an example if you want period-based filtering
    if period == "monthly":
        query = query.filter(Transaction.date >= '2024-11-01')  # Example date range for monthly
    
    query = query.group_by(Transaction.type, Transaction.category)  # Group by transaction type and category
    
    # Output the report
    print(f"Financial Report ({period.capitalize()}):")
    for row in query:
        print(f"{row.type} - {row.total_amount} in {row.category}")


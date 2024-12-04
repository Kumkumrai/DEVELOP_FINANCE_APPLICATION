
from typing import Any
import pytest

from app.finance import FinanceTracker

@pytest.fixture
def finance_tracker():
    # Setup a FinanceTracker instance for use in tests
    return FinanceTracker()

def test_add_transaction(finance_tracker: Any):
    # Test adding an income transaction
    finance_tracker.add_transaction ("Salary", 5000, "income")
    assert len(finance_tracker.transactions) == 1
    assert finance_tracker.transactions[0].category == "Salary"
    assert finance_tracker.transactions[0].amount == 5000
    assert finance_tracker.transactions[0].transaction_type == "income"

    # Test adding an expense transaction
    finance_tracker.add_transaction("Rent", 1200, "expense")
    assert len(finance_tracker.transactions) == 2
    assert finance_tracker.transactions[1].category == "Rent"
    assert finance_tracker.transactions[1].amount == 1200
    assert finance_tracker.transactions[1].transaction_type == "expense"

def test_get_balance(finance_tracker: Any):
    # Test the balance calculation (income - expense)
    finance_tracker.add_transaction("Salary", 5000, "income")
    finance_tracker.add_transaction("Rent", 1200, "expense")
    balance = finance_tracker.get_balance()
    assert balance == 3800  # 5000 (income) - 1200 (expense)

def test_show_report(finance_tracker: Any):
    # Test the report generation
    finance_tracker.add_transaction("Salary", 5000, "income")
    finance_tracker.add_transaction("Rent", 1200, "expense")
    
    # Capture the output of the report method
    from io import StringIO
    import sys
    captured_output = StringIO()
    sys.stdout = captured_output
    finance_tracker.show_report()
    sys.stdout = sys.__stdout__
    
    # Check if the correct report was printed
    assert "Salary" in captured_output.getvalue()
    assert "Rent" in captured_output.getvalue()
    assert "Total Balance: 3800" in captured_output.getvalue()

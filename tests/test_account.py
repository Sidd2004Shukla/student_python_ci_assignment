import pytest

from student_account import BankAccount


def test_deposit_increases_balance():
    account = BankAccount("Alice", 100)
    assert account.deposit(50) == 150


def test_withdraw_decreases_balance():
    account = BankAccount("Bob", 200)
    assert account.withdraw(75) == 125


def test_monthly_interest_calculation():
    account = BankAccount("Charlie", 1200)
    interest = account.monthly_interest(0.06)  # 6% annual interest
    assert round(interest, 2) == 6.0
    assert round(account.balance, 2) == 1206.0


def test_transfer_between_accounts():
    account1 = BankAccount("David", 300)
    account2 = BankAccount("Eve", 100)
    account1.transfer_to(account2, 50)
    assert account1.balance == 250
    assert account2.balance == 150


def test_transaction_count():
    account = BankAccount("Frank", 500)
    account.deposit(100)
    account.withdraw(50)
    account.monthly_interest(0.05)
    assert account.transaction_count == 3


def test_statement_format():
    account = BankAccount("Grace", 400)
    account.deposit(100)
    account.withdraw(50)
    statement = account.statement()
    assert "Owner: Grace" in statement
    assert "Balance: 450.00" in statement
    assert "Transactions: 2" in statement


def test_init_with_default_balance():
    account = BankAccount("Henry")
    assert account.balance == 0.0
    assert account.owner == "Henry"


def test_init_with_empty_owner_raises_error():
    with pytest.raises(ValueError, match="Owner name cannot be empty"):
        BankAccount("", 100)


def test_init_with_whitespace_owner_raises_error():
    with pytest.raises(ValueError, match="Owner name cannot be empty"):
        BankAccount("   ", 100)


def test_init_with_negative_balance_raises_error():
    with pytest.raises(ValueError, match="Opening balance cannot be negative"):
        BankAccount("Iris", -50)


def test_deposit_with_zero_raises_error():
    account = BankAccount("Jack", 100)
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.deposit(0)


def test_deposit_with_negative_raises_error():
    account = BankAccount("Kate", 100)
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.deposit(-25)


def test_withdraw_with_zero_raises_error():
    account = BankAccount("Liam", 100)
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.withdraw(0)


def test_withdraw_with_negative_raises_error():
    account = BankAccount("Mia", 100)
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        account.withdraw(-50)


def test_withdraw_insufficient_funds():
    account = BankAccount("Nina", 100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)


def test_transfer_with_invalid_target_type():
    account = BankAccount("Oscar", 300)
    with pytest.raises(TypeError, match="Target must be a BankAccount"):
        account.transfer_to("invalid", 50)  # type: ignore


def test_transfer_to_updates_transaction_count():
    account1 = BankAccount("Paul", 200)
    account2 = BankAccount("Quinn", 50)
    account1.transfer_to(account2, 75)
    assert account1.transaction_count == 1  # withdrawal
    assert account2.transaction_count == 1  # deposit


def test_monthly_interest_with_negative_rate():
    account = BankAccount("Rachel", 1000)
    with pytest.raises(ValueError, match="Annual rate cannot be negative"):
        account.monthly_interest(-0.05)


def test_monthly_interest_with_zero_rate():
    account = BankAccount("Steve", 1000)
    interest = account.monthly_interest(0.0)
    assert interest == 0.0
    assert account.balance == 1000.0


def test_statement_with_no_transactions():
    account = BankAccount("Tina", 500)
    statement = account.statement()
    assert "Owner: Tina" in statement
    assert "Balance: 500.00" in statement
    assert "Transactions: 0" in statement
    assert "No transactions." in statement


def test_balance_property():
    account = BankAccount("Uma", 750.5)
    assert account.balance == 750.5


def test_transaction_count_property():
    account = BankAccount("Victor", 100)
    assert account.transaction_count == 0
    account.deposit(50)
    assert account.transaction_count == 1










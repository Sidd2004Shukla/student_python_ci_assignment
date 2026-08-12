from student_account.account import BankAccount


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
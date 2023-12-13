import itertools
from datetime import datetime
from typing import List

class Transaction:
    id_iter: itertools.count = itertools.count()
    
    def __init__(self, type: str, amount: float):
        self.id: int = next(Transaction.id_iter)
        self.type: str = type
        self.amount: float = amount
        self.date: datetime = datetime.now()



class Account:
    id_iter: itertools.count = itertools.count()

    def __init__(self):
        self.id: int = next(Account.id_iter)
        self.balance: float = 0.0
        self.transactions: List[Transaction] = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(Transaction('deposit', amount))
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Withdraw: Insufficient funds')
        self.balance -= amount
        self.transactions.append(Transaction('withdraw', amount))
    
    def transfer(self, amount: float, target_account: 'Account') -> None:
        if amount > self.balance:
            raise ValueError('Transfer: Insufficient funds')
        self.withdraw(amount)
        target_account.deposit(amount)




class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = {}
    
    def create_account(self) -> Account:
        account = Account()
        self.accounts[account.id] = account
        return account
    
    def get_top_accounts_by_transactions(self, n: int) -> List[Account]:
        return sorted(self.accounts.values(), key=lambda account: len(account.transactions), reverse=True)[:n]
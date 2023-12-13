import unittest
from models import Bank, Account, Transaction

class TestBankingSystem(unittest.TestCase):

    # Unit tests for Account methods
    def test_deposit(self):
        account = Account()
        account.deposit(100)
        self.assertEqual(account.balance, 100)
        self.assertEqual(len(account.transactions), 1)
        self.assertEqual(account.transactions[0].amount, 100)

    def test_withdraw(self):
        account = Account()
        account.deposit(200)
        account.withdraw(50)
        self.assertEqual(account.balance, 150)
        self.assertEqual(len(account.transactions), 2)
        self.assertEqual(account.transactions[1].amount, 50)
        self.assertEqual(account.transactions[1].type, "withdraw")
    
    def test_insufficient_funds_withdraw(self):
        account = Account()
        with self.assertRaises(ValueError):
            account.withdraw(100)

    
    def test_transfer(self):
        account1 = Account()
        account2 = Account()
        account1.deposit(200)
        account1.transfer(50, account2)
        self.assertEqual(account1.balance, 150)
        self.assertEqual(account2.balance, 50)

    def test_insufficient_funds_transfer(self):
        account1 = Account()
        account2 = Account()
        with self.assertRaises(ValueError):
            account1.transfer(100, account2)
    

    # Unit tests for Bank methods
    def test_account_creation(self):
        bank = Bank()
        account = bank.create_account()
        self.assertIsInstance(account, Account)
        self.assertEqual(account.balance, 0)
        self.assertEqual(len(account.transactions), 0)
    
    def test_top_accounts_by_transactions(self):
        bank = Bank()
        acc1 = bank.create_account()
        acc1.deposit(100)

        acc2 = bank.create_account()
        acc2.deposit(100)
        acc2.withdraw(50)
        acc2.deposit(1000)
        acc2.transfer(100, acc1)

        acc3 = bank.create_account()

        top_accounts = bank.get_top_accounts_by_transactions(2)

        self.assertEqual(top_accounts[0], acc2)
        self.assertEqual(top_accounts[1], acc1)

if __name__ == '__main__':
    unittest.main()
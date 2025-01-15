class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount class with an optional initial balance.
        :param initial_balance: Starting balance of the account (default is 0).
        """
        self.__account_balance = initial_balance  # Encapsulated account balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        :param amount: Amount to withdraw.
        :return: True if the withdrawal is successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

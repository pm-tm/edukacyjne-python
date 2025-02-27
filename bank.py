# Stwórz symulator banku w Pythonie, korzystając z programowania obiektowego.
# Symulator powinien zawierać klasy BankAccount i Bank.
# Klasa BankAccount powinna mieć atrybuty: numer konta, saldo, właściciel konta.
# Klasa BankAccount powinna mieć metody: wpłata, wypłata, sprawdzanie salda.
# Klasa Bank powinna zarządzać wieloma kontami bankowymi.
# Klasa Bank powinna mieć metody: dodawanie konta, usuwanie konta, wyszukiwanie konta po numerze konta.

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
    def get_owner_name(self):
        return self.owner

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def find_account(self, account_number):
        return self.accounts.get(account_number)

# Przykładowe użycie:
bank = Bank()
account1 = BankAccount("123456", "Jan Kowalski", 1000)
bank.add_account(account1)

print(account1.get_balance())  # Wyświetli: 1000
account1.deposit(500)
print(account1.get_balance())  # Wyświetli: 1500
account1.withdraw(200)
print(account1.get_balance())  # Wyświetli: 1300

print("\n")
print(bank.find_account("123456").get_balance())
print(bank.find_account("123456").get_owner_name())

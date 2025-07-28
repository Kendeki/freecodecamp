class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger: list[dict[str, float | str]] = []

    def __str__(self):
        return f'{("*" * (15 - len(self.name)//2)) + self.name + ("*" * (15 - len(self.name)//2))}'

    def check_funds(self, amount: float) -> bool:
        return sum([i['amount'] for i in self.ledger]) > amount

    def deposit(self, amount: float, description: str = '') -> None:
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float, description: str = '') -> bool:
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self) -> float:
        return sum([i['amount'] for i in self.ledger])
    
    def transfer(self, amount: float, category: 'Category') -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to {category.name}')
            category.deposit(amount, 'Transfer from {self.name}') 
            return True
        return False
    
#def create_spend_chart(categories):
#    pass

a = Category('a')
a.deposit(1222, 'oi')
print(a)
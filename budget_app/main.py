class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger: list[dict[str, float | str]] = []

    def __str__(self):
        MAX_CHARACTERS_PER_LINE = 30
        MAX_CHARACTERS_PER_DESCRIPTION = 23
        title = f"{self.name:*^{MAX_CHARACTERS_PER_LINE}}\n"
        transactions = ''.join([
            i['description'][:MAX_CHARACTERS_PER_DESCRIPTION] + # description
            ' ' * (MAX_CHARACTERS_PER_LINE - len(i['description'][:MAX_CHARACTERS_PER_DESCRIPTION]) - len(f"{(i['amount']):.2f}")) + # spaces between description and amout 
            f"{(i['amount']):.2f}\n" # amount
            for i in self.ledger
                        ])
        
        return title + transactions + f'Total: {self.get_balance():.2f}'

    def check_funds(self, amount: float) -> bool:
        return sum([i['amount'] for i in self.ledger]) >= amount

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
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}') 
            return True
        return False
    
def create_spend_chart(categories: list[Category]) -> str:
    def check_withdraws(category: Category) -> float:
        return sum(i['amount'] if i['amount'] < 0 else 0 for i in category.ledger)
    
    def num_circles(withdraw: list[float]) -> list[int]:
        return [int(round(i/sum(withdraw)*100, -1)/10) + 1 for i in withdraw]
    
    withdraws_percentage = num_circles(list(map(check_withdraws, categories)))
    print(withdraws_percentage)
    
    title = 'Percentage spent by category\n'

    return ''
    
# test case

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(240.15, 'groceries')
food.withdraw(100.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(500, clothing)
clothing.withdraw(240.15, 'groceries')
print(food)
a = Category('a')
a.deposit(1223, 'skibidi')
a.withdraw(100, 'groceries')
a.withdraw(152.89, 'teste')
b = Category('b')
a.transfer(500, b)
b.withdraw(300, 'groceries')
create_spend_chart([food,clothing,a,b])
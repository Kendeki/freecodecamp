from math import floor

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

    def percentage(withdraw: list[float]) -> list[int]:
        return [int(floor(i/sum(withdraw)*100)) for i in withdraw]
    
    withdraws_percentage = percentage(list(map(check_withdraws, categories)))
    
    output_string = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        output_string += f'{i!s:>3}| '
        for p in withdraws_percentage:
            output_string += f'{"o" if p >= i else " "}  '
        output_string += '\n'
    
    output_string += f'{(x := "-" * 3 * len(categories) + "-"):>{len(x)+4}}\n'
    longest_word = max([len(i.name) for i in categories])

    for i in range(longest_word):
        output_string += ' ' * 5
        for category in categories:
            try:
                output_string += f'{category.name[i]}  '
            except IndexError:
                output_string += ' ' * 3
        if i != longest_word - 1:
            output_string += '\n'

    return output_string
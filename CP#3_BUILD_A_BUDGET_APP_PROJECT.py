class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
    def deposit(self, amount, description = ''):
        return self.ledger.append({"amount": amount, "description": description})
    def getBalance(self):
        current_balance = 0
        for entry in self.ledger:
            current_balance += entry["amount"]
        return current_balance
    def checkFund(self, amount):
        if amount > self.getBalance(): return False
        else: return True
    def withdraw(self, amount, description = ''):
        if self.checkFund(amount):
            self.ledger.append({"amount": (- 1) * amount, "description": description})
            return True
        else: return False
    def transfer(self, amount, another_budget_category):
        if self.checkFund(amount):
            self.withdraw(amount, f"transfer to {another_budget_category.category}")
            another_budget_category.deposit(amount, f"transfer from {self.category}")
            return True
        else: return False
    def __str__(self):
        left_part_asterisk = (30 - len(self.category)) // 2
        right_part_asterisk = 30 - len(self.category) - left_part_asterisk
        title = '\n' + left_part_asterisk * '*' + self.category + right_part_asterisk * '*'
        for entry in self.ledger:
            if len(entry["description"]) > 23:
                title += f"\n{entry['description'][:23]}" + (7 - len(f'{entry["amount"]:.2f}')) * ' ' + f'{entry["amount"]:.2f}'
            else:
                title += f"\n{entry['description']}" + (30 - len(entry["description"]) - len(f'{entry["amount"]:.2f}')) * ' ' + f'{entry["amount"]:.2f}'
        title += f"\nTOTAL: {self.getBalance():.2f}\n"
        return title
def createSpendChart(category_set: list):
    # bring only category and correspond withdraw
    withdraw_for_every_category = {}
    for category in category_set:
        withdraw_count = 0
        for input_count in range(len(category.ledger)):
            if category.ledger[input_count]["amount"] < 0:
                withdraw_count += category.ledger[input_count]["amount"]
            else: pass
        withdraw_for_every_category[f"{category.category}"] = withdraw_count
    # bring only category and correspond withdraw percentage
    sum_of = sum(withdraw_for_every_category.values())
    percentage = {}
    for category_name, category_amount in withdraw_for_every_category.items():
        percentage[category_name] = int(category_amount / sum_of * 100 // 10)
    # write down for terminal
    bar_chart = 'PERCENTAGE SPENT BY CATEGORY'
    for tenner in range(100, -1, -10):
        bar_chart += '\n' + (3 - len(str(tenner))) * ' ' + f"{tenner}|"
        for value in percentage.values():
            if tenner == 0:
                bar_chart += " o "
            else:
                if value * 10 // tenner >= 1:
                    bar_chart += " o "
                else: pass
    bar_chart += "\n    " + ((len(percentage) - 1) * 2 + len(percentage) + 3) * '-'
    category_length = [len(string) for string in percentage.keys()]
    maximum_category_length = max(category_length)
    count = 0
    while count < maximum_category_length:
        bar_chart += "\n    "
        for category_type in percentage.keys():
            if count < len(category_type):
                bar_chart += f" {category_type[count]} "
            else: pass
        count += 1
    return bar_chart
if __name__ == "__main__":
    clothing = Category("clothing")
    food = Category("food")
    clothing.deposit(1000, "deposit")
    clothing.withdraw(105, "prom")
    clothing.transfer(50, food)
    food.withdraw(45, "dinner")
    print(clothing)
    print(createSpendChart([clothing, food]))
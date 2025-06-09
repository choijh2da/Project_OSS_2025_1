import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def compare_categories(self, catg_1, catg_2):
        total1 = sum(e.amount for e in self.expenses if e.category == catg_1)
        total2 = sum(e.amount for e in self.expenses if e.category == catg_2)

        print(f"\n[{catg_1} vs {catg_2} 지출 비교]")
        print(f"{catg_1}: {total1}원")
        print(f"{catg_2}: {total2}원")

        if total1 > total2:
            print(f"{catg_1} 지출이 더 많습니다.\n")
        elif total2 > total1:
            print(f"{catg_2} 지출이 더 많습니다.\n")
        else:
            print("지출이 같습니다.\n")
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append({
            'amount': amount,
            'category': category,
            'description': description
        })
        print(f"Добавлено: {description} - {amount} у.е. в категории '{category}'")

    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def show_expenses(self):
        if not self.expenses:
            print("Нет записанных расходов.")
            return

        print("nСписок расходов:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['description']} - {expense['amount']} у.е. (Категория: {expense['category']})")
        print(f"Общая сумма расходов: {self.total_expenses()} у.е.n")


def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Показать общий баланс")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            try:
                amount = float(input("Введите сумму расхода: "))
                category = input("Введите категорию: ")
                description = input("Введите описание: ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Введите корректную сумму.")

        elif choice == '2':
            tracker.show_expenses()

        elif choice == '3':
            print(f"Общий баланс расходов: {tracker.total_expenses()} у.е.n")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()

    
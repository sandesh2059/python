# ---------------- DATA STORAGE ----------------
expenses = []


# ---------------- LOGIC FUNCTIONS ----------------

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    note = input("Enter note (optional): ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("✅ Expense added successfully!")


def total_expense(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    return total


def category_summary(expenses):
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        amt = exp["amount"]

        if cat in summary:
            summary[cat] += amt
        else:
            summary[cat] = amt

    return summary


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - Rs. {exp['amount']} ({exp['note']})")


# ---------------- MENU ----------------

def menu():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. View Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)

        elif choice == '2':
            display_expenses(expenses)

        elif choice == '3':
            total = total_expense(expenses)
            print(f"💰 Total Expense: Rs. {total}")

        elif choice == '4':
            summary = category_summary(expenses)
            print("\n--- Category Summary ---")
            for cat, amt in summary.items():
                print(f"{cat}: Rs. {amt}")

        elif choice == '5':
            print("👋 Exiting Expense Tracker")
            break

        else:
            print("❌ Invalid choice, try again.")


# ---------------- RUN PROGRAM ----------------
menu()

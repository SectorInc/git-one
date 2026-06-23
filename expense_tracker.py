# Personal Daily Expense Tracker

def display_expenses(expenses):
    """Print all recorded expenses in a formatted table."""
    print("\n📋 Your Expenses:")
    print("-" * 35)
    for item, price in expenses.items():
        print(f"  {item:<20} ${price:.2f}")
    print("-" * 35)


def main():
    print("=" * 40)
    print("     PERSONAL EXPENSE TRACKER 💸")
    print("=" * 40)

    user_name = input("\nHello! What is your name? ").strip()

    while True:
        try:
            num_expenses = int(input(f"\n{user_name}, how many expenses do you have today? "))
            if num_expenses <= 0:
                print("❌ Please enter at least 1 expense.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")

    expenses = {}
    print()
    for i in range(num_expenses):
        expense_name = input(f"Expense {i + 1} name: ").strip()
        while True:
            try:
                expense_price = float(input(f"Price of '{expense_name}' $: "))
                if expense_price < 0:
                    print("❌ Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("❌ Please enter a valid price.")
        expenses[expense_name] = expense_price

    display_expenses(expenses)

    # Total
    see_total = input("\nWould you like to see your total expenses? (y/n): ").strip().lower()
    if see_total == 'y':
        print(f"💰 Total: ${sum(expenses.values()):.2f}")

    # Lowest
    see_lowest = input("Would you like to see your lowest expense? (y/n): ").strip().lower()
    if see_lowest == 'y':
        lowest_item = min(expenses, key=expenses.get)
        print(f"📉 Lowest: {lowest_item} — ${expenses[lowest_item]:.2f}")

    # Highest
    see_highest = input("Would you like to see your highest expense? (y/n): ").strip().lower()
    if see_highest == 'y':
        highest_item = max(expenses, key=expenses.get)
        print(f"📈 Highest: {highest_item} — ${expenses[highest_item]:.2f}")

    print(f"\nThanks for using Expense Tracker, {user_name}! Stay financially savvy 🚀")


if __name__ == "__main__":
    main()

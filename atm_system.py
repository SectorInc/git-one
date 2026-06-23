
# ATM Banking System


#  User Database 
users = {
    "user1": {"name": "John Doe",  "pin": "1234", "balance": 2000.00},
    "user2": {"name": "Jane Smith","pin": "5678", "balance": 1000.00},
}

# Tracks the currently logged-in user
current_user = None


def check_pin():
    """Prompt for user ID and PIN. Returns True on success."""
    global current_user
    user_id = input("Enter your User ID (user1 / user2): ").strip()

    if user_id not in users:
        print("❌ User not found.\n")
        return False

    pin = input("Enter your PIN: ").strip()
    if pin == users[user_id]["pin"]:
        current_user = user_id
        print(f"\n✅ Welcome, {users[current_user]['name']}!")
        return True
    else:
        print("❌ Incorrect PIN.\n")
        return False


def show_menu():
    """Display the ATM menu and return the user's choice."""
    print("\n--- ATM Menu ---")
    print("1) Withdraw")
    print("2) Check Balance")
    print("3) Transfer")
    print("4) Exit")
    return input("Select an option: ").strip()


def withdraw():
    """Withdraw funds from the current user's account."""
    balance = users[current_user]["balance"]
    try:
        amount = float(input("Enter withdrawal amount: $"))
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
        elif amount > balance:
            print(f"❌ Insufficient funds. Your balance is ${balance:.2f}.")
        else:
            users[current_user]["balance"] -= amount
            print(f"✅ ${amount:.2f} dispensed. Please collect your cash.")
            print(f"   Remaining balance: ${users[current_user]['balance']:.2f}")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")


def show_balance():
    """Display the current user's balance."""
    balance = users[current_user]["balance"]
    print(f"\n💳 Account Balance: ${balance:.2f}")


def transfer():
    """Transfer funds to another user account."""
    balance = users[current_user]["balance"]

    receiver_id = input("Enter the recipient's User ID: ").strip()
    if receiver_id not in users:
        print("❌ Recipient account not found.")
        return
    if receiver_id == current_user:
        print("❌ You cannot transfer to your own account.")
        return

    try:
        amount = float(input("Enter transfer amount: $"))
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return
        if amount > balance:
            print(f"❌ Insufficient funds. Your balance is ${balance:.2f}.")
            return
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    # Confirm with PIN before transferring
    receiver_name = users[receiver_id]["name"]
    print(f"\nConfirm transfer of ${amount:.2f} to {receiver_name}.")
    confirm_pin = input("Enter your PIN to confirm: ").strip()

    if confirm_pin == users[current_user]["pin"]:
        users[current_user]["balance"] -= amount
        users[receiver_id]["balance"] += amount
        print(f"✅ Transfer of ${amount:.2f} to {receiver_name} was successful!")
    else:
        print("❌ Incorrect PIN. Transaction cancelled.")


def main():
    print("=" * 40)
    print("       WELCOME TO PyBANK ATM 🏧")
    print("=" * 40)

    # Allow up to 3 login attempts
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        if check_pin():
            break
        if attempt < max_attempts:
            print(f"   {max_attempts - attempt} attempt(s) remaining.")
    else:
        print("\n🔒 Too many failed attempts. Card blocked. Contact your bank.")
        return

    # Main ATM loop
    while True:
        choice = show_menu()
        if choice == "1":
            withdraw()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            transfer()
        elif choice == "4":
            print(f"\nThank you, {users[current_user]['name']}. Have a great day! 👋")
            break
        else:
            print("❌ Invalid option. Please choose 1–4.")


if __name__ == "__main__":
    main()

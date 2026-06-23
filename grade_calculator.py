# ==============================================
# Grade Calculator
# Author: [Your Name]
# Description: Calculates student letter grades
#              based on numeric scores (0-100).
# ==============================================

def get_grade(score):
    """Return a letter grade based on numeric score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def display_result(name, score, grade):
    """Print a personalized result message."""
    if grade in ('A', 'B'):
        print(f"\n🎉 Congratulations {name}! You scored {score} and got a {grade}!")
    elif grade in ('C', 'D'):
        print(f"\n👍 Good effort {name}! You scored {score} and got a {grade}.")
    else:
        print(f"\n😔 Sorry {name}, you scored {score} and got an F. Keep pushing!")


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    while True:
        name = input("\nEnter student name (or 'quit' to exit): ").strip()
        if name.lower() == 'quit':
            print("\nGoodbye! Keep up the great work. 👋")
            break

        try:
            score = int(input(f"Enter {name}'s score (0 - 100): "))
            if not (0 <= score <= 100):
                print("❌ Invalid score. Please enter a number between 0 and 100.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")
            continue

        grade = get_grade(score)
        display_result(name, score, grade)

        again = input("\nGrade another student? (y/n): ").strip().lower()
        if again != 'y':
            print("\nAll done! Goodbye. 👋")
            break


if __name__ == "__main__":
    main()

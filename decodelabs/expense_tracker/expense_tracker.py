# ============================================================
#  PROJECT  : Expense Tracker
#  FILE     : expense_tracker.py
#  AUTHOR   : Industrial Training Kit - Project 2
#  PURPOSE  : Track multiple expenses and display the total
#             using beginner-friendly Python concepts.
# ============================================================
#
#  CONCEPTS DEMONSTRATED
#  ---------------------
#  1. Accumulator Pattern   - total grows with each addition
#  2. Sentinel Value        - "quit" signals the loop to stop
#  3. Defensive Coding      - try/except handles bad input
#  4. State Management      - `total` tracks program state
#  5. Input-Process-Output  - clear separation of IPO stages
# ============================================================


# ---- STATE MANAGEMENT ---------------------------------------
# Initialize the accumulator to zero before any input is taken.
total = 0           # This variable holds the running expense total


# ---- OUTPUT: Welcome Banner ----------------------------------
print("=" * 45)
print("         [  EXPENSE TRACKER  ]")
print("=" * 45)
print("  Enter your expenses one by one.")
print("  Type  'quit'  when you are done.")
print("=" * 45)
print()


# ---- SENTINEL VALUE + WHILE-TRUE LOOP -----------------------
# We use an infinite loop because we don't know in advance
# how many expenses the user wants to enter.
# The word "quit" acts as the SENTINEL VALUE -- a special
# keyword that tells the program to stop asking for input.

while True:

    # ---- INPUT stage (IPO Model) ----------------------------
    user_input = input("  Enter expense amount: ").strip()

    # Check for the sentinel value
    if user_input.lower() == "quit":
        break       # Exit the loop and move to the output stage

    # ---- DEFENSIVE CODING (try-except ValueError) -----------
    # int() raises ValueError if the input is not a valid number.
    # Instead of letting the program crash, we catch the error
    # and show a helpful message so the user can try again.
    try:
        expense = int(user_input)       # Convert string -> integer

        # Extra guard: disallow negative values
        if expense < 0:
            print("  [!] Expense cannot be negative. Please try again.\n")
            continue                    # Go back to the top of the loop

        # ---- PROCESS stage (IPO Model) - Accumulator Pattern -
        # Add the new expense to the running total.
        # This is the core of the ACCUMULATOR PATTERN.
        total += expense                # Equivalent to: total = total + expense

        print(f"  [+] Rs.{expense} added.  Running total: Rs.{total}\n")

    except ValueError:
        # Triggered when the user types something like "abc" or "12.5"
        print("  [X] Invalid input! Please enter a whole number (e.g., 500).\n")


# ---- OUTPUT stage (IPO Model) --------------------------------
# After the loop ends (user typed "quit"), display the final total.
print()
print("=" * 45)
print(f"  >> Total Expenses : Rs.{total}")
print("=" * 45)
print("  Thank you for using Expense Tracker!")
print("=" * 45)

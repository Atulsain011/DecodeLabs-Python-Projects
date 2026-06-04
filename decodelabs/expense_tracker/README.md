# ============================================================
#  PROJECT  : Expense Tracker
#  FILE     : README.md
#  SECTION  : Industrial Training Kit – Project 2
# ============================================================

# 💰 Expense Tracker — Project 2

> **Industrial Training Kit | Beginner Python Series**
> A clean, beginner-friendly console application that lets you
> track daily expenses and calculates the total automatically.

---

## 📁 Project Structure

```
task2/
├── expense_tracker.py   ← Main program file
└── README.md            ← Project documentation (this file)
```

---

## 🚀 How to Run

```bash
python expense_tracker.py
```

---

## 📖 Step-by-Step Explanation

### Step 1 — Initialize the Accumulator
```python
total = 0
```
We set `total` to **zero** before the loop starts. This is the
**Accumulator Pattern** — a variable that grows as we add values to it.

---

### Step 2 — Start the Infinite Loop
```python
while True:
```
We use `while True` because we don't know in advance how many
expenses the user will enter. The loop runs **forever** until
we explicitly `break` out of it.

---

### Step 3 — Read User Input
```python
user_input = input("Enter expense amount: ").strip()
```
`input()` reads whatever the user types as a **string**.
`.strip()` removes any accidental leading/trailing spaces.

---

### Step 4 — Check the Sentinel Value
```python
if user_input.lower() == "quit":
    break
```
**Sentinel Value** = a special keyword that signals "I'm done."
When the user types `quit` (any case), `break` exits the loop.

---

### Step 5 — Convert & Validate with try-except
```python
try:
    expense = int(user_input)
except ValueError:
    print("❌ Invalid input! Please enter a whole number.")
```
`int()` converts the string to an integer. If the user types
letters or decimals, Python raises a **ValueError**. The
`except` block catches it gracefully — **Defensive Coding**.

---

### Step 6 — Add to the Total (Accumulator Pattern)
```python
total += expense
```
`+=` is shorthand for `total = total + expense`. Every valid
expense is accumulated into `total` — **State Management** in action.

---

### Step 7 — Display the Final Total
```python
print(f"Total Expenses : Rs.{total}")
```
After the loop ends, we print the accumulated total —
the **Output** stage of the **Input → Process → Output** model.

---

## 🖥️ Sample Input / Output

```
=============================================
       💰  EXPENSE TRACKER  💰
=============================================
Enter your expenses one by one.
Type  'quit'  when you are done.

Enter expense amount: 200
   ✔  Rs.200 added.  Running total: Rs.200

Enter expense amount: 450
   ✔  Rs.450 added.  Running total: Rs.650

Enter expense amount: abc
❌  Invalid input! Please enter a whole number (e.g., 500).

Enter expense amount: -50
⚠  Expense cannot be negative. Please try again.

Enter expense amount: 300
   ✔  Rs.300 added.  Running total: Rs.950

Enter expense amount: quit

=============================================
   🧾  Total Expenses : Rs.950
=============================================
   Thank you for using Expense Tracker! 👋
=============================================
```

---

## 🧠 Concepts Used

| # | Concept | Where Used |
|---|---------|------------|
| 1 | **Accumulator Pattern** | `total += expense` — grows with each addition |
| 2 | **Sentinel Value** | `"quit"` signals the end of input |
| 3 | **Defensive Coding** | `try/except ValueError` — handles bad input |
| 4 | **State Management** | `total` tracks the running state |
| 5 | **Input-Process-Output (IPO)** | `input()` → `int() + +=` → `print()` |

---

## ⚙️ Python Features Used

- `while True` loop — infinite loop with controlled exit
- `break` — exits the loop when sentinel is encountered
- `continue` — skips the current iteration (negative check)
- `try / except ValueError` — handles conversion errors
- `int()` — converts string input to integer
- f-strings — clean, readable output formatting
- `.strip()` / `.lower()` — input normalization

---

## ✅ Key Learning Outcomes

After completing this project you will understand:

1. How to use a **while loop** for repeated user input
2. How the **accumulator pattern** works in real programs
3. Why **defensive coding** (error handling) is essential
4. What a **sentinel value** is and why it's more flexible than counting loops
5. How programs follow the **Input → Process → Output** model

---

*Industrial Training Kit — Python Beginner Series | Project 2*

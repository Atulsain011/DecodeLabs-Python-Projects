# 🚀 TO-DO LIST & TASK MANAGEMENT SYSTEM

A feature-rich, modular, and colorful Command-Line Interface (CLI) application built for task management. This project demonstrates backend logic, file persistence, and professional terminal UI design in Python.

## ✨ Features
- **Clean UI**: Uses ASCII banners and `colorama` for a premium look.
- **Task Management**: Add, View, Mark as Completed, and Delete tasks.
- **Priority System**: Categorize tasks as High, Medium, or Low with color coding.
- **Persistence**: Automatically saves tasks to a `tasks.json` file.
- **Search**: Fast case-insensitive task search.
- **Input Validation**: Robust handling of empty inputs and incorrect data types.
- **Modular Code**: Separated backend logic (`task_manager.py`) from frontend UI (`main.py`).

## 📁 Project Structure
```text
todo/
├── main.py            # CLI Interface & User Interaction
├── task_manager.py     # Core Logic, File I/O, & CRUD Operations
├── requirements.txt    # Project Dependencies
├── tasks.json         # Data storage (Auto-generated)
└── README.md          # Documentation
```

## 🛠️ Installation & Usage

1. **Clone the project** or copy the files into a folder.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```

## 🧠 Python Concepts Covered
- **Functions**: Modularizing code for reusability.
- **Data Structures**: Using Lists and Dictionaries to store complex task data.
- **File Handling**: Reading and writing JSON files for data persistence.
- **Exception Handling**: Using `try-except` blocks to prevent crashes.
- **List Comprehension**: Efficient data filtering and manipulation.
- **Module Imports**: Organizing code across multiple files.

## 🚀 Future Improvements
- [ ] Add due dates for tasks.
- [ ] Filter tasks by priority or status.
- [ ] Implement a Category/Tag system.
- [ ] Export task list to CSV or PDF.

---
*Created for Python Internship Portfolio - 2026*

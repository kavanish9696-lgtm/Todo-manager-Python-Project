# Todo-manager-Python-Project
# 📋 To-Do List Manager (Group 12)

A modular, robust, menu-driven Python Command-Line Interface (CLI) application for task management. This project demonstrates core and advanced Python programming principles, including structured data types (dictionaries, tuples, sets, lists), file persistence, recursive algorithms, defensive user input validation, nested loops, and automated unit testing using doctests.

---

## 👥 Project Contributors & Module Distribution

| Part | Contributor | Module / Responsibility | Core Topics Covered |
| :--- | :--- | :--- | :--- |
| **Part 1** | **Manasvi Saharawat** | Constants, Validation, Math & Recursion | Constants, Tuples, String sanitization (`strip`, `title`), Date validation, Float math, Recursion (`count_pending`), Doctests |
| **Part 2** | **Aayush Kumar** | File Handling, Persistence & Sets | Context managers (`with open`), File parsing (`\|` delimiter), Error handling (`FileNotFoundError`, `ValueError`), Sets (`categories`) |
| **Part 3** | **Avanish Kumar ** | CRUD Operations, Search & Table Display | Dictionary CRUD, Tuple immutability, List operations (`sort`, slicing, `remove`), Keyword search, Formatted output, Nested loops |
| **Part 4** | **Prashant** | Menu Controller & System Integration | Interactive event loop (`while True`), Menu logic (`if-elif-else`), System coordination, Auto-persistence, Graceful exit |

---

## 📁 Repository Structure

```text
Todo-manager-Python-Project
├── todo_manager.py       # Consolidated, fully integrated executable application
├── part1_manasvi.py      # Part 1: Validation routines, recursive stats, and doctests
├── part2_aayush.py       # Part 2: File reading/writing and category set management
├── part3_avanish.py      # Part 3: Task CRUD operations, search, and priority table display
├── part4_prashant.py     # Part 4: Interactive menu controller and integration
├── tasks.txt             # Persistent storage file for all task records
└── README.md             # Project documentation and user manual
```

---

## ⚙️ Features & Functionalities

### 1. Task Management (CRUD)
- **Add Tasks**: Assign a title, priority level (`High`, `Medium`, `Low`), category (e.g., `Study`, `Work`, `Personal`, `Health`), and an optional due date (`YYYY-MM-DD`).
- **Mark as Done**: Safely updates task status from `Pending` to `Done` while preserving tuple integrity.
- **Edit Tasks**: Modify title, priority, category, or due date for any existing task with fallback defaults (press Enter to keep existing value).
- **Delete Task**: Remove a specific task permanently by ID.
- **Clear Completed Tasks**: Batch delete all finished tasks with user confirmation.

### 2. Search & Filter
- **Keyword Search**: Case-insensitive substring search across task titles.
- **Status Filters**: View only pending tasks, only completed tasks, or all tasks.

### 3. Display & Reporting
- **Priority-Grouped Table**: Uses nested loops to cleanly display tasks grouped under `High`, `Medium`, and `Low` priority headings with aligned column formatting.
- **Recursive Task Statistics**:
  - Counts pending tasks using a **recursive algorithm** (`count_pending`) with list slicing and a base case.
  - Calculates completion percentage rounded to 1 decimal place.

### 4. Persistence & Data Safety
- Reads from and writes to `tasks.txt` using a pipe-delimited (`|`) format.
- Automatically saves data after every modification and upon exit.
- Sanitizes input to prevent delimiter injection (rejects `|` in titles and categories).
- Gracefully handles missing files, empty lines, and malformed records.

---

## 💾 Data Storage Format (`tasks.txt`)

Tasks are stored in plain text with the following pipe-delimited schema:

```text
ID|Title|Priority|Status|Category|DueDate
```


---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher installed on your system.
- Standard Library only (no third-party dependencies required).

### Running the Application

To run the complete, consolidated program:

```bash
python todo_manager.py
```

### Running Doctests

To run the automated tests embedded in the validation and recursion module:

```bash
python part1_manasvi.py
```

All doctest assertions (`clean_title`, `is_valid_priority`, `is_valid_date`, `percent_done`, `count_pending`) will execute and print their pass/fail status in verbose mode.

---

## 🖥️ Interactive Menu Overview

When you launch `todo_manager.py`, the following menu is presented:

```text
====================================
    TO-DO LIST MANAGER (GROUP 12)
====================================
1.  Add Task (with Due Date)
2.  Mark Task as Done
3.  Edit Task
4.  Delete Task
5.  View All Tasks (by Priority)
6.  View Pending Tasks
7.  View Completed Tasks
8.  Show Pending Count & Stats
9.  Search Tasks by Keyword  [NEW]
10. Clear Completed Tasks     [NEW]
11. Exit
====================================
```

---

## 🧠 Python Concepts & Highlights

1. **Tuples & Immutability**: Tasks are stored as tuples `(task_id, title, priority, status, category, due_date)` to ensure record immutability once created. Updates construct a fresh tuple.
2. **Dictionaries**: Tasks are indexed by their unique integer ID (`tasks[task_id]`), providing $O(1)$ lookups for edits, deletions, and status toggles.
3. **Sets**: Categories are tracked in a `set` to automatically guarantee uniqueness and dynamic category discovery.
4. **Recursion**: `count_pending(task_list)` uses structural recursion (`first_task` + `count_pending(task_list[1:])`) with base condition `len(task_list) == 0`.
5. **Defensive Programming**: All user inputs (integers, strings, dates) are wrapped in validation loops with informative error prompts to prevent unhandled runtime exceptions.
6. **File I/O**: Safe reading and writing using Python context managers (`with open(...)`) and exception trapping (`FileNotFoundError`, `ValueError`, `IOError`).

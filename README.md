# 📋 To-Do List Manager (Group 12)

A simple **Python** program that runs in the terminal and helps you keep track of your daily tasks. You can add tasks, mark them done, edit them, delete them, and see them sorted by priority. All tasks are saved in a file, so they are still there when you run the program again.

This is a college project made by **Group 12**.

---

## 👥 Group Members

| Name | Roll No. | Part of the project |
| --- | --- | --- |
| Manasvi Saharawat | 202610101200024 | Validation, math and recursion |
| Aayush Kumar | 202610101200018 | File handling and categories |
| Avanish Kumar | 202610101200012 | Add / edit / delete tasks, search and table display |
| Prashant | 202610101200060 | Menu and joining all parts together |

---

## ✨ What can it do?

- ➕ **Add a task** with a title, priority (High / Medium / Low), category and due date
- ✅ **Mark a task as done**
- ✏️ **Edit a task** (press Enter to keep the old value)
- 🗑️ **Delete a task** using its ID
- 📃 **View tasks** – all, only pending, or only completed (sorted by priority)
- 🔢 **See how many tasks are pending** and what percent is done
- 🔍 **Search** tasks by a keyword
- 🧹 **Clear all completed tasks**
- 💾 **Auto-save** to a file (`tasks.txt`)

---

## 🛠️ What you need

- Python 3.7 or newer
- Nothing else to install (only Python's built-in features are used)

---

## 🚀 How to run

1. Download or clone this repository:
   ```
   git clone https://github.com/kavanish9696-lgtm/Todo-manager-Python-Project.git
   ```
2. Open the project folder in your terminal.
3. Run the program:
   ```
   python todo_manager.py
   ```

---

## 🖥️ Menu

When you run the program, you will see this menu. Type the number of the option you want.

```
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
9.  Search Tasks by Keyword
10. Clear Completed Tasks
11. Exit
====================================
```

---

## 💾 How tasks are saved

Tasks are saved in a text file called `tasks.txt`. Each task is one line, with parts separated by `|`:

```
ID|Title|Priority|Status|Category|DueDate
```

Example:

```
1|Finish Python assignment|High|Pending|Study|2026-11-30
```

> Because `|` is used to separate the parts, please don't use `|` in a task title or category.

---

## 📚 Python topics used in this project

- Variables, strings and operators
- Lists, tuples, dictionaries and sets
- `if / elif / else` and loops (including nested loops)
- Functions
- Recursion (to count pending tasks)
- File handling (`with open`)
- Exception handling (`try / except`)
- Doctests (to test small functions)

---

## 📁 Files in this repository

| File | What it is |
| --- | --- |
| `todo_manager.py` | The main program – run this one |
| `README.md` | This file |
| `tasks.txt` | Created automatically when you add your first task (your saved tasks) |

---

Made with ❤️ by Group 12

**• Manasvi Saharawat • Avanish Kumar • Aayush Kumar • Prashant**

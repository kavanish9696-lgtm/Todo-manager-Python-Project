
# ============================================================
# PART 1: CONSTANTS, VALIDATION, MATH AND RECURSION
# ============================================================
# 1. GLOBAL CONSTANTS
PRIORITIES = ("High", "Medium", "Low") # Fixed tuple defining priority hierarchy
FILE_NAME = "tasks.txt"
STATUS_PENDING = "Pending" 
STATUS_DONE = "Done"
STATUSES = (STATUS_PENDING, STATUS_DONE)
DEFAULT_CATEGORIES = {"Study", "Personal", "Work", "Health"} # Initial category set
QUIT_REQUESTED = False

def get_input(prompt):
    global QUIT_REQUESTED
    answer = input(prompt)

    if answer.strip().lower() == "quit":
        QUIT_REQUESTED = True
        return ""

    return answer
# 2. VALIDATE TASK TITLE (asks again until valid)
def validate_title():
    while True:
        title = input("Enter task title: ").strip()
        if title == "":
            print("Title cannot be empty. Please try again.")
            continue
        if "|" in title:
            print("Invalid character '|' in title. Please try again.")
            continue
        print("Valid title:", title)
        return title


# 3. VALIDATE CATEGORY (asks again until valid)
def validate_category():
    while True:
        category = input("Enter task category: ").strip().title()
        if category == "":
            print("Category cannot be empty. Please try again.")
            continue
        if "|" in category:
            print("Invalid character '|' in category. Please try again.")
            continue
        print("Valid category:", category)
        return category


# 4. VALIDATE PRIORITY (asks again until valid)
def validate_priority():
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().title()
        if priority in PRIORITIES:
            print("Valid priority:", priority)
            return priority
        print("Invalid priority. Enter High, Medium or Low.")


# 5. VALIDATE DATE (asks again until valid)
def validate_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        parts = date.split("-")
        if len(parts) != 3:
            print("Invalid date format. Use YYYY-MM-DD.")
            continue
        year, month, day = parts
        if not year.isdigit():
            print("Invalid year.")
            continue
        if not month.isdigit():
            print("Invalid month.")
            continue
        if not day.isdigit():
            print("Invalid day.")
            continue
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            print("Use YYYY-MM-DD format.")
            continue
        year = int(year)
        month = int(month)
        day = int(day)
        if year < 1 or month < 1 or month > 12:
            print("Invalid date.")
            continue

        # CHECK LEAP YEAR
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap_year = True
        else:
            leap_year = False
        days = [31, 29 if leap_year else 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
        if day < 1 or day > days[month - 1]:
            print("Invalid day for this month.")
            continue
        print("Valid date:", date)
        return date


# 6. COUNT PENDING TASKS USING RECURSION
def count_pending(tasks):
    """Count pending tasks from the task records using recursion."""
    def count_recursive(task_list):
        if task_list == []:
            return 0
        count = 0
        if task_list[0][3] == STATUS_PENDING:
            count = 1
        return count + count_recursive(task_list[1:])

    return count_recursive(tasks)


# 7. CALCULATE PERCENTAGE OF COMPLETED TASKS
def calculate_percent_done(pending, total):
    if total == 0:
        print("No tasks available.")
        return 0
    completed = total - pending
    percentage = (completed / total) * 100
    percentage = round(percentage, 1)
    print("Completed tasks:", completed)
    print("Completion percentage:", percentage, "%")
    return percentage
"""
PART 2: FILE HANDLING, STORAGE & SETS
Student Name: Aayush Kumar (Group 12)
File: part2_aayush.py
"""
def load_tasks(filename, categories):
    """Load tasks from file into a dictionary; add categories to the set."""
    tasks = {}

    # append mode me file na ho to ban jati hai, isliye aage read me error nahi aata
    file = open(filename, "a")
    file.close()

    file = open(filename, "r")
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line == "":
            continue

        parts = cleaned_line.split("|")
        # 5 fields (old file) or 6 fields (with due date)
        if len(parts) < 5 or len(parts) > 6:
            print(f"Warning: Skipping malformed line -> {cleaned_line}")
            continue

        if not parts[0].strip().isdigit():
            print(f"Warning: Non-integer ID in line -> {cleaned_line}")
            continue

        task_id = int(parts[0])
        title = parts[1].strip()
        priority = parts[2].strip()
        status = parts[3].strip()
        category = parts[4].strip()
        due_date = "No Date"
        if len(parts) == 6:
            due_date = parts[5].strip()

        if priority not in PRIORITIES or status not in STATUSES:
            print(f"Warning: Invalid priority/status in line -> {cleaned_line}")
            continue

        tasks[task_id] = (task_id, title, priority, status, category, due_date)
        categories.add(category)
    file.close()

    print(f"Loaded {len(tasks)} task(s) from '{filename}'.")
    return tasks


def save_tasks(filename, tasks):
    """Save all tasks to file, one task per line, joined with '|'."""
    id_list = []
    for task_id in tasks:
        id_list.append(task_id)
    id_list.sort()

    file = open(filename, "w")
    for task_id in id_list:
        task = tasks[task_id]
        file.write("|".join([str(task[0]), task[1], task[2], task[3], task[4], task[5]]) + "\n")
    file.close()
    return len(tasks)
"""
PART 3: TASK OPERATIONS, SEARCH & NESTED LOOPS TABLE
Student Name: Avanish Kar (Group 12)
File: part3_avanish.py
"""

def clean_title(raw_title):
    """Remove extra spaces and reject empty titles or the file separator."""
    title = raw_title.strip()
    if title == "" or "|" in title:
        return ""
    return title


def is_valid_priority(raw_priority):
    """Return the correctly formatted priority, or an empty string."""
    priority = raw_priority.strip().title()
    if priority in PRIORITIES:
        return priority
    return ""


def is_valid_date(raw_date):
    """Check YYYY-MM-DD using the same date and leap-year logic as Part 1."""
    parts = raw_date.split("-")
    if len(parts) != 3:
        return False
    year, month, day = parts
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 1 or month < 1 or month > 12:
        return False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False
    days = [31, 29 if leap_year else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    if day < 1 or day > days[month - 1]:
        return False
    return True


def get_valid_id(prompt_msg, tasks):
    """Ask for a task ID until an existing one is entered."""
    while True:
        raw = input(prompt_msg).strip()
        if raw == "":
            print("Error: ID cannot be empty. Please enter a valid number.")
            continue
        if not raw.isdigit():
            print("Error: Invalid input. ID must be an integer (e.g. 1, 2, 3).")
            continue
        task_id = int(raw)
        if task_id not in tasks:
            print(f"Error: Task ID {task_id} does not exist in the list. Please try again.")
            continue
        return task_id


def get_valid_priority():
    """Ask until a valid priority is entered."""
    while True:
        print("Available Priorities: " + ", ".join(PRIORITIES))
        priority = is_valid_priority(input("Enter priority (High/Medium/Low): "))
        if priority != "":
            return priority
        print("Error: Invalid priority. Please choose High, Medium, or Low.")


def get_valid_category(categories):
    """Choose an existing category or type a new one."""
    while True:
        category_list = list(categories)
        category_list.sort()
        print("Known Categories: " + ", ".join(category_list))
        raw = input("Enter category (or type a new one): ").strip()
        if raw == "":
            print("Error: Category cannot be empty. Please try again.")
            continue
        if "|" in raw:
            print("Error: Category name cannot contain '|'. Please try again.")
            continue
        formatted_cat = raw.title()
        categories.add(formatted_cat)
        return formatted_cat


def get_valid_date():
    """Ask for due date (YYYY-MM-DD) or Enter to skip."""
    while True:
        raw = input("Enter due date (YYYY-MM-DD) or press Enter for 'No Date': ").strip()
        if raw == "":
            return "No Date"
        if is_valid_date(raw):
            return raw
        print("Error: Invalid date format! Please enter in YYYY-MM-DD format (e.g. 2026-11-25).")


def add_task(tasks, categories):
    """Add a new task."""
    print("\n--- Add New Task ---")
    while True:
        raw_title = input("Enter task title: ")
        title = clean_title(raw_title)
        if title != "":
            break
        if "|" in raw_title:
            print("Error: Title cannot contain the '|' character.")
        else:
            print("Error: Title cannot be empty. Please try again.")

    priority = get_valid_priority()
    category = get_valid_category(categories)
    due_date = get_valid_date()

    # new ID = highest existing ID + 1 (starts from 1)
    new_id = 1
    for tid in tasks:
        if tid >= new_id:
            new_id = tid + 1

    task_tuple = (new_id, title, priority, STATUS_PENDING, category, due_date)
    tasks[new_id] = task_tuple

    print(f"Success: Task #{new_id} '{title}' due on {due_date} added successfully!")
    return task_tuple


def mark_done(tasks):
    """Mark a pending task as Done."""
    print("\n--- Mark Task as Done ---")
    if len(tasks) == 0:
        print("Notice: No tasks available.")
        return False

    print("\nHere are your tasks and their IDs:")
    show_tasks(tasks, None)
    task_id = get_valid_id("Enter Task ID to mark as done: ", tasks)
    task = tasks[task_id]
    if task[3] == STATUS_DONE:
        print(f"Notice: Task #{task_id} is already marked as Done.")
        return False

    # tuple cannot be changed, so make a new tuple
    tasks[task_id] = (task[0], task[1], task[2], STATUS_DONE, task[4], task[5])
    print(f"Success: Task #{task_id} ('{task[1]}') marked as Done!")
    return True


def edit_task(tasks, categories):
    """Edit title, priority, category or due date of a task."""
    print("\n--- Edit Task ---")
    if len(tasks) == 0:
        print("Notice: No tasks available to edit.")
        return False

    print("\nHere are your tasks and their IDs:")
    show_tasks(tasks, None)
    task_id = get_valid_id("Enter Task ID to edit: ", tasks)
    task = tasks[task_id]
    print(f"Current task: Title='{task[1]}', Priority='{task[2]}', Status='{task[3]}', Category='{task[4]}', Due Date='{task[5]}'")

    while True:  # title
        raw_title = input(f"Enter new title (press Enter to keep '{task[1]}'): ")
        if raw_title.strip() == "":
            new_title = task[1]
            break
        new_title = clean_title(raw_title)
        if new_title != "":
            break
        print("Error: Invalid title or contains '|'. Please try again.")

    while True:  # priority
        raw_priority = input(f"Enter new priority (press Enter to keep '{task[2]}'): ").strip()
        if raw_priority == "":
            new_priority = task[2]
            break
        new_priority = is_valid_priority(raw_priority)
        if new_priority != "":
            break
        print("Error: Priority must be High, Medium, or Low.")

    while True:  # category
        raw_cat = input(f"Enter new category (press Enter to keep '{task[4]}'): ").strip()
        if raw_cat == "":
            new_category = task[4]
            break
        if "|" in raw_cat:
            print("Error: Category cannot contain '|'. Please try again.")
            continue
        new_category = raw_cat.title()
        categories.add(new_category)
        break

    while True:  # due date
        raw_date = input(f"Enter new due date (YYYY-MM-DD) (press Enter to keep '{task[5]}'): ").strip()
        if raw_date == "":
            new_date = task[5]
            break
        if is_valid_date(raw_date):
            new_date = raw_date
            break
        print("Error: Invalid date! Please use YYYY-MM-DD format.")

    tasks[task_id] = (task[0], new_title, new_priority, task[3], new_category, new_date)
    print(f"Success: Task #{task_id} updated successfully!")
    return True


def delete_task(tasks):
    """Delete a task by ID."""
    print("\n--- Delete Task ---")
    print("Note: You can delete only one task at a time.")
    if len(tasks) == 0:
        print("Notice: No tasks available to delete.")
        return False

    print("\nHere are your tasks and their IDs:")
    show_tasks(tasks, None)
    task_id = get_valid_id("Enter Task ID to delete: ", tasks)
    deleted_task = tasks[task_id]
    del tasks[task_id]
    print(f"Success: Task #{task_id} ('{deleted_task[1]}') deleted successfully!")
    return True


def clear_completed_tasks(tasks):
    """Delete all completed tasks at once."""
    print("\n--- Clear Completed Tasks ---")
    completed_ids = []
    for tid in tasks:
        if tasks[tid][3] == STATUS_DONE:
            completed_ids.append(tid)

    if len(completed_ids) == 0:
        print("Notice: There are no completed tasks to clear.")
        return False

    confirm = input(f"Are you sure you want to delete all {len(completed_ids)} completed task(s)? (y/n): ").strip().lower()
    if confirm != "y":
        print("Operation cancelled. No tasks were deleted.")
        return False

    for tid in completed_ids:
        del tasks[tid]
    print(f"Success: Cleared {len(completed_ids)} completed task(s)!")
    return True


def search_tasks(tasks):
    """Search tasks by title keyword."""
    print("\n--- Search Tasks by Keyword ---")
    if len(tasks) == 0:
        print("Notice: Task list is empty.")
        return 0

    keyword = input("Enter search keyword (e.g. 'hw', 'lab', 'gym'): ").strip().lower()
    if keyword == "":
        print("Notice: Search keyword was empty.")
        return 0

    matching_tasks = {}
    for tid in tasks:
        if keyword in tasks[tid][1].lower():
            matching_tasks[tid] = tasks[tid]

    if len(matching_tasks) == 0:
        print(f"No tasks found matching keyword '{keyword}'.")
        return 0

    print(f"\nFound {len(matching_tasks)} matching task(s):")
    return show_tasks(matching_tasks, None)


def show_tasks(tasks, filter_status=None):
    """Show tasks in a table, grouped by priority (nested loops)."""
    if len(tasks) == 0:
        print("\nNotice: Task list is empty.")
        return 0

    # tasks to show, in ID order (all tasks, or only the given status)
    id_list = []
    for tid in tasks:
        id_list.append(tid)
    id_list.sort()

    display_list = []
    for tid in id_list:
        if filter_status == None or tasks[tid][3] == filter_status:
            display_list.append(tasks[tid])

    if len(display_list) == 0:
        print(f"\nNotice: No tasks found matching status '{filter_status}'.")
        return 0

    print("\n" + "=" * 78)
    print(f"{'ID':<5} {'Title':<25} {'Priority':<9} {'Status':<9} {'Category':<12} {'Due Date':<11}")
    print("=" * 78)

    count = 0
    # NESTED LOOPS: outer = priorities, inner = tasks
    for p in PRIORITIES:
        for task in display_list:
            if task[2] == p:
                tid, title, priority, status, category, due_date = task
                print(f"{tid:<5} {title:<25} {priority:<9} {status:<9} {category:<12} {due_date:<11}")
                count = count + 1

    print("=" * 78)
    print(f"Total tasks shown: {count}")
    return count


"""
PART 4: MAIN MENU
Student Name: Prashant (Group 12)
File: part4_prashant.py
"""


def main():
    """Main menu loop."""
    categories = set(DEFAULT_CATEGORIES)
    tasks = load_tasks(FILE_NAME, categories)

    while True:
        print("\n" + "=" * 36)
        print("    TO-DO LIST MANAGER (GROUP 12)")
        print("=" * 36)
        print("""1.  Add Task (with Due Date)
2.  Mark Task as Done
3.  Edit Task
4.  Delete Task
5.  View All Tasks (by Priority)
6.  View Pending Tasks
7.  View Completed Tasks
8.  Show Pending Count & Stats
9.  Search Tasks by Keyword  [NEW]
10. Clear Completed Tasks     [NEW]
11. Exit""")
        print("=" * 36)

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_task(tasks, categories)
            save_tasks(FILE_NAME, tasks)
        elif choice == "2":
            if mark_done(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "3":
            if edit_task(tasks, categories):
                save_tasks(FILE_NAME, tasks)
        elif choice == "4":
            if delete_task(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "5":
            show_tasks(tasks, None)
        elif choice == "6":
            show_tasks(tasks, STATUS_PENDING)
        elif choice == "7":
            show_tasks(tasks, STATUS_DONE)
        elif choice == "8":
            task_list = []
            for tid in tasks:
                task_list.append(tasks[tid])
            pending_num = count_pending(task_list)
            total_num = len(tasks)

            print("\n--- Task Statistics ---")
            print(f"Total Tasks     : {total_num}")
            print(f"Pending Tasks   : {pending_num} (calculated via recursion)")
            calculate_percent_done(pending_num, total_num)
        elif choice == "9":
            search_tasks(tasks)
        elif choice == "10":
            if clear_completed_tasks(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "11":
            save_tasks(FILE_NAME, tasks)
            print("\nAll tasks saved successfully. Thank you for using To-Do List Manager! Goodbye.")
            break
        else:
            print("Error: Invalid choice! Please enter a number between 1 and 11.")


main()

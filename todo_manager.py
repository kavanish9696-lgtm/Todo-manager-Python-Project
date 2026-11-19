

# PART 1: CONSTANTS, VALIDATION, MATH & RECURSION
# Student Name: Manasvi Saharawat
# Group: 12
# File: part1_manasvi.py


# 1. GLOBAL CONSTANTS

PRIORITIES = ("High", "Medium", "Low")

STATUSES = ("Pending", "Done")


# 2. VALIDATE TASK TITLE

def validate_title(title):

    title = title.strip()

    if title == "" or "|" in title:
        return None

    return title


# 3. VALIDATE CATEGORY

def validate_category(category):

    category = category.strip().title()

    if category == "" or "|" in category:
        return None

    return category


# 4. VALIDATE PRIORITY

def validate_priority(priority):

    priority = priority.strip().title()

    if priority in PRIORITIES:
        return priority

    else:
        return None


# 5. VALIDATE DATE

def validate_date(date):

    parts = date.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1 or month < 1 or month > 12:
        return False

    # Check leap year

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False

    # Number of days in each month

    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if leap_year:
        days[1] = 29

    if day < 1 or day > days[month - 1]:
        return False

    return True


# 6. COUNT PENDING TASKS USING RECURSION

def count_pending(tasks):

    # Base case

    if len(tasks) == 0:
        return 0

    # Check first task

    if tasks[0][3] == "Pending":
        count = 1
    else:
        count = 0

    # Recursive call

    return count + count_pending(tasks[1:])


# 7. CALCULATE COMPLETION PERCENTAGE

def calculate_percent_done(tasks):

    total_tasks = len(tasks)

    if total_tasks == 0:
        return 0.0

    pending = count_pending(tasks)

    completed = total_tasks - pending

    percentage = (completed / total_tasks) * 100

    return round(percentage, 1)


# END OF PART 


def load_tasks(filename, categories):
    """Load tasks from text file into a dictionary; add loaded categories to set."""
    tasks = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line == "":
                    continue

                parts = cleaned_line.split("|")
                # Supports both 5-field (legacy) and 6-field (with due date) files
                if len(parts) < 5 or len(parts) > 6:
                    print(f"Warning: Skipping malformed line -> {cleaned_line}")
                    continue

                try:
                    task_id = int(parts[0])
                except ValueError:
                    print(f"Warning: Non-integer ID in line -> {cleaned_line}")
                    continue

                title = parts[1].strip()
                priority = parts[2].strip()
                status = parts[3].strip()
                category = parts[4].strip()

                if len(parts) == 6:
                    due_date = parts[5].strip()
                else:
                    due_date = "No Date"

                if priority not in PRIORITIES or status not in STATUSES:
                    print(f"Warning: Invalid priority/status in line -> {cleaned_line}")
                    continue

                # Store task as 6-element tuple in dictionary
                tasks[task_id] = (task_id, title, priority, status, category, due_date)
                # Add category to unique set
                categories.add(category)

        print(f"Loaded {len(tasks)} task(s) from '{filename}'.")
    except FileNotFoundError:
        print(f"Notice: '{filename}' not found. Starting with an empty task list.")

    return tasks


def save_tasks(filename, tasks):
    """Save all tasks from dictionary to text file using '|' delimiter."""
    try:
        with open(filename, "w") as file:
            for task_id in sorted(tasks.keys()):
                task = tasks[task_id]
                # Convert tuple items to string and join with '|'
                record = [str(task[0]), task[1], task[2], task[3], task[4], task[5]]
                line = "|".join(record)
                file.write(line + "\n")
        return len(tasks)
    except IOError as e:
        print(f"Error saving to file: {e}")
        return -1

      
      
"""
PART 3: TASK CRUD OPERATIONS, SEARCH & NESTED LOOPS TABLE
Student Name: Avanish Kumar (Group 12)
"""
"""
Topics Covered:
  - Input validation & crash prevention (get_valid_id, get_valid_priority, get_valid_category, get_valid_date)
  - Dictionary operations (insert, update, delete with `del`, lookup)
  - Tuple immutability (creating updated tuples for modified tasks)
  - List algorithms (id_list.sort(), display_list.remove(), list slicing copy [:])
  - Nested Loops (outer loop over PRIORITIES, inner loop over display_list)
  - Formatted output (f-string table column alignments)
  - String search & membership operators (keyword in title.lower())
"""
def get_valid_id(prompt_msg,tasks):
    """prompt user for a valid task ID that exist in the task dictionary."""
    while True:
        raw = input(prompt_msg).strip()
        if raw == "":
            print("Error: Invalid input. ID must be an integer(e.g. 1, 2, 3).")
            continue
        try:
            task_id = int(raw)
        except ValueError:
            print("Error: Invalid input. ID must be an integer (e.g. 1, 2, 3.)")
            continue
        if task_id not in tasks:
            print(f"Error: Task ID {task_id} does not exist in the list. Please try again!.")
            continue
        return task_id 

def get_valid_priority():
    "prompt user until a valid priority (High, Medium, or Low) is entered. "
    while True:
        print("Available Priorities: " + ", ".join(PRIORITIES))
        raw = input("Enter priority (High/Medium/Low): ")
        priority = is_valid_priority(raw)
        if priority != "":
            return priority
        print("Error: Invalid priority. Please Choose High, Medium, Low.")


def get_valid_category(categories):
    """Prompt user to choose an existing category or enter a new one."""
    while True:
        category_list = sorted(list(categories))
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
    """Prompt user for a due date in YYYY-MM-DD format, or press Enter to skip."""
    while True:
        raw = input("Enter due date (YYYY-MM-DD) or press Enter for 'No Date': ").strip()
        if raw == "":
            return "No Date"
        if is_valid_date(raw):
            return raw
        print("Error: Invalid date format! Please enter in YYYY-MM-DD format (e.g. 2026-11-25).")

def add_task(tasks, categories):
    """Add a new task with priority, status, category, and due date."""
    print("\n--- Add New Task ---")
    while True:
        raw_title = input("Enter task title: ")
        title = clean_title(raw_title)
        if title == "":
            if "|" in raw_title:
                print("Error: Title cannot contain the '|' character.")
            else:
                print("Error: Title cannot be empty. Please try again.")
            continue
        break

    priority = get_valid_priority()
    category = get_valid_category(categories)
    due_date = get_valid_date()

    if len(tasks) == 0:
        new_id = 1
    else:
        highest_id = 0
        for tid in tasks:
            if tid > highest_id:
                highest_id = tid
        new_id = highest_id + 1

    status = STATUS_PENDING
    task_tuple = (new_id, title, priority, status, category, due_date)
    tasks[new_id] = task_tuple

    print(f"Success: Task #{new_id} '{title}' due on {due_date} added successfully!")
    return task_tuple


def mark_done(tasks):
    """Mark an existing pending task as 'Done'."""
    print("\n--- Mark Task as Done ---")
    if len(tasks) == 0:
        print("Notice: No tasks available.")
        return False

    task_id = get_valid_id("Enter Task ID to mark as done: ", tasks)
    task = tasks[task_id]

    if task[3] == STATUS_DONE:
        print(f"Notice: Task #{task_id} is already marked as Done.")
        return False

    # Tuples are immutable, so we create a new tuple keeping due date intact
    updated_task = (task[0], task[1], task[2], STATUS_DONE, task[4], task[5])
    tasks[task_id] = updated_task

    print(f"Success: Task #{task_id} ('{task[1]}') marked as Done!")
    return True


def mark_done(tasks):
    """Mark an existing pending task as 'Done'."""
    print("\n--- Mark Task as Done ---")
    if len(tasks) == 0:
        print("Notice: No tasks available.")
        return False

    task_id = get_valid_id("Enter Task ID to mark as done: ", tasks)
    task = tasks[task_id]

    if task[3] == STATUS_DONE:
        print(f"Notice: Task #{task_id} is already marked as Done.")
        return False

    # Tuples are immutable, so we create a new tuple keeping due date intact
    updated_task = (task[0], task[1], task[2], STATUS_DONE, task[4], task[5])
    tasks[task_id] = updated_task

    print(f"Success: Task #{task_id} ('{task[1]}') marked as Done!")
    return True


def edit_task(tasks, categories):
    """Edit title, priority, category, or due date of an existing task."""
    print("\n--- Edit Task ---")
    if len(tasks) == 0:
        print("Notice: No tasks available to edit.")
        return False

    task_id = get_valid_id("Enter Task ID to edit: ", tasks)
    task = tasks[task_id]
    print(f"Current task: Title='{task[1]}', Priority='{task[2]}', Status='{task[3]}', Category='{task[4]}', Due Date='{task[5]}'")

    # Edit title
    while True:
        prompt = f"Enter new title (press Enter to keep '{task[1]}'): "
        raw_title = input(prompt)
        if raw_title.strip() == "":
            new_title = task[1]
            break
        cleaned = clean_title(raw_title)
        if cleaned == "":
            print("Error: Invalid title or contains '|'. Please try again.")
            continue
        new_title = cleaned
        break

    # Edit priority
    while True:
        prompt = f"Enter new priority (press Enter to keep '{task[2]}'): "
        raw_priority = input(prompt).strip()
        if raw_priority == "":
            new_priority = task[2]
            break
        validated_p = is_valid_priority(raw_priority)
        if validated_p != "":
            new_priority = validated_p
            break
        print("Error: Priority must be High, Medium, or Low.")

    # Edit category
    while True:
        prompt = f"Enter new category (press Enter to keep '{task[4]}'): "
        raw_cat = input(prompt).strip()
        if raw_cat == "":
            new_category = task[4]
            break
        if "|" in raw_cat:
            print("Error: Category cannot contain '|'. Please try again.")
            continue
        new_category = raw_cat.title()
        categories.add(new_category)
        break

    # Edit due date
    while True:
        prompt = f"Enter new due date (YYYY-MM-DD) (press Enter to keep '{task[5]}'): "
        raw_date = input(prompt).strip()
        if raw_date == "":
            new_date = task[5]
            break
        if is_valid_date(raw_date):
            new_date = raw_date
            break
        print("Error: Invalid date! Please use YYYY-MM-DD format.")

    updated_task = (task[0], new_title, new_priority, task[3], new_category, new_date)
    tasks[task_id] = updated_task

    print(f"Success: Task #{task_id} updated successfully!")
    return True


def delete_task(tasks):
    """Delete a task by its ID from the tasks dictionary."""
    print("\n--- Delete Task ---")
    if len(tasks) == 0:
        print("Notice: No tasks available to delete.")
        return False

    task_id = get_valid_id("Enter Task ID to delete: ", tasks)
    deleted_task = tasks[task_id]
    del tasks[task_id]

    print(f"Success: Task #{task_id} ('{deleted_task[1]}') deleted successfully!")
    return True


def clear_completed_tasks(tasks):
    """Clear all completed tasks from the dictionary at once."""
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
        title = tasks[tid][1]
        if keyword in title.lower():
            matching_tasks[tid] = tasks[tid]

    if len(matching_tasks) == 0:
        print(f"No tasks found matching keyword '{keyword}'.")
        return 0

    print(f"\nFound {len(matching_tasks)} matching task(s):")
    return show_tasks(matching_tasks, None)


def show_tasks(tasks, filter_status=None):
    """Display tasks in a formatted table sorted by priority (Nested Loops)."""
    if len(tasks) == 0:
        print("\nNotice: Task list is empty.")
        return 0

    # Step 1: Collect all IDs and sort them using sort()
    id_list = []
    for tid in tasks:
        id_list.append(tid)
    id_list.sort()

    # Step 2: Build list of all tasks ordered by ID
    all_tasks = []
    for tid in id_list:
        all_tasks.append(tasks[tid])

    # Step 3: Filter tasks using slicing copy and remove()
    if filter_status == STATUS_PENDING:
        display_list = all_tasks[:]
        for task in all_tasks:
            if task[3] == STATUS_DONE:
                display_list.remove(task)
    elif filter_status == STATUS_DONE:
        display_list = all_tasks[:]
        for task in all_tasks:
            if task[3] == STATUS_PENDING:
                display_list.remove(task)
    else:
        display_list = all_tasks[:]
    
    if len(display_list) == 0:
        print(f"\nNotice: No tasks found matching status '{filter_status}'.")
        return 0

    # Step 4: Print table header with formatted column widths including Due Date
    print("\n" + "=" * 78)
    print(f"{'ID':<5} {'Title':<25} {'Priority':<9} {'Status':<9} {'Category':<12} {'Due Date':<11}")
    print("=" * 78)

    count = 0
    # NESTED LOOPS:
    # Outer loop iterates through priorities (High, Medium, Low)
    # Inner loop iterates through tasks to group them under each priority
    for p in PRIORITIES:
        for task in display_list:
            if task[2] == p:
                tid, title, priority, status, category, due_date = task
                print(f"{tid:<5} {title:<25} {priority:<9} {status:<9} {category:<12} {due_date:<11}")
                count = count + 1

    print("=" * 78)
    print(f"Total tasks shown: {count}")
    return count
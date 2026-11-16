"""
================================================================================
PART 3: TASK CRUD OPERATIONS, SEARCH & NESTED LOOPS TABLE
Student Name: Avanish Kumar (Group 12)
"""
"""
================================================================================
Topics Covered:
  - Input validation & crash prevention (get_valid_id, get_valid_priority, get_valid_category, get_valid_date)
  - Dictionary operations (insert, update, delete with `del`, lookup)
  - Tuple immutability (creating updated tuples for modified tasks)
  - List algorithms (id_list.sort(), display_list.remove(), list slicing copy [:])
  - Nested Loops (outer loop over PRIORITIES, inner loop over display_list)
  - Formatted output (f-string table column alignments)
  - String search & membership operators (keyword in title.lower())
================================================================================
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

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
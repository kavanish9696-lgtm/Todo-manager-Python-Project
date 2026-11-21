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

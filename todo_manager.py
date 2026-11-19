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


if __name__ == "__main__":
    print("Avinash Kumar's Storage Module (Part 2) is ready.")



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

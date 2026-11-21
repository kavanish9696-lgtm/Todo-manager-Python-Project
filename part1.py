# ============================================================
# PART 1: CONSTANTS, VALIDATION, MATH AND RECURSION
# ============================================================
# 1. GLOBAL CONSTANTS
PRIORITIES = ("High", "Medium", "Low")
STATUSES = ("Pending", "Done")
FILE_NAME = "tasks.txt"
PRIORITIES = ("High", "Medium", "Low") # Fixed tuple defining priority hierarchy
STATUS_PENDING = "Pending" 
STATUS_DONE = "Done"
STATUSES = (STATUS_PENDING, STATUS_DONE)
DEFAULT_CATEGORIES = {"Study", "Personal", "Work", "Health"} # Initial category set


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
def count_pending():
    # keep asking until a valid non-negative whole number is entered
    while True:
        text = input("\nHow many tasks do you want to enter? ").strip()
        if text.isdigit():
            total = int(text)
            break
        print("Please enter a valid whole number.")

    tasks = []
    for i in range(total):
        print("\nTask", i + 1)
        status = input("Enter status (Pending/Done): ").strip().title()
        while status not in STATUSES:
            print("Invalid status. Enter Pending or Done.")
            status = input("Enter status: ").strip().title()
        tasks.append(status)

    def count_recursive(tasks):
        if tasks == []:
            return 0
        count = 0
        if tasks[0] == "Pending":
            count = 1
        return count + count_recursive(tasks[1:])

    pending = count_recursive(tasks)
    print("\nTotal pending tasks:", pending)
    return pending, total


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


# ============================================================
# MAIN PROGRAM
# ============================================================

print("===================================")
print("       TO-DO LIST MANAGER")
print("===================================")

print("\n--- TASK DETAILS ---")

title = validate_title()
category = validate_category()
priority = validate_priority()
date = validate_date()

print("\n--- TASK DETAILS SUMMARY ---")

print("Title:", title)
print("Category:", category)
print("Priority:", priority)
print("Date:", date)

print("\n--- TASK STATISTICS ---")

pending, total = count_pending()

calculate_percent_done(pending, total)

print("\n===================================")
print("       PART 1 COMPLETED")
print("===================================")

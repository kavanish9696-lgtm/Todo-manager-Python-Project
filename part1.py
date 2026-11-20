# ============================================================
# PART 1: CONSTANTS, VALIDATION, MATH AND RECURSION
# ============================================================
# 1. GLOBAL CONSTANTS
PRIORITIES = ("High", "Medium", "Low")
STATUSES = ("Pending", "Done")


# 2. VALIDATE TASK TITLE
def validate_title():
    title = input("Enter task title: ")
    title = title.strip()
    if title == "":
        print("Title cannot be empty.")
        return None
    if "|" in title:
        print("Invalid character in title.")
        return None
    print("Valid title:", title)
    return title


# 3. VALIDATE CATEGORY
def validate_category():
    category = input("Enter task category: ")
    category = category.strip().title()
    if category == "":
        print("Category cannot be empty.")
        return None
    if "|" in category:
        print("Invalid category.")
        return None
    print("Valid category:", category)
    return category


# 4. VALIDATE PRIORITY
def validate_priority():
    priority = input("Enter priority (High/Medium/Low): ")
    priority = priority.strip().title()
    if priority in PRIORITIES:
        print("Valid priority:", priority)
        return priority
    else:
        print("Invalid priority.")
        return None


# 5. VALIDATE DATE
def validate_date():
    date = input("Enter date (YYYY-MM-DD): ")
    date = date.strip()
    parts = date.split("-")
    if len(parts) != 3:
        print("Invalid date format.")
        return False
    year = parts[0]
    month = parts[1]
    day = parts[2]
    if not year.isdigit():
        print("Invalid year.")
        return False
    if not month.isdigit():
        print("Invalid month.")
        return False
    if not day.isdigit():
        print("Invalid day.")
        return False
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        print("Use YYYY-MM-DD format.")
        return False
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 1 or month < 1 or month > 12:
        print("Invalid date.")
        return False

    # CHECK LEAP YEAR

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap_year = True
    else:
        leap_year = False
    days = [31, 29 if leap_year else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    if day < 1 or day > days[month - 1]:
        print("Invalid day for this month.")
        return False
    print("Valid date:", date)
    return True


# 6. COUNT PENDING TASKS USING RECURSION
def count_pending():
    total = int(input("\nHow many tasks do you want to enter? "))
    tasks = []
    for i in range(total):
        print("\nTask", i + 1)
        status = input("Enter status (Pending/Done): ")
        status = status.strip().title()
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
print("Date valid:", date)

print("\n--- TASK STATISTICS ---")

pending, total = count_pending()

calculate_percent_done(pending, total)

print("\n===================================")
print("       PART 1 COMPLETED")
print("===================================")


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


# END OF PART 1


"""
PART 1: CONSTANTS, VALIDATION, MATH & RECURSION
Student Name: Manasvi Saharawat
Group: 12
File: part1_manasvi.py

This module provides constants, validation functions,
completion percentage calculation and recursive counting
for the To-Do List Manager project.
"""

# --------------------------------------------------
# 1. GLOBAL CONSTANTS AND FIXED TUPLES
# --------------------------------------------------

PRIORITIES = ("High", "Medium", "Low")

STATUSES = ("Pending", "Done")


# --------------------------------------------------
# 2. STRING MANIPULATION AND VALIDATION
# --------------------------------------------------

def validate_title(title):
    """
    Remove unnecessary spaces and validate a task title.

    >>> validate_title("  Complete Python Project  ")
    'Complete Python Project'
    >>> validate_title("   ")
    None
    >>> validate_title("Task|Invalid")
    None
    """
    title = title.strip()

    if title == "" or "|" in title:
        return None

    return title


def validate_category(category):
    """
    Clean and validate a task category.

    >>> validate_category("  Study  ")
    'Study'
    >>> validate_category("")
    None
    >>> validate_category("Work|Personal")
    None
    """
    category = category.strip().title()

    if category == "" or "|" in category:
        return None

    return category


def validate_priority(priority):
    """
    Validate and standardize task priority.

    >>> validate_priority(" high ")
    'High'
    >>> validate_priority("MEDIUM")
    'Medium'
    >>> validate_priority("Urgent")
    None
    """
    priority = priority.strip().title()

    if priority in PRIORITIES:
        return priority

    return None


# --------------------------------------------------
# 3. DATE VALIDATION
# --------------------------------------------------

def validate_date(date_text):
    """
    Validate a date in YYYY-MM-DD format.

    Checks the year, month, day and leap years.

    >>> validate_date("2026-11-18")
    True
    >>> validate_date("2024-02-29")
    True
    >>> validate_date("2025-02-29")
    False
    >>> validate_date("18-11-2026")
    False
    >>> validate_date("2026-13-10")
    False
    """

    parts = date_text.split("-")

    # Check format and number of components
    if len(parts) != 3:
        return False

    year, month, day = parts

    # Check that all components contain digits
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    # Check component lengths
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    # Check valid year and month
    if year < 1 or month < 1 or month > 12:
        return False

    # Calculate leap year
    is_leap_year = (
        year % 400 == 0 or
        (year % 4 == 0 and year % 100 != 0)
    )

    # Days in each month
    days_in_month = (
        31, 29 if is_leap_year else 28,
        31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    )

    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True


# --------------------------------------------------
# 4. RECURSION: COUNT PENDING TASKS
# --------------------------------------------------

def count_pending(tasks):
    """
    Count pending tasks using recursion and list slicing.

    Each task is stored as:
    (id, title, priority, status)

    Base case: An empty list contains zero pending tasks.

    Recursive case: Check the first task and process
    the remaining tasks.

    >>> count_pending([])
    0
    >>> count_pending([(1, "Study", "High", "Pending")])
    1
    >>> count_pending([
    ...     (1, "Study", "High", "Pending"),
    ...     (2, "Exercise", "Low", "Done"),
    ...     (3, "Coding", "Medium", "Pending")
    ... ])
    2
    """

    # Base case
    if len(tasks) == 0:
        return 0

    # Check the status of the first task
    if tasks[0][3] == "Pending":
        current_pending = 1
    else:
        current_pending = 0

    # Recursive call with the remaining list
    return current_pending + count_pending(tasks[1:])


# --------------------------------------------------
# 5. MATHEMATICAL CALCULATION
# --------------------------------------------------

def calculate_percent_done(tasks):
    """
    Calculate the percentage of completed tasks.

    Formula:
    (Completed Tasks / Total Tasks) * 100

    The result is rounded to one decimal place.

    >>> calculate_percent_done([])
    0.0
    >>> calculate_percent_done([
    ...     (1, "Study", "High", "Done"),
    ...     (2, "Coding", "Medium", "Pending")
    ... ])
    50.0
    >>> calculate_percent_done([
    ...     (1, "Study", "High", "Done"),
    ...     (2, "Coding", "Medium", "Done"),
    ...     (3, "Exercise", "Low", "Pending")
    ... ])
    66.7
    """

    total_tasks = len(tasks)

    # Avoid division by zero
    if total_tasks == 0:
        return 0.0

    completed_tasks = total_tasks - count_pending(tasks)

    percentage = (completed_tasks / total_tasks) * 100

    return round(percentage, 1)


# --------------------------------------------------
# END OF PART 1
# --------------------------------------------------


# PART 1: CONSTANTS, VALIDATION, MATH AND RECURSION

# 1. Global Constants

PRIORITIES = ("High", "Medium", "Low")
STATUSES = ("Pending", "Done")


# 2. Validate Task Title

def validate_title(title):
    title = title.strip()

    if title == "":
        return None

    if "|" in title:
        return None

    return title


# 3. Validate Category

def validate_category(category):
    category = category.strip().title()

    if category == "":
        return None

    if "|" in category:
        return None

    return category


# 4. Validate Priority

def validate_priority(priority):
    priority = priority.strip().title()

    if priority in PRIORITIES:
        return priority
    else:
        return None


# 5. Validate Date

def validate_date(date):

    date = date.strip()

    parts = date.split("-")

    if len(parts) != 3:
        return False

    year = parts[0]
    month = parts[1]
    day = parts[2]

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
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

    days = [31, 29 if leap_year else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if day < 1 or day > days[month - 1]:
        return False

    return True


# 6. Count Pending Tasks Using Recursion

def count_pending(tasks):

    if tasks == []:
        return 0

    count = 0

    if tasks[0][3] == "Pending":
        count = 1

    return count + count_pending(tasks[1:])


# 7. Calculate Percentage of Completed Tasks

def calculate_percent_done(tasks):

    total = len(tasks)

    if total == 0:
        return 0

    pending = count_pending(tasks)

    completed = total - pending

    percentage = (completed / total) * 100

    return round(percentage, 1)

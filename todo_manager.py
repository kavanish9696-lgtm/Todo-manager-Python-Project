"""
================================================================================
PART 4: MAIN MENU
Student Name: Prashant (Group 12)
File: part4_prashant.py
================================================================================
"""


def main():
    """Main menu loop."""
    categories = set(DEFAULT_CATEGORIES)
    tasks = load_tasks(FILE_NAME, categories)

    while True:
        print("\n" + "=" * 36)
        print("    TO-DO LIST MANAGER (GROUP 12)")
        print("=" * 36)
        print("""1.  Add Task (with Due Date)
2.  Mark Task as Done
3.  Edit Task
4.  Delete Task
5.  View All Tasks (by Priority)
6.  View Pending Tasks
7.  View Completed Tasks
8.  Show Pending Count & Stats
9.  Search Tasks by Keyword  [NEW]
10. Clear Completed Tasks     [NEW]
11. Exit""")
        print("=" * 36)

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_task(tasks, categories)
            save_tasks(FILE_NAME, tasks)
        elif choice == "2":
            if mark_done(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "3":
            if edit_task(tasks, categories):
                save_tasks(FILE_NAME, tasks)
        elif choice == "4":
            if delete_task(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "5":
            show_tasks(tasks, None)
        elif choice == "6":
            show_tasks(tasks, STATUS_PENDING)
        elif choice == "7":
            show_tasks(tasks, STATUS_DONE)
        elif choice == "8":
            task_list = []
            for tid in tasks:
                task_list.append(tasks[tid])
            pending_num = count_pending(task_list)
            total_num = len(tasks)

            print("\n--- Task Statistics ---")
            print(f"Total Tasks     : {total_num}")
            print(f"Pending Tasks   : {pending_num} (calculated via recursion)")
            calculate_percent_done(pending_num, total_num)
        elif choice == "9":
            search_tasks(tasks)
        elif choice == "10":
            if clear_completed_tasks(tasks):
                save_tasks(FILE_NAME, tasks)
        elif choice == "11":
            save_tasks(FILE_NAME, tasks)
            print("\nAll tasks saved successfully. Thank you for using To-Do List Manager! Goodbye.")
            break
        else:
            print("Error: Invalid choice! Please enter a number between 1 and 11.")


main()


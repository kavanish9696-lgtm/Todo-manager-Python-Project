"""
================================================================================
PART 4: MAIN MENU CONTROLLER & SYSTEM INTEGRATION
Student Name: Prashant (Group 12)
File: part4_prashant.py
================================================================================
Topics Covered:
  - Integration of all 3 preceding modules (part1_manasvi, part2_avinash, part3_aayush)
  - Main event loop using while True
  - Menu flow control using if-elif-else (Options 1 to 11)
  - Recursive pending count integration
  - Percentage completion calculation
  - Persistence triggers (auto-saving on state changes and exit)
  - Clean error messages and graceful termination
================================================================================
"""


def main():
    """Main function controlling the interactive menu loop."""
    categories = set(DEFAULT_CATEGORIES)
    tasks = load_tasks(FILE_NAME, categories)

    while True:
        print("\n" + "=" * 36)
        print("    TO-DO LIST MANAGER (GROUP 12)")
        print("=" * 36)
        print("1.  Add Task (with Due Date)")
        print("2.  Mark Task as Done")
        print("3.  Edit Task")
        print("4.  Delete Task")
        print("5.  View All Tasks (by Priority)")
        print("6.  View Pending Tasks")
        print("7.  View Completed Tasks")
        print("8.  Show Pending Count & Stats")
        print("9.  Search Tasks by Keyword  [NEW]")
        print("10. Clear Completed Tasks     [NEW]")
        print("11. Exit")
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
            for tid in sorted(tasks.keys()):
                task_list.append(tasks[tid])

            pending_num = count_pending(task_list)
            total_num = len(tasks)
            completed_num = total_num - pending_num
            pct = percent_done(total_num, completed_num)

            print("\n--- Task Statistics ---")
            print(f"Total Tasks     : {total_num}")
            print(f"Pending Tasks   : {pending_num} (calculated via recursion)")
            print(f"Completed Tasks : {completed_num}")
            print(f"Completion Rate : {pct}%")
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


if __name__ == "__main__":
    main()

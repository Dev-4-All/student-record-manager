from typing import Final

from student_record_manager import StudentRecordManager

RECORD_FILE: Final = "student_record.pickle"


def display_options():
    print("1) Add Record")
    print("2) Delete Record")
    print("3) Search Record")
    print("4) Display All Records")
    print("5) Update Marks")
    print("6) Display Marks Statistics")
    print("7) Exit")


def main():
    manager = StudentRecordManager(RECORD_FILE)

    operations = {
        "1": manager.add_record,
        "2": manager.delete_record,
        "3": manager.search_record,
        "4": manager.display_all_records,
        "5": manager.update_marks,
        "6": manager.display_marks_statistics,
    }

    print("Welcome to Py Student Record Manager!")

    while True:
        display_options()

        choice = input("Choose an option: ")
        if choice in operations:
            operations[choice]()
        elif choice == "7":
            manager.save_records()
            break
        else:
            print("Please enter a valid choice")


if __name__ == "__main__":
    main()

from pickle import dump, load
from typing import Final

from student import Student


class StudentRecordManager:
    def __init__(self, record_file: str) -> None:
        self.__record_file: Final = record_file
        self.__records = self.__load_records()

    def __load_records(self) -> list:
        records: list[Student]

        try:
            with open(self.__record_file, "rb") as file:
                records = load(file)
        except FileNotFoundError:
            records = []

        return records

    def __get_matches(self, name: str) -> list[tuple[int, Student]] | None:
        matches: list[tuple[int, Student]] = []

        for idx, record in enumerate(self.__records):
            if record.get_name() == name:
                matches.append((idx, record))

        if matches:
            return matches

        print("No such student found in records.")

        return None

    def __get_exact_match(self, name: str) -> tuple[int, Student] | None:
        matches: list[tuple[int, Student]] | None = self.__get_matches(name)

        if matches:
            exact_match: tuple[int, Student]

            no_of_matches = len(matches)

            if no_of_matches == 1:
                print("Found 1 matching record:")
                exact_match = matches[0]
                StudentRecordManager.__print_record_info(
                    exact_match[1].get_name(),
                    exact_match[1].get_marks(),
                    exact_match[1].get_phone(),
                )
            else:
                print(f"Found {len(matches)} matching records:")
                for idx, exact_match in enumerate(matches, start=1):
                    print(f"{idx}) ", end="")
                    StudentRecordManager.__print_record_info(
                        exact_match[1].get_name(),
                        exact_match[1].get_marks(),
                        exact_match[1].get_phone(),
                    )

                while True:
                    try:
                        choice = int(input("Choose one: "))
                        exact_match = matches[choice - 1]
                        break
                    except ValueError:
                        print("Please enter a valid number")
                    except IndexError:
                        print("Please enter a valid choice")

            return exact_match

        return None

    def __get_insertion_index(self, marks: int) -> int:
        left = 0
        right = len(self.__records) - 1

        while left <= right:
            mid = (left + right) // 2
            existing_student_marks = self.__records[mid].get_marks()

            if marks > existing_student_marks:
                left = mid + 1
            elif marks < existing_student_marks:
                right = mid - 1
            else:
                left = mid
                break

        return left

    def __lowest_marks(self) -> int:
        return self.__records[0].get_marks()

    def __highest_marks(self) -> int:
        return self.__records[-1].get_marks()

    def __average_marks(self) -> float:
        marks: list[int] = [record.get_marks() for record in self.__records]
        return sum(marks) / len(marks)

    def add_record(self) -> None:
        name: str = StudentRecordManager.__input_name("Enter name: ")
        marks: int = StudentRecordManager.__input_marks("Enter marks: ")
        existing_phones: list[str] = [record.get_phone() for record in self.__records]
        phone: str = StudentRecordManager.__input_phone(
            "Enter phone number: ", existing_phones
        )

        idx: int = self.__get_insertion_index(marks)
        student = Student(name, marks, phone)
        self.__records.insert(idx, student)

        print("Operation Successful!")

    def delete_record(self) -> None:
        if not self.__records:
            print("No records to delete anything")
            return

        name: str = StudentRecordManager.__input_name("Enter name: ")
        exact_match: tuple[int, Student] | None = self.__get_exact_match(name)

        if exact_match:
            confirmation = input("Would like to delete this record? [Y/N]\n").upper()
            if confirmation == "Y":
                record_idx, _ = exact_match
                self.__records.pop(record_idx)
                print("Operation Successful!")
            elif confirmation == "N":
                print("Record not deleted!")
            else:
                print("Invalid input. Operation Unsuccessful!")

    def search_record(self) -> None:
        if not self.__records:
            print("No records to search anything")
            return

        name: str = StudentRecordManager.__input_name("Enter name: ")
        matching_records: list[tuple[int, Student]] | None = self.__get_matches(name)

        if matching_records:
            for record_tuple in matching_records:
                _, record = record_tuple
                StudentRecordManager.__print_record_info(
                    record.get_name(), record.get_marks(), record.get_phone()
                )

    def display_all_records(self) -> None:
        if not self.__records:
            print("No records to display anything")
            return

        for record in self.__records:
            StudentRecordManager.__print_record_info(
                record.get_name(), record.get_marks(), record.get_phone()
            )

    def save_records(self) -> None:
        with open(self.__record_file, "wb") as file:
            dump(self.__records, file)
        print("Records saved Successfully!")

    def update_name(self) -> None:
        if not self.__records:
            print("No records to update anything")
            return

        old_name: str = StudentRecordManager.__input_name("Enter name: ")
        exact_match: tuple[int, Student] | None = self.__get_exact_match(old_name)

        if exact_match:
            _, student = exact_match

            new_name: str = self.__input_name("Enter new name: ")
            student.set_name(new_name)

            print(f"Name updated from {old_name} to {new_name}")

    def update_marks(self) -> None:
        if not self.__records:
            print("No records to update anything")
            return

        name: str = StudentRecordManager.__input_name("Enter name: ")
        exact_match: tuple[int, Student] | None = self.__get_exact_match(name)

        if exact_match:
            old_idx, student = exact_match

            old_marks = student.get_marks()
            new_marks: int = StudentRecordManager.__input_marks("Enter new marks: ")
            student.set_marks(new_marks)

            self.__records.pop(old_idx)
            new_idx = self.__get_insertion_index(new_marks)
            self.__records.insert(new_idx, student)

            print(f"Marks updated from {old_marks} to {new_marks}")

    def update_phone(self) -> None:
        if not self.__records:
            print("No records to update anything")
            return

        name: str = StudentRecordManager.__input_name("Enter name: ")
        exact_match: tuple[int, Student] | None = self.__get_exact_match(name)

        if exact_match:
            _, student = exact_match

            old_phone: str = student.get_phone()

            existing_phones: list[str] = [
                record.get_phone() for record in self.__records
            ]
            new_phone: str = self.__input_phone(
                "Enter new phone number: ", existing_phones
            )
            student.set_phone(new_phone)

            print(f"Name updated from {old_phone} to {new_phone}")

    def display_marks_statistics(self) -> None:
        if not self.__records:
            print("No records to display anything")
            return

        print(f"Lowest Marks: {self.__lowest_marks()}")
        print(f"Highest Marks: {self.__highest_marks()}")
        print(f"Average Marks: {self.__average_marks()}")

    def clear_all_records(self) -> None:
        confirmation = input("Would like to clear all existing records? [Y/N]\n").upper()
        
        if confirmation == "Y":
            self.__records.clear()
            print("Operation Successful!")
        elif confirmation == "N":
            print("Records not cleared!")
        else:
            print("Invalid input. Operation Unsuccessful!")

    @staticmethod
    def __print_record_info(name: str, marks: int, phone: str) -> None:
        print(f"Name: {name}, Marks: {marks}, Phone: {phone}.")

    @staticmethod
    def __input_name(prompt: str) -> str:
        while True:
            name = input(prompt)
            if StudentRecordManager.__is_name_valid(name):
                return " ".join(name.split()).title()
            else:
                print("Name cannot be empty and must contain only letters and spaces")

    @staticmethod
    def __input_marks(prompt: str) -> int:
        while True:
            try:
                marks = int(input(prompt))
                if StudentRecordManager.__is_marks_valid(marks):
                    return marks
                else:
                    print("Marks are out of the valid range")
            except ValueError:
                print("Please enter a valid integral number")

    @staticmethod
    def __input_phone(prompt: str, existing_phones: list[str]) -> str:
        while True:
            phone = input(prompt)
            if (
                StudentRecordManager.__is_phone_valid(phone)
                and phone not in existing_phones
            ):
                return phone
            else:
                print(
                    "Phone number must be unique and should contain 10 numerical digits"
                )

    @staticmethod
    def __is_name_valid(name: str) -> bool:
        if not name.strip():
            return False

        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False

        return True

    @staticmethod
    def __is_marks_valid(marks: int) -> bool:
        return 0 <= marks <= 100

    @staticmethod
    def __is_phone_valid(phone: str) -> bool:
        if len(phone) != 10:
            return False

        for digit in phone:
            if not digit.isdigit():
                return False

        return True

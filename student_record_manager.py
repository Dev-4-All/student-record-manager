from pickle import load
from typing import Final

from student import Student


class StudentRecordManager:
    def __init__(self, record_file: str) -> None:
        self.__record_file: Final = record_file
        self.__records = self.load_records()

    def load_records(self) -> list:
        records: list[Student]

        try:
            with open(self.__record_file, "rb") as file:
                records = load(file)
        except FileNotFoundError:
            records = []

        return records

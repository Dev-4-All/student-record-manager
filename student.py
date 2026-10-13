from uuid import UUID, uuid4


class Student:
    def __init__(self, name: str, marks: int, phone: str) -> None:
        self.__id: UUID = uuid4()
        self.__name = name
        self.__marks = marks
        self.__phone = phone

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_marks(self) -> int:
        return self.__marks

    def set_marks(self, marks: int) -> None:
        self.__marks = marks

    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

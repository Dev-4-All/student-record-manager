class Student:
    def __init__(self, name: str, marks: int) -> None:
        self.__name = name
        self.__marks = marks

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_marks(self) -> int:
        return self.__marks

    def set_marks(self, marks: int) -> None:
        self.__marks = marks

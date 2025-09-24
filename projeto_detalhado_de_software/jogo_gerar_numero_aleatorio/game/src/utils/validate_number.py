class ValidateNumber:
    def __init__(self, number: int) -> None:
        self._number: int = number

    def result(self, number_user: int) -> int:
        if number_user > self._number:
            return 1
        elif number_user < self._number:
            return -1
        return 0
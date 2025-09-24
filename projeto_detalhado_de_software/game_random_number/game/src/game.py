from .utils import GenerateRandomNumber, ValidateNumber

class Game:
    def __init__(self) -> None:
        self._number_random = GenerateRandomNumber.generate_number()
    
    def result(self, number_user: int) -> int:
        validate_number = ValidateNumber(self._number_random)
        return validate_number.result(number_user)
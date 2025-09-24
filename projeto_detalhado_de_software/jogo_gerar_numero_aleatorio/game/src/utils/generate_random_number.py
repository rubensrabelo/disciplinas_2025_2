from random import randint


class GenerateRandomNumber:
    @staticmethod
    def generate_number() -> int:
        return randint(1, 5)

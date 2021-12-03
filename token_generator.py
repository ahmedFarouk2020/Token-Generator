import random


class GeneratePassword:
    def __init__(self) -> None:
        pass


    @staticmethod
    def generate_password(num_of_passwordDigits: int) -> int :

        
        upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "~!@#$%^&*()-_=+."
        all_characters = upper_case_letters + lower_case_letters + special_characters

        password = "".join(random.sample(all_characters,num_of_passwordDigits))
        
        return password




from string import ascii_letters
import random


def generate_room_code(length: int, existing_codes: list[str]) -> str:
    """
    To create a random alphanumeric code of a 
    specified length that is not already 
    present in a given list of existing codes
    """
    while True:
        code_chars = [random.choice(ascii_letters) for _ in range(length)]
        code = ''.join(code_chars)

        if code not in existing_codes:
            
            return code


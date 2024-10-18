import random
import string


def random_string_generator(char_number: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_number))

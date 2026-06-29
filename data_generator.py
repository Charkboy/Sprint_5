import random
import string

def generate_email():
    return f"test_testov_1999_{''.join(random.choices(string.digits, k=3))}@yandex.ru"

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def generate_name():
    return ''.join(random.choices(string.ascii_letters, k=8)).capitalize()
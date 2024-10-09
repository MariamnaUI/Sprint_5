import string
import random


class Generator:

    @staticmethod
    def login_generate():
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5, 20)))+'@yandex.ru'

    @staticmethod
    def password_generate():
        return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(random.randint(6, 12)))

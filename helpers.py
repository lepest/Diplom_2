import random
import string

class Helpers:

    def register_new_user(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        password = generate_random_string(10)
        name = generate_random_string(10)
        email = f'{name}@yandex.ru'

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload
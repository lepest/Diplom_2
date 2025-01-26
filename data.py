class Data:
    user_reg = {
        "email": "masterok_user@yandex.ru",
        "password": "123456852",
        "name": "Lusya"
    }

    registered_user = {
        "email": "master_user@yandex.ru",
        "password": "123456852",
        "name": "Vasya"
    }

    user_empty_field = {
        "email": "",
        "password": "123456852",
        "name": "Vasya"
    }

    existing_login = {
        "email": "master_user@yandex.ru",
        "password": "123456852"
    }

    incorrect_email = {
        "email": "master_user@yandex",
        "password": "123456852"
    }

    incorrect_password = {
        "email": "master_user@yandex.ru",
        "password": "1"
    }

    incorrect_email_password = {
        "email": "master_useryandex.ru",
        "password": "1"
    }

    update_data = {
        "name": "Roman"
    }

    incorrect_ingredients = {
        "ingredients": ["60d","609646e4dc9"]
    }
import requests
import allure

from config import REGISTER_URL, USER_URL, AUTHORIZATION_USER

class UserMethods:

    @allure.step('Создать уникального пользователя')
    def request_to_create_user(self, payload):
        response = requests.post(f'{REGISTER_URL}', data=payload)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, token):
        header = {'Authorization': token}
        response = requests.delete(f'{USER_URL}?accessToken=', headers=header)
        return response

    @allure.step('Авторизация под существующим логином пользователя')
    def authorization_existing_login(self, payload):
        response = requests.post(f'{AUTHORIZATION_USER}', data=payload)
        return response

    @allure.step('Получить токен уникального пользователяз')
    def get_token_user(self, payload):
        response = requests.post(f'{AUTHORIZATION_USER}', data=payload)
        return response.json()['refreshToken']

    @allure.step('Изменение данных пользователя')
    def user_data_update(self, payload, headers_1):
        response = requests.patch(f'{USER_URL}', data=payload, headers=headers_1)
        return response

    @allure.step('Получить токен')
    def get_token_user(self, payload):
        response = self.authorization_existing_login(payload)
        return response.json()["accessToken"]
import pytest
import allure

from methods.user_methods import UserMethods
from helpers import Helpers
from data import Data

class TestUser:

    token = ''

    @allure.title('Создание курьера')
    def test_create_user(self, delete_user):
        payload = Helpers().register_new_user()
        response = UserMethods().request_to_create_user(payload)
        payload_av = {'email': payload['email'],
                           'password': payload['password']}
        self.token = UserMethods().get_token_user(payload_av)
        assert response.status_code == 200 and response.json()['success']


    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_registered_user(self):
        payload = Data.registered_user
        response = UserMethods().request_to_create_user(payload)
        assert response.status_code == 403 and response.json()['success'] == False

    @allure.title('Создание пользователя с незаполненным полем')
    def test_create_user_with_empty_field(self):
        payload = Data.user_empty_field
        response = UserMethods().request_to_create_user(payload)
        assert response.status_code == 403 and response.json()['success'] == False

    @allure.title('Авторизация под существующим логином пользователя')
    def test_authorization_existing_login(self):
        payload = Data.existing_login
        response = UserMethods().authorization_existing_login(payload)
        assert payload['email'] in response.json()['user']['email'] and response.status_code == 200

    @allure.title('Авторизация с неверным логином и паролем')
    @pytest.mark.parametrize('data_payload', ['Data.incorrect_email, Data.incorrect_password, Data.incorrect_email_password'])
    def test_authorization_incorrect_data(self, data_payload):
        payload = data_payload
        response = UserMethods().authorization_existing_login(payload)
        assert response.status_code == 401 and response.json()['success'] == False

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_user_data_update_with_authorization(self):
        update_payload = Data.update_data
        headers = {}
        headers['Authorization'] = UserMethods().get_token_user(Data.existing_login)
        response = UserMethods().user_data_update(update_payload, headers)
        assert response.json()["success"] and response.status_code == 200

    @allure.title('Изменение данных пользователя без авторизации')
    def test_user_data_update_without_authorization(self):
        payload = Data.update_data
        response = UserMethods().user_data_update(payload, '')
        assert response.json()["success"] == False and response.status_code == 401
import requests
import allure

from config import ORDER_URL, INGREDIENT_URL, GET_ORDER
from methods.user_methods import UserMethods

class OrderMethods:

    @allure.step('Получение данных об ингредиентах c авторизацией')
    def get_hash_ingredient(self, payload):
        headers_1 = {}
        headers_1['Authorization'] = UserMethods().get_token_user(payload)
        response = requests.get(f'{INGREDIENT_URL}', headers=headers_1)
        list_hash = []
        for i in range(0, 10):
            list_hash.append(response.json()['data'][i]['_id'])
        return list_hash

    @allure.step('Создание заказа')
    def create_order(self, payload):
        response = requests.post(f'{ORDER_URL}', data=payload)
        return response

    @allure.step('Получение данных об ингредиентах без авторизации')
    def get_hash_ingredient_without_authorization(self):
        response = requests.get(f'{INGREDIENT_URL}')
        list_hash = []
        for i in range(0, 10):
            list_hash.append(response.json()['data'][i]['_id'])
        return list_hash

    @allure.step('Получение заказов')
    def get_orders(self):
        response = requests.get(f'{GET_ORDER}')
        return response
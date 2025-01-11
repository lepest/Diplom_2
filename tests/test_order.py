import allure

from data import Data
from methods.order_methods import OrderMethods

class TestOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_authorization(self):
        payload = {}
        payload_ingredient = OrderMethods().get_hash_ingredient(Data.existing_login)
        payload["ingredients"] = payload_ingredient
        response = OrderMethods().create_order(payload)
        assert response.status_code == 200

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self):
        payload = {}
        payload_ingredient = OrderMethods().get_hash_ingredient_without_authorization()
        payload["ingredients"] = payload_ingredient
        response = OrderMethods().create_order(payload)
        assert response.status_code == 200

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = {"ingredients": []}
        OrderMethods().get_hash_ingredient(Data.existing_login)
        response = OrderMethods().create_order(payload)
        assert response.status_code == 400

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_incorrect_authorization(self):
        OrderMethods().get_hash_ingredient(Data.existing_login)
        response = OrderMethods().create_order(Data.incorrect_ingredients)
        assert response.status_code == 500

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_authorization_user(self):
        payload = {}
        payload_ingredient = OrderMethods().get_hash_ingredient(Data.existing_login)
        payload["ingredients"] = payload_ingredient
        response = OrderMethods().create_order(payload)
        assert response.json()["success"] == True and response.status_code == 200

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_no_authorization_user(self):
        response = OrderMethods().get_orders()
        assert response.status_code == 401

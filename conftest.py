import pytest

from methods.user_methods import UserMethods
@pytest.fixture(scope='function')
def delete_user():
    user_method = UserMethods()
    del_user = user_method.delete_user()
    yield del_user




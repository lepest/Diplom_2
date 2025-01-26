import pytest

from methods.user_methods import UserMethods

@pytest.fixture()
def delete_user(request):
    yield
    return UserMethods().delete_user(request.cls.token)

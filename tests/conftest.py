import pytest
from pytest_factoryboy import register

from rest_framework.test import APIClient

from tests.factories import AdsFactory, UserFactory

# Factories
register(AdsFactory)
register(UserFactory)


@pytest.fixture
@pytest.mark.django_db
def authenticated_user(django_user_model):
    user_data = {
        "email": "test@test.ru",
        "password": "test123test",
        "first_name": "Test",
        "last_name": "Testov",
        "phone": "+79001112233"
    }
    # Create a user
    user = django_user_model.objects.create_user(**user_data)

    # Authenticate the user using the Django test client
    client = APIClient()
    client.force_authenticate(user=user)
    return user, client

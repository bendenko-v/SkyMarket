import json
import pytest

from django.conf import settings

from ads.models import Ad
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_get_ads_list(client):
    AdsFactory.create_batch(7)

    response = client.get('/api/ads/')

    assert response.status_code == 200
    assert len(response.data['results']) == settings.REST_FRAMEWORK['PAGE_SIZE']


@pytest.mark.django_db
def test_get_ad(client):
    ads = AdsFactory.create_batch(3)
    ad_id = ads[0].id

    response = client.get(f'/api/ads/{ad_id}/')

    assert response.status_code == 200
    assert response.data['pk'] == ad_id


@pytest.mark.django_db
def test_create_ad(client, authenticated_user):
    user, auth_client = authenticated_user

    new_ad = {
        'title': 'Test ad title',
        'price': 10000,
        'description': 'Test ad description',
    }

    response = auth_client.post(
        '/api/ads/',
        data=json.dumps(new_ad),
        content_type='application/json'
    )

    response_data = response.json()
    created = response_data['created_at']
    ad_id = response_data['id']

    expected_response = {
        'id': ad_id,
        'title': 'Test ad title',
        'price': 10000,
        'description': 'Test ad description',
        'image': None,
        'author': user.id,
        'created_at': created,
    }

    assert response.status_code == 201
    assert response_data == expected_response


@pytest.mark.django_db
def test_update_ad(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create(author=user)

    updated_ad_data = {
        'title': 'Updated ad title',
        'price': 20000,
        'description': 'Updated ad description',
    }

    response = auth_client.patch(
        f'/api/ads/{ad.id}/',
        data=json.dumps(updated_ad_data),
        content_type='application/json'
    )

    expected_response = {
        'pk': ad.id,
        'title': 'Updated ad title',
        'price': 20000,
        'description': 'Updated ad description',
        'image': None,
    }

    assert response.status_code == 200
    assert response.data == expected_response

    ad.refresh_from_db()
    assert ad.title == 'Updated ad title'
    assert ad.price == 20000
    assert ad.description == 'Updated ad description'


@pytest.mark.django_db
def test_delete_ad(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create(author=user)

    response = auth_client.delete(f'/api/ads/{ad.id}/')

    assert response.status_code == 204

    # Verify that the ad is deleted from the database
    with pytest.raises(Ad.DoesNotExist):
        ad.refresh_from_db()

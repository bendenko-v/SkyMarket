import pytest
from rest_framework import status

from ads.models import Comment
from tests.factories import AdsFactory


@pytest.mark.django_db
def test_get_comments_list(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create()
    comment = Comment.objects.create(ad=ad, author=user, text='some text')

    response = client.get(f'/api/ads/{ad.id}/comments/')

    expected_response = {
        'count': 1,
        'next': None,
        'previous': None,
        'results': [
            {
                'pk': comment.id,
                'text': comment.text,
                'author_id': user.id,
                'author_first_name': user.first_name,
                'author_last_name': user.last_name,
                'ad_id': ad.id,
                'author_image': None
            }
        ]
    }
    # 'created_at' was not included in expected

    assert response.status_code == 200
    assert len(response.data['results']) == 1

    actual_results = response.data['results']
    expected_results = expected_response['results']

    for actual, expected in zip(actual_results, expected_results):
        for key in expected.keys():
            assert key in actual
            assert actual[key] == expected[key]


@pytest.mark.django_db
def test_get_comment(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create()
    comment = Comment.objects.create(ad=ad, author=user, text='Test comment')

    response = auth_client.get(f'/api/ads/{ad.id}/comments/{comment.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['pk'] == comment.id
    assert response.data['text'] == 'Test comment'
    assert response.data['author_id'] == user.id
    assert response.data['ad_id'] == ad.id


@pytest.mark.django_db
def test_create_comment(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create()
    comment_data = {
        'text': 'Test comment',
        'ad': ad.id,
    }

    response = auth_client.post(f'/api/ads/{ad.id}/comments/', data=comment_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['text'] == 'Test comment'
    assert response.data['author'] == user.id
    assert response.data['ad'] == ad.id


@pytest.mark.django_db
def test_update_comment(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create()
    comment = Comment.objects.create(ad=ad, author=user, text='Test comment')

    updated_comment_data = {
        'text': 'Updated comment',
    }

    response = auth_client.patch(
        f'/api/ads/{ad.id}/comments/{comment.id}/',
        data=updated_comment_data
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data['text'] == 'Updated comment'
    assert response.data['author_id'] == user.id
    assert response.data['ad_id'] == ad.id

    comment.refresh_from_db()
    assert comment.text == 'Updated comment'


@pytest.mark.django_db
def test_delete_comment(client, authenticated_user):
    user, auth_client = authenticated_user

    ad = AdsFactory.create()
    comment = Comment.objects.create(ad=ad, author=user, text='Test comment')

    response = auth_client.delete(f'/api/ads/{ad.id}/comments/{comment.id}/')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    with pytest.raises(Comment.DoesNotExist):
        comment.refresh_from_db()

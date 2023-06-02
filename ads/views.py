from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ads.filters import AdFilterSet
from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import (
    AdSerializer, AdDetailSerializer, CommentSerializer, AdCreateSerializer, CommentCreateSerializer
)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilterSet

    serializers = {
        'list': AdSerializer,
        'retrieve': AdDetailSerializer,
        'create': AdCreateSerializer,
    }
    default_serializer = AdSerializer

    permissions = {
        'create': [IsAuthenticated],
        'update': [IsOwner],
        'partial_update': [IsOwner],
        'destroy': [IsOwner | IsAdmin],
    }
    default_permission = [AllowAny]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Set the author as the currently authenticated user
        request.data['author'] = request.user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    serializers = {
        'list': CommentSerializer,
        'create': CommentCreateSerializer,
    }
    default_serializer = CommentSerializer

    permissions = {
        'create': [IsAuthenticated],
        'update': [IsOwner],
        'partial_update': [IsOwner],
        'destroy': [IsOwner | IsAdmin],
    }
    default_permission = [AllowAny]

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)

        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        ad_pk = self.kwargs.get('ad_pk')
        queryset = self.queryset.filter(ad_id=ad_pk)
        serializer = self.get_serializer(queryset, many=True)

        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def create(self, request, *args, **kwargs):
        ad_pk = self.kwargs.get('ad_pk')

        data = {
            'ad': ad_pk,
            'author': request.user.pk,
            'text': request.data.get('text')
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAdsListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(author=request.user)

        return super().list(request, *args, **kwargs)

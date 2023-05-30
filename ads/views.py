from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ads.models import Ad, Comment
from ads.serializers import (
    AdSerializer, AdDetailSerializer, CommentSerializer
)


# class AdPagination(pagination.PageNumberPagination):
#     page_size = 4
#     page_size_query_param = 'page'


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    # pagination_class = AdPagination

    serializers = {
        'list': AdSerializer,
        'retrieve': AdDetailSerializer,
    }
    default_serializer = AdSerializer

    permissions = {
        # 'retrieve': [IsAuthenticated],
        'create': [IsAuthenticated],
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # set the author as the currently authenticated user
        serializer.validated_data['author'] = request.user

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
    serializer_class = CommentSerializer

    permissions = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
    }

    default_permission = [AllowAny]

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

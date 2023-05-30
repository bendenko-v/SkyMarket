from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

router = SimpleRouter()
router.register("ads", AdViewSet, basename="ads")
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = [
    path('', include(router.urls))
]

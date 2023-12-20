from rest_framework.routers import DefaultRouter

from blogs.views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register("post", PostViewSet)
router.register("comment", CommentViewSet)

urlpatterns = router.urls

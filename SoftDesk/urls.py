from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from web.views import UserAPIView, ProjectAPIView, IssueAPIView, CommentAPIView, ContributorAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register(r'signup',UserAPIView, basename="signup")
router.register(r"projects", ProjectAPIView)

project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
project_router.register(r"issues", IssueAPIView, basename="issues")
project_router.register(r'contributors', ContributorAPIView, basename='contributors')
issue_router = routers.NestedSimpleRouter(project_router, r"issues", lookup="issue")
issue_router.register(r"comments", CommentAPIView, basename="comments")
issue_router.register(r"contributors", ContributorAPIView, basename="test")


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

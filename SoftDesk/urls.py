from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from web.views import UserAPIView, ProjectAPIView, IssueAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()

router.register("signup",UserAPIView, basename="signup")
router.register("project", ProjectAPIView, basename="project")
router.register("issues", IssueAPIView, basename="issue")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

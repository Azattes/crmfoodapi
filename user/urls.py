from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UsersAPIView, RegistrationAPIView, LoginAPIView, RoleAPIView, RoleDetail, UsersDetail, ChangePasswordView

app_name = 'user'
urlpatterns = [
    path('user/reg', RegistrationAPIView.as_view()),
    path('user/log', LoginAPIView.as_view()),
    path('user/', UsersAPIView.as_view()),
    path('user/<int:pk>', UsersDetail.as_view()),
    path('role/', RoleAPIView.as_view()),
    path('role/<int:pk>', RoleDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('changepassword/', ChangePasswordView.as_view()),
]
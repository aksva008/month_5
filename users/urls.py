from django.urls import path
from users.views import AuthorizationAPIView, RegistrationAPIView, ConfirmUserAPIView
urlpatterns = [
	path('register/', RegistrationAPIView.as_view()),
	path('autherization/', AuthorizationAPIView.as_view()),
	path('confirm/', ConfirmUserAPIView.as_view())
]
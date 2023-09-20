from django.urls import path
from .views import SignUpView, profile_details

urlpatterns = [
	path('signup/', SignUpView.as_view(), name = 'signup'),
	path('profile_details/<int:pk>/', profile_details, name='profile_details'),


]
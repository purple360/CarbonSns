# pages/urls.py
from django.urls import path
from .views import HomePageView, landing_page

urlpatterns = [
	path('home/', HomePageView.as_view(), name='home'),
    path('', landing_page.as_view(), name='landing_page'),
    
    # Add this line for the homepage
# Add other URL patterns for your "pages" app here if needed
]

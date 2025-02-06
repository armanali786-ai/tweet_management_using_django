from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),  # List all tweets
    path("create/", views.tweet_create, name="tweet_create"),  # Create a tweet
    path("<int:tweet_id>/edit/", views.tweet_edit, name="tweet_edit"),  # Edit a tweet
    path("<int:tweet_id>/delete/", views.tweet_delete, name="tweet_delete"),  # Delete a tweet
    path("<int:tweet_id>/confirm_delete/", views.tweet_confirm_delete, name="tweet_confirm_delete"),  # Confirmation page
    path("registration/", views.registration, name="registration"),
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    
]

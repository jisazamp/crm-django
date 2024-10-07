from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("client/<int:pk>", views.client_details, name="client"),
    path("client/create", views.create_client, name="create_client"),
    path("client/<int:pk>/update", views.update_client, name="update_client"),
    path("client/<int:pk>/delete", views.delete_client, name="delete_client")
]

from django.urls import path
from .views import (
    home,
    about,
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoUpdateView,
    ProductoDeleteView,
)

urlpatterns = [
    path("", ProductoListView.as_view(), name="home"),
    path("about/", about, name="about"),
    path("create/",ProductoCreateView.as_view(), name="create_productos"),
    path("productos/<int:pk>",ProductoDetailView.as_view(), name="detail_productos"),
    path("producto/actualizacion/<int:pk>",ProductoUpdateView.as_view(), name="update_productos"),
    path("producto/delete/<int:pk>",ProductoDeleteView.as_view(), name="delete_productos"),
]



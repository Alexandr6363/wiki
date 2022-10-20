from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("add_page/", views.add_page, name="add_page"),
    path("random_page/", views.random_page, name="random_page"),
    path("<str:title>/", views.get_page, name="get_page"),
    path("search_page/", views.search_page, name="search_page"),
]

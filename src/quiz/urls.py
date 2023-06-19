from django.urls import path

from quiz.views import IndexView, CategoriesView

app_name = "quiz"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/", CategoriesView.as_view(), name="categories"),
    ]

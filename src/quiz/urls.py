from django.urls import path

from quiz.views import CategoryDetailView, IndexView

app_name = "quiz"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="categories"),
]

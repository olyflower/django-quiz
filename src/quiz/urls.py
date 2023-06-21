from django.urls import path

from quiz.views import (CategoryDetailView, IndexView, QuizDetailView,
                        ResultView, SubmitQuizView)

app_name = "quiz"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="categories"),
    path("quiz/<int:pk>/", QuizDetailView.as_view(), name="quiz"),
    path("submit/<int:quiz_pk>/", SubmitQuizView.as_view(), name="submit"),
    path("result/<int:quiz_pk>/", ResultView.as_view(), name="result"),
]

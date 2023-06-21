from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, TemplateView

from quiz.models import Category, Choice, Quiz, Result


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryDetailView(LoginRequiredMixin, DetailView):
    login_url = "account:login"
    redirect_field_name = "index"
    template_name = "quiz/categories.html"
    model = Category


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz.html"
    context_object_name = "quiz"


class SubmitQuizView(View):
    def post(self, request, quiz_pk):
        quiz = get_object_or_404(Quiz, pk=quiz_pk)
        user = request.user
        user_answers = {}
        for question in quiz.questions.all():
            answer_key = f"question_{question.pk}"
            selected_choice = request.POST.get(answer_key)
            user_answers[question.pk] = selected_choice

        total_questions = quiz.questions.count()
        correct_answers = sum(
            Choice.objects.filter(pk=user_answers.get(question.pk), question=question, is_correct=True).exists()
            for question in quiz.questions.all()
        )

        percentage = (correct_answers / total_questions) * 100

        result = Result(quiz=quiz, user=user, score=correct_answers)
        result.save()

        context = {
            "quiz": quiz,
            "correct_answers": result.score,
            "total_questions": total_questions,
            "percentage": percentage,
        }
        return render(request, "quiz/result.html", context)


class ResultView(View):
    def get(self, request, quiz_pk):
        quiz = get_object_or_404(Quiz.objects.select_related("quiz"), pk=quiz_pk)
        user = request.user
        result = get_object_or_404(Result, quiz=quiz, user=user)

        total_questions = quiz.questions.count()
        percentage = (result.score / total_questions) * 100

        context = {
            "quiz": quiz,
            "result": result,
            "percentage": percentage,
        }
        return render(request, "quiz/result.html", context)

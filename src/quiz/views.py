from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, TemplateView

from quiz.models import Category


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoryDetailView(DetailView):
    redirect_field_name = "index"
    template_name = "quiz/categories.html"
    model = Category

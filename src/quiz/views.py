from django.views.generic import TemplateView, ListView

from quiz.models import Category


class IndexView(TemplateView):
    template_name = "../templates/index.html"
    http_method_names = ["get"]
    extra_context = {"site_name": "Craft-Market"}


class CategoriesView(ListView):
    redirect_field_name = "index"
    template_name = "quiz/categories.html"
    model = Category

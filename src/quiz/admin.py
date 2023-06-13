from django.contrib import admin

from quiz.models import Question, Quiz, Result, Choice, Category

admin.site.register([Quiz, Question, Result, Choice, Category])

from django.forms import CharField
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from account.models import Customer
from quiz.models import Choice, Question, Quiz


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "is_staff")


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "text", "is_correct")


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "order_number", "text", "choices")


class QuizSerializer(ModelSerializer):
    level = SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ("id", "title", "description", "level", "questions_count")

    def get_level(self, obj):
        return obj.get_level_display()

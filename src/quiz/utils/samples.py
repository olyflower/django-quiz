from quiz.models import Category, Question, Quiz


def sample_quiz(title, **params):
    default = {"description": "Some description", "category": Category.objects.create()}
    default.update(params)
    return Quiz.objects.create(title=title, **default)


def sample_question(quiz, order_number, **params):
    default = {
        "text": "Some text",
    }
    default.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **default)

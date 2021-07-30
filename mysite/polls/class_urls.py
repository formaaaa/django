from django.urls import path

from polls import class_views

app_name = "class_polls"

urlpatterns = [
    path("poll-class-view/", class_views.PollView.as_view(), name="poll-class-view"),
    path("question-class-view/", class_views.QuestionView.as_view(), name="question-class-view"),
    path("answer-class-view/", class_views.AnswerView.as_view(), name="answer-class-view"),
]

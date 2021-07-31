from django.urls import path

from polls import class_views

app_name = "class_polls"

urlpatterns = [
    path("poll-class-view/", class_views.PollView.as_view(), name="poll-class-view"),
    path("poll-class-form-view/", class_views.PollFormView.as_view(), name="poll-class-form-view"),
    path("question-class-view/", class_views.QuestionView.as_view(), name="question-class-view"),
    path("question-class-form-view/", class_views.QuestionFormView.as_view(), name="question-class-form-view"),
    path("question-class-detail-view/<pk>/",
         class_views.QuestionDetailView.as_view(),
         name="question-class-detail-view"),
    path("question-class-update-view/<pk>/",
         class_views.QuestionUpdateView.as_view(),
         name="question-class-update-view"),
    path("question-class-delete-view/<pk>/",
         class_views.QuestionDeleteView.as_view(),
         name="question-class-delete-view"),
    path("answer-class-view/", class_views.AnswerView.as_view(), name="answer-class-view"),
    path("answer-class-form-view/", class_views.AnswerFormView.as_view(), name="answer-class-form-view"),
]
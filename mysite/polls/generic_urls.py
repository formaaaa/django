from django.urls import path

from polls import generic_views

app_name = "generic_polls"
urlpatterns = [
    path('poll-template-view/', generic_views.PollTemplateView.as_view(), name="poll-template-view"),
    path('poll-list-view/', generic_views.PollListView.as_view(), name="poll-list-view"),
    path('poll-form-view/', generic_views.PollFormView.as_view(), name="poll-form-view"),
    path('answer-template-view/', generic_views.AnswerTemplateView.as_view(), name="answer-template-view"),
    path('answer-list-view/', generic_views.AnswerListView.as_view(), name="answer-list-view"),
    path('answer-form-view/', generic_views.AnswerFormView.as_view(), name="form-list-view"),
    path('question-template-view/', generic_views.QuestionTemplateView.as_view(), name="question-template-view"),
    path('question-list-view/', generic_views.QuestionListView.as_view(), name="question-list-view"),
    path('question-form-view/', generic_views.QuestionFormView.as_view(), name="question-form-view"),
]
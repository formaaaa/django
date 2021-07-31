from django.urls import path
from polls import generic_views

app_name = "generic_polls"
urlpatterns = [
    path('poll-template-view/', generic_views.PollTemplateView.as_view(), name="poll-template-view"),
    path('poll-list-view/', generic_views.PollListView.as_view(), name="poll-list-view"),
    path('poll-form-view/', generic_views.PollFormView.as_view(), name="poll-form-view"),
    path('poll-create-view/', generic_views.PollCreateView.as_view(), name="poll-create-view"),
    path('poll-detail-view/<pk>/', generic_views.PollDetailView.as_view(), name="poll-detail-view"),
    path('poll-update-view/<pk>/', generic_views.PollUpdateView.as_view(), name="poll-update-view"),
    path('poll-delete-view/<pk>/', generic_views.PollDeleteView.as_view(), name="poll-delete-view"),

    path('answer-template-view/', generic_views.AnswerTemplateView.as_view(), name="answer-template-view"),
    path('answer-list-view/', generic_views.AnswerListView.as_view(), name="answer-list-view"),
    path('answer-form-view/', generic_views.AnswerFormView.as_view(), name="answer-form-view"),
    path('answer-create-view/', generic_views.AnswerCreateView.as_view(), name="answer-create-view"),
    path('answer-detail-view/<pk>/', generic_views.AnswerDetailView.as_view(), name="answer-detail-view"),
    path('answer-update-view/<pk>/', generic_views.AnswerUpdateView.as_view(), name="answer-update-view"),
    path('answer-delete-view/<pk>/', generic_views.AnswerDeleteView.as_view(), name="answer-delete-view"),

    path('question-template-view/', generic_views.QuestionTemplateView.as_view(), name="question-template-view"),
    path('question-list-view/', generic_views.QuestionListView.as_view(), name="question-list-view"),
    path('question-form-view/', generic_views.QuestionFormView.as_view(), name="question-form-view"),
    path('question-create-view/', generic_views.QuestionCreateView.as_view(), name="question-create-view"),
    path('question-detail-view/<pk>/', generic_views.QuestionDetailView.as_view(), name="question-detail-view"),
    path('question-update-view/<pk>/', generic_views.QuestionUpdateView.as_view(), name="question-update-view"),
    path('question-delete-view/<pk>/', generic_views.QuestionDeleteView.as_view(), name="question-delete-view"),

]

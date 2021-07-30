from django.urls import path

from polls import views

app_name = "polls"

urlpatterns = [
    path('hello/<int:year>/', views.hello),
    path('hello2/', views.hello2),
    path('hello-adjective/<s0>/', views.hello_adjectives),
    path('animals/', views.animals),
    path('polls/', views.polls, name="polls"),
    path('questions/', views.questions, name="questions"),
    path('answers/', views.answers, name="answers"),
    path('index/', views.index, name="index"),
    path('my-name-form/', views.get_name, name="my-name-form"),
    path('poll-form/', views.poll_form, name="poll-form"),
    path('question-form/', views.question_form, name="question-form"),
    path('answer-form/', views.answer_form, name="answer-form"),
]

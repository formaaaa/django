from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from polls.forms import QuestionForm, AnswerForm, PollForm
from polls.models import Question, Poll, Answer


class QuestionFormView(FormView):
    template_name = 'form.html'
    form_class = QuestionForm
    success_url = reverse_lazy("generic_polls: question-list-view")

    def form_valid(self, form):
        question_passed_in_form = form.cleaned_data["question_text"]
        date_passed_in_form = form.cleaned_data["pub_date"]
        poll_passed_in_form = form.cleaned_data["poll"]
        Question.objects.create(
            question_text=question_passed_in_form,
            pub_date=date_passed_in_form,
            poll=poll_passed_in_form
        )
        return HttpResponseRedirect(self.get_success_url())


class AnswerFormView(FormView):
    template_name = 'form.html'
    form_class = AnswerForm
    success_url = reverse_lazy("generic_polls: answer-list-view")

    def form_valid(self, form):
        answer_text_in_form = form.cleaned_data["answer_text"]
        question_passed_in_form = form.cleaned_data["question"]
        Question.objects.create(
            answer_text=answer_text_in_form,
            question=question_passed_in_form,
        )
        return HttpResponseRedirect(self.get_success_url())


class PollFormView(FormView):
    template_name = 'form.html'
    form_class = PollForm
    success_url = reverse_lazy("generic_polls: poll-list-view")

    def form_valid(self, form):
        name_passed_in_form = form.cleaned_data["name"]
        Question.objects.create(name=name_passed_in_form)
        return HttpResponseRedirect(self.get_success_url())


class PollTemplateView(TemplateView):
    template_name = "polls.html"
    extra_context = {"polls": Poll.objects.all()}


class PollListView(ListView):
    template_name = "list.html"
    model = Poll


class AnswerTemplateView(TemplateView):
    template_name = "answers.html"
    extra_context = {"answers": Answer.objects.all()}


class AnswerListView(ListView):
    template_name = "list.html"
    model = Answer


class QuestionTemplateView(TemplateView):
    template_name = "questions.html"
    extra_context = {"questions": Question.objects.all()}


class QuestionListView(ListView):
    template_name = "list.html"
    model = Question

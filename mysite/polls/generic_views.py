from django.views.generic import FormView, ListView, TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

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
        Answer.objects.create(
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
        Poll.objects.create(name=name_passed_in_form)
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


class QuestionCreateView(CreateView):
    model = Question
    template_name = "form.html"
    # fields = "__all__"
    success_url = reverse_lazy("generic_polls:question-list-view")
    form_class = QuestionForm  #musi być klasą dziedziczącą po ModelForm






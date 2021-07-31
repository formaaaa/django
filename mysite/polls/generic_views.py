from django.views.generic import (
    FormView,
    ListView,
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from polls.forms import QuestionForm, AnswerForm, PollForm
from polls.models import Question, Poll, Answer


class PollTemplateView(TemplateView):
    template_name = "polls.html"
    extra_context = {"polls": Poll.objects.all()}


class PollListView(ListView):
    template_name = "list.html"
    model = Poll


class PollFormView(FormView):
    template_name = 'form.html'
    form_class = PollForm
    success_url = reverse_lazy("generic_polls: poll-list-view")

    def form_valid(self, form):
        name_passed_in_form = form.cleaned_data["name"]
        Poll.objects.create(name=name_passed_in_form)
        return HttpResponseRedirect(self.get_success_url())


class PollCreateView(CreateView):
    model = Poll
    template_name = "form.html"
    success_url = reverse_lazy("generic_polls:poll-list-view")
    form_class = PollForm



class PollDetailView(DetailView):
    model = Poll
    template_name = "poll.html"


class PollUpdateView(UpdateView):
    model = Poll
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("generic_polls:poll-list-view")


class PollDeleteView(DeleteView):
    model = Poll
    template_name = "delete.html"
    success_url = reverse_lazy("generic_polls:poll-list-view")


class QuestionTemplateView(TemplateView):
    template_name = "questions.html"
    extra_context = {"questions": Question.objects.all()}


class QuestionListView(ListView):
    template_name = "list.html"
    model = Question


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


class QuestionCreateView(CreateView):
    model = Question
    template_name = "form.html"
    # fields = "__all__"
    success_url = reverse_lazy("generic_polls:question-list-view")
    form_class = QuestionForm  # musi być klasą dziedziczącą po ModelForm


class QuestionDetailView(DetailView):
    model = Question
    template_name = "question.html"


class QuestionUpdateView(UpdateView):
    model = Question
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("generic_polls:question-list-view")


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "delete.html"
    success_url = reverse_lazy("generic_polls:question-list-view")


class AnswerTemplateView(TemplateView):
    template_name = "answers.html"
    extra_context = {"answers": Answer.objects.all()}


class AnswerListView(ListView):
    template_name = "list.html"
    model = Answer


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


class AnswerCreateView(CreateView):
    model = Answer
    template_name = "form.html"
    success_url = reverse_lazy("generic_polls:answer-list-view")
    form_class = AnswerForm


class AnswerDetailView(DetailView):
    model = Answer
    template_name = "answer.html"


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("generic_polls:answer-list-view")


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = "delete.html"
    success_url = reverse_lazy("generic_polls:answer-list-view")

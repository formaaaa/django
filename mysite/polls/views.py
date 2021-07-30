from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from polls.forms import NameForm, PollForm, QuestionForm, AnswerForm
from polls.models import Poll, Question, Answer


def index(request):
    return render(
        request,
        template_name="index.html"
    )


def hello(request, year):
    return HttpResponse(f"Hello darkness my old friend! {year}")


def hello2(request):
    year = request.GET.get("year", "NO YEAR")
    return HttpResponse(f"Hello darkness my old friend! {year}")


def hello_adjectives(request, s0):
    s1 = request.GET.get("s1", "")
    return render(
        request,
        template_name="hello.html",
        context={"adjectives": [s0, s1, "beautiful", "pretty"]}
    )


def animals(request):
    animals = request.GET.get("animals", "")
    animals_list = animals.split(",")
    return render(
        request,
        template_name="my_template.html",
        context={"animals": animals_list}
    )


def polls(request):
    return render(
        request,
        template_name="polls.html",
        context={"polls": Poll.objects.all()}
    )


def questions(request):
    return render(
        request,
        template_name="questions.html",
        context={"questions": Question.objects.all()}
    )


def answers(request):
    return render(
        request,
        template_name="answers.html",
        context={"answers": Answer.objects.all()}
    )


def get_name(request):
    form = NameForm(request.POST or None)
    if form.is_valid():
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        name_passed_in_form = form.cleaned_data["name"]
        Poll.object.create(name=name_passed_in_form)
        return redirect('generic_polls:poll_list_view')
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question_passed_in_form = form.cleaned_data["question_text"]
        date_passed_in_form = form.cleaned_data["pub_date"]
        poll_passed_in_form = form.cleaned_data["poll"]
        Question.objects.create(
            question_text=question_passed_in_form,
            pub_date=date_passed_in_form,
            poll=poll_passed_in_form)
        return redirect('generic_polls:question_list_view')
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        answer_text_in_form = form.cleaned_data["answer_text"]
        question_passed_in_form = form.cleaned_data["question"]
        Answer.objects.create(
            answer_text=answer_text_in_form,
            question=question_passed_in_form)
        return redirect('generic_polls:answer_list_view')
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )
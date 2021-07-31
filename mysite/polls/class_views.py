from django.shortcuts import render, redirect
from django.views import View

from polls.models import Poll, Question, Answer
from polls.forms import AnswerForm, QuestionForm, PollForm


class PollView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls.html",
            context={"polls": Poll.objects.all()}
        )


class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="questions.html",
            context={"questions": Question.objects.all()}
        )


class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="answers.html",
            context={"answers": Answer.objects.all()}
        )


# class PollFormView(View):
#     form_class = PollForm
#     template_name = "form.html"
#
#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             name_passed_in_form = form.cleaned_data["name"]
#             Poll.object.create(name=name_passed_in_form)
#             return redirect('class_polls:poll-class-view')
#         return render(request, self.template_name, context={"form": form})
#
#
# class AnswerFormView(View):
#     form_class = AnswerForm
#     template_name = "form.html"
#
#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             answer_text_in_form = form.cleaned_data["answer_text"]
#             question_passed_in_form = form.cleaned_data["question"]
#             Answer.objects.create(
#                 answer_text=answer_text_in_form,
#                 question=question_passed_in_form)
#             return redirect('class_polls:answer-class-view')
#         return render(request, self.template_name, {"form": form})
#
#     class AnswerFormView(View):
#         def get(self, request):
#             form = AnswerForm()
#             return
#
#
# class QuestionFormView(View):
#     form_class = QuestionForm
#     template_name = "form.html"
#
#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, {"form": form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             question_passed_in_form = form.cleaned_data["question_text"]
#             date_passed_in_form = form.cleaned_data["pub_date"]
#             poll_passed_in_form = form.cleaned_data["poll"]
#             Question.objects.create(
#                 question_text=question_passed_in_form,
#                 pub_date=date_passed_in_form,
#                 poll=poll_passed_in_form)
#             return redirect('class_polls:question-class-view')
#         return render(request, self.template_name, {"form": form})
#

class PollFormView(View):
    def get(self, request):
        form = PollForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = PollForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            Poll.objects.create(name=name)
            return redirect("class_polls:poll-class-view")
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class AnswerFormView(View):
    def get(self, request):
        form = AnswerForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text_passed_in_form = form.cleaned_data["answer_text"]
            question_passed_in_form = form.cleaned_data["question"]
            Answer.objects.create(
                answer_text=answer_text_passed_in_form,
                question=question_passed_in_form
            )
            return redirect("class_polls:answer-class-view")
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionFormView(View):
    def get(self, request):
        form = QuestionForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text_passed_in_form = form.cleaned_data["question_text"]
            pub_date_passed_in_form = form.cleaned_data["pub_date"]
            poll_passed_in_form = form.cleaned_data["poll"]
            Question.objects.create(
                question_text=question_text_passed_in_form,
                pub_date=pub_date_passed_in_form,
                poll=poll_passed_in_form
            )
            return redirect("class_polls:question-class-view")
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionDetailView(View):
    def get(self, request, pk):
        return render(
            request,
            template_name='question.html',
            context={"question": Question.objects.get(pk=pk)}
        )
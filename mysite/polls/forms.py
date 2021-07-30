import datetime
import pytz
from django import forms
from django.core.exceptions import ValidationError
from polls.models import Poll, Question


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must start with a capital letter")


def lowercase_validator(value):
    if value.isupper():
        raise ValidationError("Value must be lowercase")


class PastDateField(forms.DateTimeField):
    def validate(self, value):
        super().validate(value)
        if value >= datetime.datetime.today().replace(tzinfo=pytz.UTC):
            raise ValidationError("Only past dates allowed")


class LowerCaseLetterField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if value[0].isupper():
            raise ValidationError("Value must start with a lower letter")


class NameForm(forms.Form):
    name = forms.CharField(max_length=20)
    birth_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'eg.2006-10-25 14:30:59'}))


class PollForm(forms.Form):
    name = LowerCaseLetterField(max_length=128)

    def clean_name(self):
        return self.cleaned_data["name"].upper()


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=128, validators=[capitalized_validator])
    pub_date = PastDateField(widget=forms.TextInput(attrs={'placeholder': 'eg.2006-10-25 14:30:59'}))
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())

    def clean_question_text(self):
        return self.cleaned_data["question_text"].lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data["question_text"][0] == "a" and cleaned_data["pub_date"].year < 2000:
                self.add_error("question_text", "Can't start with an 'a'")
                self.add_error("pub_date", "Can't be a date before 2000")
                raise ValidationError("Form invalid. Correct errors and submit again")
            if (
                    cleaned_data["question_text"][0] == "w" and
                    cleaned_data["pub_date"] < datetime.datetime.today().replace(tzinfo=pytz.UTC)
            ):
                self.add_error("question_text", "Can't start with an 'w'")
                self.add_error("pub_date", "Can't be a date from past")
                raise ValidationError("Form invalid. Correct errors and submit again")
        return cleaned_data


class AnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=128, validators=[lowercase_validator])
    question = forms.ModelChoiceField(queryset=Question.objects.all())

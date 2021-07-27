from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=128)


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)



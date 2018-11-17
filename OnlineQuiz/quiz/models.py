# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=100,default="")
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200,default="")
    option1 = models.CharField(max_length=50,default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    quiz = models.ForeignKey(Quiz,on_delete=CASCADE, null=True)

    def __unicode__(self):
        return self.question


class Score(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
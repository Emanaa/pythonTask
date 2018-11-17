# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from quiz.models import Question, Quiz
from quiz.serializer import QuestionSerializer, QuizSerializer


# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        return render(request,"quiz.html")
    return render(request,"index.html")

@login_required()
def get_data(request):
    return render(request,"quiz.html")


#view for creating user
def create_user(request):
    if request.method == 'POST':
        name =  request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(name,email,password)
    return render(request,"index.html")

#view for logging in
def log_in(request):
    
    if request.method == 'POST':
       
        username = request.POST.get("username")
        password  = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse("success")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid credentials")
@login_required()
def log_out(request):
    logout(request)
    return render(request,"index.html")



#viewsets for rest_framework
class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(quiz_id = 1)
    def get_queryset(self,request):
        return Question.objects.filter(quiz_id=self.kwargs.get('pk'))
        user_choice = request.POST.get('choice1')
        qid = request.POST.get('question')
        correct_answer = request.POST.get('answer')
        if user_choice == correct_answer:
            s = Score(question_id=qid, score=1, user_id=request.user.id)
            s.save()
        else:
            s = Score(question_id=qid, score=0, user_id=request.user.id)
            s.save()

        question_already_played = Score.objects.values_list('question')
   
        question_not_played = Question.objects.filter(quiz='iq').exclude(id__in=question_already_played)[:1]
  
        if question_not_played:
            context = {'sq': question_not_played}
            return render(request, 'quiz.html', context)
        else:
            scores = Score.objects.all()
            total = sum([sc.score for sc in scores])
            context = {'score': scores, 'total': total}
            return render(request, 'quiz.html', context)





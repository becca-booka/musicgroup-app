# reusing code from previous tasks
# had help from djangocentral.com, https://djangocentral.com/building-a-blog-application-with-django/

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post


def user_login(request):
    return render(request, 'login.html')



def authenticate_user(request):
    username= request.POST['username']
    password= request.POST['password']
    user= authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('angelfire:register')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('angelfire:index')
        )


def register(request):
    return render(request, 'register.html')



def register_user(request):
    username= request.POST['username']
    password= request.POST['password']

    if 'first_name' in request.POST:
        first_name= request.POST['first_name']
    else:
        first_name=''
        last_name=''
        email=''

    user=authenticate(username=username, password=password)
    if user is None:
        user= User.objects.create_user(
            username, first_name, password)
        login(request, user)
        return HttpResponseRedirect(reverse('angelfire:index'))
    else:
        return render(request, 'register.html', {
            'error_message': "user already exists"
        })            


def logout_request(request):
    logout(request)
    return render(request, 'logout.html')



def index(request):
    template= loader.get_template('homepage.html')
    return HttpResponse(template.render())


def merch(request):
    
    if request.user.is_authenticated:

        template= loader.get_template('merchpage.html')
        return HttpResponse(template.render())
    
    else:
        return HttpResponseRedirect(
            reverse('angelfire:login')
        )


class PostList(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = "blog.html"


class PostDetail(DetailView):
    model=Post
    template_name="post.html"    


def poll(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list': latest_question_list}
    return render(request, "polls.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})



def vote(request, question_id):
    
    if request.user.is_authenticated:

        question= get_object_or_404(Question, pk=question_id)
        try:
            selected_choice =  question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form
            return render(request, 'detail.html', {
               'question': question,
               'error_message': "You didn't select a choice."
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            
            return HttpResponseRedirect(
              reverse('angelfire:results', args=(question_id,))
            ) 
        
    else:return HttpResponseRedirect(
            reverse('angelfire:login')
        )


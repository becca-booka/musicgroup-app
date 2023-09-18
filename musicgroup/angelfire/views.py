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

# LOGIN METHOD
def user_login(request):

    """This method returns the login page for the Earth, Wind and Angelfire website
    """

    return render(request, 'login.html')

##########################################################################################

# AUTHENTICATION METHOD
def authenticate_user(request):
    """This method authenticates the user by using the python authentication method from the django
       authentication library
       
       If the user is not found in the database:
        * :returns: the registeration page
          :rtype: html
       
       If the user is found in the database:
        * :raises: login method
        * :returns: the homepage of the Earth, Wind and Angelfire website
          :rtype: html
    """
    
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

######################################################################################

# REGISTER METHOD
def register(request):
    """This method takes the user to the registration page
    
       :returns: The registration page
       :rtype: html
    """

    return render(request, 'register.html')

#####################################################################################

# REGISTER_USER METHOD
def register_user(request):
    """This method registers a new user and adds their details to the database
       
       :raises: the authentication method from the django authentication library
        
       If user is not found in the database:
        * :raises: create_user method
        * :raises: the login method
        * :returns: the homepage of the Earth, Wind and Angelfire website
          :rtype: html
    
       If the user is found in the database:
        * :raises error_message: user already in the database cannot create
        * :returns: the registration webpage
          :rtype: html
    """

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

#######################################################################################

# LOGOUT_REQUEST METHOD
def logout_request(request):
    """This method logs the user out of the website
    
       :raises: logout method
       
       :returns: the farewell page
       
       :rtype: html"""
    
    logout(request)
    return render(request, 'logout.html')

#################################################################################################

# INDEX METHOD
def index(request):
    """This method takes the user to the homepage of the Earth, Wind and Angelfire website
    
       :returns: the homepage of the Earth, Wind and Angelfire website
       
       :rtype: html
    """

    template= loader.get_template('homepage.html')
    return HttpResponse(template.render())

#####################################################################################################

# MERCHPAGE METHOD
def merch(request):
    """This method takes logged in users the the merchandise page
    
       If the user has been authenticated:
        * :returns: the merchandise webpage
          :rtype: html
          
       If the user has not been authenticated:
        * :returns: the login page of the Earth, Wind and Angelfire website
          :rtype: html
    """
    
    if request.user.is_authenticated:

        template= loader.get_template('merchpage.html')
        return HttpResponse(template.render())
    
    else:
        return HttpResponseRedirect(
            reverse('angelfire:login')
        )

#######################################################################################################

# POSTLIST CLASS
class PostList(ListView):
    """This class takes all the records stored in the post database and presents them as a list that is ordered
       by date publised in descending order, and displays them on the blog.html webpage.
    """

    queryset = Post.objects.all().order_by('-date')
    template_name = "blog.html"

#######################################################################################################

# POSTDETAIL CLASS
class PostDetail(DetailView):
    """This class presents the details of the selected record (blog entry) that is stored in the post database and displays 
       it on the post.html webpage.
    """

    model=Post
    template_name="post.html"    

########################################################################################################

# POLL METHOD
def poll(request):
    """This method displays all the records stored in the question database as a list
       that is ordered by date published in descending order and displayed on the polls.html webpage.
       
       :returns: The polls webpage of the Earth, Wind and Angelfire website
       :rtype: html
       :rtype: list
    """

    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list': latest_question_list}
    return render(request, "polls.html", context)

#########################################################################################################

# QUESTION DETAIL METHOD
def detail(request, question_id):
    """This method displays the details of the selected record (question) stored in the question database,
       along with their corresponding records (choices) stored in the choices database, and displays them
       on the detail.html webpage for the user to read the question and select one of the presented choices.

       :param: question_id key: database key for the question record
       
       :returns: The webpage that displays the selected question and its corresponding choices

       :rtype: html
       :rtype: str
    """

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

#################################################################################################################

# RESULTS METHOD
def results(request, question_id):
    """This method displays the results of the voting on the selected record (question) stored in the question database

       :param str Question: The question of the poll 
       :param: question_id key: database key for the question record
       
       :returns: The webpage that displays the results of the voting on the selected record (question) stored in the
        question databse

       :rtype: html
       :rtype: list
    """

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

######################################################################################################################

# VOTE METHOD
def vote(request, question_id):
    """This method collects votes for the selected poll
       
       :param: question_id key: database key for the question record
       
       If the user is logged in/has been authenticated:
        * :raises: keyError: Error is raised if user does not select a choice
        * :returns: input for the results method 

       If the user is not logged in/has not been authenticated:
        * :returns: the login webpage
          :rtype: html
       """
    
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


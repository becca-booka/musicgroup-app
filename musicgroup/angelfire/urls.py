# reusing code from previous tasks
# had some help from djangocentral.com, https://djangocentral.com/building-a-blog-application-with-django/
from django.urls import path, include, re_path
from . import views


app_name = 'angelfire'
urlpatterns=[
    path('', views.index, name='index'),
    path('merch/', views.merch, name='merch'),
    path('polls/', views.poll, name='polls'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.user_login, name = 'login'),
    path('authenticate_user/', views.authenticate_user, name= 'authenticate_user'),
    path('register/', views.register, name="register"),
    path('register_user/', views.register_user, name= 'register_user'),
    path("logout/", views.logout_request, name= "logout"),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<int:pk>/', views.PostDetail.as_view(), name='post'),
]
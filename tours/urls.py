from graphene_django.views import GraphQLView
from . import views
from django.urls import path
from .schema import schema
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login-user"),
   path('logout/', 
   auth_views.LogoutView.as_view(next_page='/login/'), name = 'logout-user'),
   path('graphql', GraphQLView.as_view(graphiql=True,schema=schema)),
]

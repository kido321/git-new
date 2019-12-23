from django.urls import path
from . import views

app_name="post"


urlpatterns= [
    path('test/', views.index, name="ostn"),
    path('h/', views.resp),
    path('userlist/', views.userss, name="postn"),
    #path('form/', views.Formnameview2),
    path('form2/', views.Fbview),
]


#urlpatterns= [
  #  url(r'test/', views.index, name="postn"),

#]

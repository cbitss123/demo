from django.urls import path,include
from blog import views

app_name='blog'

urlpatterns=[
    path('',views.blogHome,name='blogHome'),
    path('<int:pk>',views.blogPost,name='blogPost'),
    path('like', views.like_post, name="like_post"),

    
]
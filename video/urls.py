from django.urls import path
from . import views

app_name='video'
urlpatterns=[
    path('postComment',views.postComment, name="postComment"),
    path('category',views.newcategory_list, name='category'),
    path('<slug:article_slug>/',views.article_detail, name='article_detail'),
    path('<slug:category_slug>',views.category_view, name='category_view'),

    #API to post a comment
    ]
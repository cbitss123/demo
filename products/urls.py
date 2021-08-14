from django.urls import path,include
from . import views

app_name='products'
urlpatterns=[
            path('',views.category_list,name='category_list'),
            path('<slug:category_slug>/',views.product_list,name='product_list'),
]
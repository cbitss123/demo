from django.urls import path,include
from home import views
# from home.views import ProtectedView

app_name='home'
urlpatterns=[
    path("",views.home,name='home'),
    path("contact/",views.contact,name='contact'),
    # path("contact/",ProtectedView.as_view(),name='contact'),
    path("about/",views.about,name='about'),
    path("search/",views.search,name='search'),
]
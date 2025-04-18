from django.urls import path
from . import views
urlpatterns = [
    path('',views.demo,name="demo"),
    path('home',views.home,name='home'),
    path('shop',views.shop,name='shop'),
    path('deals',views.deals,name='deals'),
    path('contact',views.contact,name='contact'),
    
    

]

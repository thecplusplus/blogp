from django.urls import path
from . import views


urlpatterns = [
    path('<int:blog_id>/',views.details,name='details'),
    path('',views.home,name='home'),
]
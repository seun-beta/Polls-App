from . import views 
from django.urls import path

app_name = 'polls'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    



]
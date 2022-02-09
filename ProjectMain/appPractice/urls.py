from django.urls import path
from django.http import HttpResponse
from . import views

# def home(request):
#     return HttpResponse('Home page!')

# patternurls = [
urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room')
]
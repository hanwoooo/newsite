from django.urls import path
from . import views

urlpatterns =[
  # view 내부의 index를 보여준다.
  path('', views.index, name='index'),
]
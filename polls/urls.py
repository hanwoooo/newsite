from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
  # view 내부의 index를 보여준다.
  # ex: /polls/
  #path('', views.index, name='index'),
  # ex: /polls/5/
  #path('<int:question_id>/', views.detail, name='detail'),
  # ex /polls/5/results/
  #path('<int:question_id>/results/', views.results, name='results'),
  # ex /polls/5/vote
  #path('<int:question_id>/vote/', views.vote, name='vote'),

  # pk ==> 객체들을 구분할 수 있는 구분자 즉 question_id를 구분하여 들어가게끔 한다.
  path('', views.IndexView.as_view(), name='index'),

  path('<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
  
  path('<int:question_id>/vote/', views.vote, name='vote'),
  

]

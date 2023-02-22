from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.
# 밑의 index, results, detail코드를 generic를 사용하면 이렇게 간단하게 만들 수 있다. 
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  # queryset == 모델로부터 전달받은 객체목록
  def get_queryset(self):
    """Return the last five published questions.(not including those set to be published in the future)."""
    #1 test코드를 작성해서 버그를 확인하기전
    #return Question.objects.order_by('-pub_date')[:5]

    #2 
    # __lte ==> less than or equal 즉 timezon.now 보다 pub_date가 작거나 같은 Question을 받는다.
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name='polls/detail.html'  
  
  def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
  model=Question
  template_name='polls/results.html'

def vote(request, question_id):
  #1
  # return HttpResponse("You're voting on question %s" % question_id)
  
  #2
  question=get_object_or_404(Question, pk=question_id)
  try:
    #request.POST는 키로 전송된 자료에 접근할 수 있도록 해주는 사전같은 객체이다.
    selected_choice=question.choice_set.get(pk=request.POST['choice'])
    #선택된 설문id를 문자열로 반환하는 역할

    #예외 처리 --> choice가 없어서 키를 못찾는 경우 에러메세지를 띄운 후 다시 설문 폼을 반환하여준다.
  except(KeyError, Choice.DoesNotExist):
      return render(request, 'polls/detail.html', {
        'question':question,
        'error_message':"You didn't select a choice.",
      })
  else:
    selected_choice.votes +=1
    selected_choice.save()
    # POST데이터를 성공적으로 처리한 후에는 항상 Redirect를 해줘야한다. --> 습관을 들이자
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

  
# generic 사용 X
#def index(request):
  #1
  #return HttpResponse("Hello World!!")
  
  #2
  # question_list는 발행일순으로 정렬하여 5개까지 보여준다.
  # pub_date ==> 발행일(출판일)
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)
  
  #3
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # context = {
  #     'latest_question_list': latest_question_list,
  # }
  # return HttpResponse(template.render(context, request))
  
  #4
  #latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #context = {'latest_question_list': latest_question_list}
  #return render(request, 'polls/index.html', context)


#def detail(request, question_id):
  #1
  # return HttpResponse("You're looking at question %s." % question_id)

  #2 에러가 났을 때 Http404 사용
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
    
  # return render(request, 'polls/detail.html', {'question': question})

  # 3 에러가 났을 때 get_object_or_404를 사용
  #question = get_object_or_404(Question, pk=question_id)
  #return render(request, 'polls/detail.html', {'question': question})

#def results(request, question_id):
  #1
  # response = "You're looking at the results of question %s."
  # return HttpResponse(response % question_id)

  #2
  #question=get_object_or_404(Question, pk=question_id)
  #return render(request, 'polls/results.html', {'question':question})
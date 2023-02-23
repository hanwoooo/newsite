from django.db import models
# 시간을 나타내기 위해서 import함.
from django.utils import timezone
from django.contrib import admin
import datetime


# Create your models here.
#1
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('data published')

#   # 밑의 __str__ 함수를 통해 shell에서 원하는 문구를 볼 수 있다. 
#     def __str__(self):
#       return self.question_text

#     def was_published_recently(self):
#       #1
#       #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#       #2
#       now = timezone.now()
#       # timedelta ==> 두 시간사이의 차이를 알기 위해 사용하는 함수
#       # return의 값은 bool값이므로 이렇게 적어도 상관 없다
#       return now - datetime.timedelta(days=1) <= self.pub_date <= now

#2 decorator 사용한 Question class
class Question(models.Model):
    @admin.display(
      boolean=True,
      ordering='pub_date',
      description='Published recently?',
    )
    def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
from django.contrib import admin
from .models import Question, Choice

# 2.23 다시 오게 되면 여기 부분 에러코드 분석하고 고칠것! --> 2.24 해결!!
# 수십개의 필드가 있을 경우 폼을 fieldset으로 분할하는 것이 좋다. 

# Register your models here.
#1
# admin.site.register(Question)
# admin.site.register(Choice)

#2
# field를 재정렬 하여 커스터마이징하기
# class QuestionAdmin(admin.ModelAdmin):
#   fields = ['pub_date', 'question_text']
  
# admin.site.register(Question, QuestionAdmin)

#3
# class QuestionAdmin(admin.ModelAdmin):
#   fieldsets = [
#     (None, {'fields':['question_text']}),
#     ('Date information', {'fields': ['pub_date']}),
#   ]
# admin.site.register(Question, QuestionAdmin)

#4 #3에 choice 추가
#4-1 StackedInline을 TabularInlin으로 바꾸기
# StackedInline 대신에 TabularInline을 사용하면, 관련된 객체는 좀 더 조밀하고 테이블 기반 형식으로 표시된다.
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  fieldsets = [
    (None, {'fields':['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInline]
  search_fields = ['question_text']
  
  list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)
from django.contrib import admin
from quiz_data.models import Test, Question, Answer, QuestionType

admin.site.register(Test)

class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerInline]
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionType)

# Register your models here.

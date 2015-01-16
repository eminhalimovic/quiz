from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

class QuestionType(models.Model):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=2)
	
	def __unicode__(self):
		return self.name	
	
class Question(models.Model):
	name = models.CharField(max_length=1024)
	type = models.ForeignKey(QuestionType)
	test = models.ForeignKey(Test)
	
	def __unicode__(self):
		return self.name	
	
class Answer(models.Model):
	name = models.CharField(max_length=1024)
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.name	
	
class Attempt(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	
class AttemptLine(models.Model):
	attempt = models.ForeignKey(Attempt)
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Answer)
	
	

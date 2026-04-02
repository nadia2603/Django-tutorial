from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

# Charfield voor tesktvelden 
# Charfield vereist dat je een parameter meegeeft 
# DateTimeField voor datum-en tijdvelden 
# question_text en pub_date zijn de namen van het veld 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# De relatie wordt met behulp van ForeignKey gedefinieerd 
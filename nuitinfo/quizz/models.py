from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    explanation = models.CharField(max_length=3000)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=None, null=True)
    nb_votes = models.IntegerField()

    def __str__(self):
        return self.choice_text

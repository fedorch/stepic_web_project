from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name="q_to_u")
    likes = models.ManyToManyField(User, related_name="q_to_l")


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, related_name="a_to_q")
    author = models.ForeignKey(User, related_name="a_to_u")

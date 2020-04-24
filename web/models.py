from django.db import models

class Publication(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    text = models.TextField()

class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.TextField()
    date = models.DateTimeField()
    text = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.TextField()
    date = models.DateTimeField()
    text = models.TextField()
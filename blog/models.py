from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField()
    ques_expand=models.TextField()




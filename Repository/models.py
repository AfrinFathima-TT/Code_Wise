from django.db import models

# Create your models here.
"""
schema   : QuestionDb
Fields   : title,language,notes,difficulty_level,sample_input,
           sample_output,topic,published_date,is_active
"""

class QuestionsDb(models.Model):
    title = models.CharField(max_length = 200)

    LANGUAGE_CHOICES = (
        ("python","Python"),
        ("java","Java"),
        ("javascript","Javascript")
    )

    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")

    DIFFICULTY_CHOICES = (
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )

    difficulty_level =models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default="easy")

    topic = models.CharField(max_length=100)
    notes = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    sample_input = models.TextField()
    sample_output = models.TextField()
    is_active = models.BooleanField(default=True)


class SubmissionsDb(models.Model):

    question_id = models.IntegerField()

    answer = models.TextField()

    points = models.PositiveIntegerField(null=True)

    owner = models.CharField(max_length = 100)

    submission_date = models.DateTimeField(auto_now_add= True)

    remarks = models.TextField(null= True)

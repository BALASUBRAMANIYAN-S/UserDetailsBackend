from django.db import models

class student(models.Model):
    Exam = models.CharField(max_length=200)
    RollNumber = models.IntegerField()

    def __str__(self):
        return self.Exam

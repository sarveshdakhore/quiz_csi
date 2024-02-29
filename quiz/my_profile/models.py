from django.db import models

# Create your models here.
class Questions(models.Model):
    quiz = models.ForeignKey('quiz_creator.Quiz', on_delete=models.CASCADE)
    textbox = models.TextField()
    def __str__(self):
        return self.textbox
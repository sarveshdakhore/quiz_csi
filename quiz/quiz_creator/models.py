from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    from_time = models.DateTimeField(default=timezone.now)
    to_time = models.DateTimeField(default=timezone.now)
    owner = models.BooleanField(default=True)

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query} - {self.timestamp}"
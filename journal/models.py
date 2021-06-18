from django.db import models
from django.contrib.auth.models import User


class Journal(models.Model):
    title = models.CharField(max_length=50)
    journal_content = models.TextField()
    key_moments = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.title} - {self.date_created}"

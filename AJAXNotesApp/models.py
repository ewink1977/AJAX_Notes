from django.db import models

class Note(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

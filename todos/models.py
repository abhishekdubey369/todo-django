from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(verbose_name='Creation Time', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Last Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

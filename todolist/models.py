from django.db import models
import uuid


class ToDo(models.Model):
    task = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ["-created"]

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Task(models.Model):
    content = models.TextField(max_length=400, unique=True)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tag = models.ManyToManyField(
        Tag,
        related_name="tasks",
    )

    class Meta:
        ordering = ["done", "-datetime"]

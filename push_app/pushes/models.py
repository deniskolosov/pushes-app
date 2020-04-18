from django.db import models


class Options(models.Model):
    name = models.CharField(max_length=256)


class Pushes(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    is_sent = models.BooleanField(default=False)
    times_sent = models.BooleanField(default=0)

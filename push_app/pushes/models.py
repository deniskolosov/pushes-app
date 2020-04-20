from django.db import models


class Push(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(blank=True, null=True)
    is_sent = models.BooleanField(default=False)
    push_image = models.ImageField()
    times_sent = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Pushes"


class Option(models.Model):
    name = models.CharField(max_length=256)


from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.published_date:
            self.published_date = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



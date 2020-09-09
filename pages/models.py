from django.db import models

from ckeditor.fields import RichTextField

class Page(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

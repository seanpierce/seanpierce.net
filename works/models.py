from django.db import models

from ckeditor.fields import RichTextField

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = RichTextField()

    @property
    def slug(self):
        return self.title.replace(' ', '-').lower()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

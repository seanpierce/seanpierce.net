from statistics import mode
from django.db import models

from ckeditor.fields import RichTextField

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = RichTextField()
    year = models.IntegerField(default="")
    present = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

class WorkImage(models.Model):
    image = models.ImageField(upload_to='works/')
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

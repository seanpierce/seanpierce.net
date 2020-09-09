from django.db import models

from ckeditor.fields import RichTextField

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, blank=True)
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at',]

    def save(self, *args, **kwargs):
        self.slug = ''.join(char for char in self.title if char.isalnum())
        super(Work , self).save()


class WorkImage(models.Model):
    image = models.ImageField(upload_to='works/')
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

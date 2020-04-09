from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
#from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    img = models.ImageField(upload_to='news/', blank=True, null=True)
    slug = models.SlugField(max_length=250)
    publised = models.DateTimeField(default=timezone.now)

    def get_image(self):
        if self.img:
            return mark_safe(f"<img class='card-img-top' src='{self.img.url}' style='width:90px;'>")

    def __str__(self):
        return self.title

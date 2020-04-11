from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
#from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='news/', blank=True, null=True)
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        string_slug = self.title + '-' + str(self.pk)
        self.slug = slugify(string_slug)
        super(News, self).save(*args, **kwargs)

    def get_image(self):
        if self.img:
            return mark_safe(f"<img class='card-img-top' src='{self.img.url}' style='width:40px;'>")

    def __str__(self):
        return self.title

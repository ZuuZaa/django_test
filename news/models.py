from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from django.utils import timezone

#from ckeditor.fields import RichTextField

# Create your models here.
class NewsModel(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='news/', blank=True, null=True)
    slug = models.SlugField(max_length=250)
    published = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        choices=(
            ('az', "Az"),
            ('rus', "Rus"),
            ('en', "En")
        ),
        max_length=20,
        default='az',
    )

    def save(self, *args, **kwargs):
        string_slug = self.title + '-' + str(self.pk)
        self.slug = slugify(string_slug)
        super(NewsModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

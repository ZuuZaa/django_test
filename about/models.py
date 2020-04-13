from django.db import models

# Create your models here.
class About(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    language = models.CharField(
        choices=(
            ('az', "Az"),
            ('rus', "Rus"),
            ('en', "En")
        ),
        max_length=20,
        default='az',
    )

    def __str__(self):
        return self.description
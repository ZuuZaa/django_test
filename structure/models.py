from django.db import models

# Create your models here.
class Department(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
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
        return self.name

class Person(models.Model):

    full_name = models.CharField(max_length=250)
    role  = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
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
        return self.full_name

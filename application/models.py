from django.db import models

# Create your models here.
class Application(models.Model):

    request_type = models.CharField(
        choices=(
            ('complaint', "Complaint"),
            ('proposal', "Proposal"),
            ('application', "Application")
        ),
        max_length=20,
        default='aapplication',
    )
    department = models.CharField(max_length=250)
    subject = models.CharField(
        choices=(
            ('complaint', "Complaint"),
            ('proposal', "Proposal"),
            ('application', "Application")
        ),
        max_length=20,
        default='aapplication',
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.request_type


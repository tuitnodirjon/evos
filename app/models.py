from django.db import models

class Profile(models.Model):
    phone = models.CharField(max_length=12, null=True)
    full_name = models.CharField(max_length=355, null=True)
    token = models.CharField(max_length=455, null=True)

    def __str__(self):
        return self.phone



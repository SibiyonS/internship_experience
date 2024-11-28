from django.db import models

from django.db import models

class UserRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    domain = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    task_file = models.FileField(upload_to='tasks/', blank=True, null=True)
    task_status = models.BooleanField(default=False)
    certificate_issued = models.BooleanField(default=False)

    def __str__(self):
        return self.name


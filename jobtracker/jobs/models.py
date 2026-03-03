
from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Applied")
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.role}"

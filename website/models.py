
from django.db import models
import os

def upload_Certificate_to(instance, filename):
    return 'Certificate/{0}/{1}'.format(instance.enrollment_id, filename)

class Certificate(models.Model):
    enrollment_id = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    verified  = models.BooleanField(default=False)
    certificate = models.ImageField(upload_to=upload_Certificate_to, blank=True, null=True)


    
    

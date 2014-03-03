from django.db import models
from jsonfield import JSONField

class EncodingJob(models.Model):
    filename = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    urls = JSONField()
    created_at = models.DateTimeField(auto_now_add = True)

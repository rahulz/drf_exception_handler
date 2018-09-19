from django.db import models


class ErrorHash(models.Model):
    hash_code = models.IntegerField()
    error = models.TextField()
    http_status = models.IntegerField()
    exc_type = models.TextField()

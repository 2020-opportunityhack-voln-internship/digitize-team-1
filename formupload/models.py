from django.db import models


class Form(models.Model):
    """
    Model that contains a file that is uploaded to website
    """
    file_upload = models.FileField()

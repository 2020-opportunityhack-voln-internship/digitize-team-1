from django.db import models
from django.forms import forms

class PaperForm(models.Model):
    """
    Model for paper forms that will be uploaded to website
    """

    paper_form = models.ImageField(upload_to='paper_forms')
    title = models.CharField(max_length=100, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_trash = models.BooleanField(default=False)

    def __str__(self):
        return self.title



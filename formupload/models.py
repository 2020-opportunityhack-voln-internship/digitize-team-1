from django.db import models


class PaperForm(models.Model):
    """
    Model for paper forms that will be uploaded to website
    """

    paper_form = models.ImageField(upload_to='paper_forms')
    title = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.title


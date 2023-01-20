from django.db import models

# Create your models here.
class Pdf(models.Model):
    link = models.URLField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s" % (self.link, self.description)
    
class Outputtext(models.Model):
    urllink = models.URLField(max_length=255)
    urldes = models.CharField(max_length=255)

    def __str__(self):
        return "%s %s" % (self.urllink, self.urldes)
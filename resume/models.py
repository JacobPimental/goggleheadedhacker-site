from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Section(models.Model):
    header = models.CharField(max_length=50, unique=True)
    content = RichTextField()
    def __str__(self):
        return self.header

class Contact_Info(models.Model):
    method = models.CharField(max_length=50, unique=True)
    info = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.method
    def link(self):
        return '<a href="' + self.info +'">'+self.method+'</a>'

class Resume(models.Model):
    sections = models.ManyToManyField(Section, default=None, blank=True)
    contact_info = models.ManyToManyField(Contact_Info, default=None,
                                          blank=True)
    def links(self):
        string = ''
        for contact in self.contact_info.all():
            string += contact.link()
            string += '&emsp;|&emsp;'
        return str(string)


from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)
    def tag_link(self):
        return ("<a href='/blog/search/tag/" +
                self.tag_name + "/1'>" +
                self.tag_name + "</a>")
    def __str__(self):
        return self.tag_name

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.cat_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    tags = models.ManyToManyField(Tag, default=None)
    my_category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    default=None)
    pub_date = models.DateField(null=True)
    is_draft = models.BooleanField(default=True)
    views = models.IntegerField(default=0, null=True)

    @property
    def hash_value(self):
        return abs(hash(self.content))


    @property
    def list_tags(self):
        val = ''
        for tag in self.tags.all():
            print(tag.tag_link())
            val += tag.tag_link()
            val += ', '
        val = val[:-2]
        return val


    def description(self):
        paragraphs = self.content.split('\n')
        length = len(paragraphs[0])
        paragraphs[0] = paragraphs[0][:length-5]
        return(paragraphs[0]+'...'+'</p>')


    def __str__(self):
        return self.title

from django.db import models
# import datetime as dt
from tinymce.models import HTMLField

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank=True)



    def save_editor(self):
        self.save()


class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank=True)



    def save_editor(self):
        self.save()

class tags(models.Model):
    name = models.CharField(max_length =30)

class Admin(models.Model):
    title = models.CharField(max_length = 60)
    post = HTMLField()
    editor = models.ForeignKey('auth.User')
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add = True)
    article_image = models.ImageField(upload_to='articles/', blank=True)

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = HTMLField()
    editor = models.ForeignKey('User')
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add = True)
    article_image = models.ImageField(upload_to='articles/', blank=True)

    @classmethod
    def todays_news(cls):
        # today = dt.date.today()
        news = cls.objects.filter()
        return news

    # @classmethod
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news

class Meta:
    ordering = ['name']

    def __str__(self):
        return self.first_name

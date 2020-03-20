from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    slug = models.SlugField('SLUG',unique=True, allow_unicode=True, help_text='One Word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField("CREATE DATE", auto_now_add=True)
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True)
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User

import datetime
import tagging
from tagging.fields import TagField

class Category(models.Model):
    """Category model."""
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique=True)
 
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        db_table = 'blog_categories'
        ordering = ('title',)
 
    def __unicode__(self):
        return u'%s' % self.title
 
    @permalink
    def get_absolute_url(self):
        return ('blog_category_detail', None, {'slug': self.slug})

class Entry(models.Model):
    """Blog model."""
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=32)
    asset = models.TextField(blank=True, null=True, help_text='Image, video or link')
    body = models.TextField(help_text='Use <a href="http://markdownr.com/" target="_blank">Markdown</a>')
    tags = TagField()

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.headline

    def url(self):
        return "/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

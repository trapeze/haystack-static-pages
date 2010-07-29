from django.db import models
from django.template.defaultfilters import truncatewords_html
from django.utils.encoding import force_unicode
from django.utils.translation import get_language, ugettext_lazy as _


class StaticPage(models.Model):
    title = models.CharField(_('title'), max_length=255)
    url = models.URLField(_('url'), max_length=255)
    description = models.TextField(_('description'))
    content = models.TextField(_('content'))
    language = models.CharField(_('language'), max_length=5)
    
    class Meta:
        verbose_name = _('static page')
        verbose_name_plural = _('static pages')
    
    def __repr__(self):
        return '<StaticPage: %s -- %s>' % (self.url, truncatewords_html(self.content, 10))

    def __unicode__(self):
        return force_unicode(self.__repr__())
    
    def get_absolute_url(self):
        return self.url
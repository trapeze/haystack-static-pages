import urllib2

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse
from django.utils import translation
from django.utils.html import escape
from optparse import make_option

from BeautifulSoup import BeautifulSoup

from haystack_static_pages.models import StaticPage


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-p', '--port', action='store', dest='port', default=None,
            help='The port number to use for internal urls.'),
        make_option('-l', '--language', action='store', dest='language', default=None,
            help='The language to use when requesting the page'),
    )
    help = 'Setup static pages defined in HAYSTACK_STATIC_PAGES for indexing by Haystack'
    cmd = 'crawl_static_pages [-p PORT] [-l LANG]'
    
    def handle(self, *args, **options):
        if args:
            raise CommandError('Usage is: %s' % cmd)

        self.port = options.get('port')

        if self.port:
            if not self.port.isdigit():
                raise CommandError('%r is not a valid port number.' % self.port)
            else:
                self.port = int(self.port)

        count = 0

        self.language = options.get('language')

        if self.language:
            translation.activate(self.language)
        
        for url in settings.HAYSTACK_STATIC_PAGES:
            if not url.startswith('http://'):
                if self.port:
                    url = 'http://%s:%r%s' % (Site.objects.get_current().domain, self.port, reverse(url))
                else:
                    url = 'http://%s%s' % (Site.objects.get_current().domain, reverse(url))
            
            print 'Analyzing %s...' % url
            
            try:
                page = StaticPage.objects.get(url=url)
                print '%s already exists in the index, updating...' % url
            except StaticPage.DoesNotExist:
                print '%s is new, adding...' % url
                page = StaticPage(url=url)
                pass
            
            try:
                html = urllib2.urlopen(url)
            except urllib2.URLError:
                print "Error while reading '%s'" % url
                continue
            
            soup = BeautifulSoup(html)
            try:
                page.title = escape(soup.head.title.string)
            except AttributeError:
                page.title = 'Untitled'
            meta = soup.find('meta', attrs={'name': 'description'})
            if meta:
                page.description = meta.get('content', '')
            else:
                page.description = ''
            page.language = soup.html.get('lang', 'en')
            page.content = soup.prettify()
            page.save()
            count += 1

        print 'Crawled %d static pages' % count

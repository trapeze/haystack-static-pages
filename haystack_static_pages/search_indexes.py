from haystack import indexes
from haystack import site

from haystack_static_pages.models import StaticPage


class StaticPageIndex(indexes.SearchIndex):
    text = indexes.CharField(
        document=True, use_template=True, 
        template_name='staticpage_text.txt'
    )
    title = indexes.CharField(model_attr='title')
    url = indexes.CharField(model_attr='url')
    content = indexes.CharField(model_attr='content')
    description = indexes.CharField(model_attr='description')
    language = indexes.CharField(model_attr='language')


site.register(StaticPage, StaticPageIndex)

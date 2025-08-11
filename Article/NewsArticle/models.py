from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from django.db import models

class NewsArticlePage(Page):
    publication_date = models.DateField(db_index=True)
    summary = models.TextField()
    source_url = models.URLField("Source URL")

    content_panels = Page.content_panels + [
        FieldPanel('publication_date'),
        FieldPanel('summary'),
        FieldPanel('source_url'),
    ]
    class Meta:
        ordering = ['-publication_date']
    
class NewsListPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
class NewsListPage(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        queryset = NewsArticlePage.objects.live().order_by('-publication_date').specific()
        
        # Print the actual SQL query
        print(queryset.query)
        
        # Print dates from the queryset
        print("Dates from queryset:")
        for article in queryset:
            print(article.publication_date)
        
        context['news_articles'] = queryset
        return context        



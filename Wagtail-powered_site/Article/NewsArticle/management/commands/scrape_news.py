from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from NewsArticle.models import NewsArticlePage, NewsListPage
from datetime import datetime
from urllib.parse import urljoin
import requests

class Command(BaseCommand):
    help = "Scrape news articles from a website and save them as Wagtail pages"
    
    def handle(self, *args, **kwargs):
        base_url = 'https://www.bbc.com'
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")

        # Get the parent listing page
        parent = NewsListPage.objects.first()
        if not parent:
            self.stdout.write(self.style.ERROR("No NewsListPage found. Please create one in Wagtail admin."))
            return
        count  = 0
        for article in articles:
            if count >= 50:
                break
            title = article.find("h3").get_text(strip=True) if article.find("h3") else "No title"
            summary = article.find("p").get_text(strip=True) if article.find("p") else "No summary"
            raw_link = article.find("a")["href"] if article.find("a") and article.find("a").has_attr("href") else ""
            source_url = urljoin(base_url, raw_link)  # Makes sure URL is absolute
            publication_date = datetime.now()
            count += 1
            # Create and publish article
            new_article = NewsArticlePage(
                title=title,
                summary=summary,
                source_url=source_url,
                publication_date=publication_date,
            )

            parent.add_child(instance=new_article)
            new_article.save_revision().publish()

            self.stdout.write(self.style.SUCCESS(f"Added: {title}"))

        self.stdout.write(self.style.SUCCESS("Scraping complete!"))

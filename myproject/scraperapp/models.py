from django.db import models

class ScrapedURL(models.Model):
    url = models.URLField(max_length=200)
    scraped_content = models.TextField()  # Store the scraped data here
    
    def __str__(self):
        return self.url

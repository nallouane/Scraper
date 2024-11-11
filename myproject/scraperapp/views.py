from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import ScrapedURL
from scraper import scrape_first_thirty_characters

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        
        if url:
            # Scrape the content of the URL
            try:
                scraped = scrape_first_thirty_characters(url)
                ScrapedURL.objects.create(url=url, scraped_content=scraped)
            except Exception as e:
                return HttpResponseBadRequest(f"Error scraping the URL: {e}")
    
    all_data = ScrapedURL.objects.all()
    
    return render(request, 'home.html', {"all_data": all_data})

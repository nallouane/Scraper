from myproject.scraper import scrape_first_thirty_characters

# Define the URL you want to scrape
url = "https://en.wikipedia.org/wiki/Donald_Trump"

# Call the function and print the result
result = scrape_first_thirty_characters(url)
print("First five sentences from the page:")
print(result)

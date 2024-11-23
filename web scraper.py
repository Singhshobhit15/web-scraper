import requests

def fetchandsavetofile(url, filepath):
    # Step 1: Fetch the web page content
    r = requests.get(url)
    
    # Step 2: Open the file with 'utf-8' encoding and save the content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(r.text)

# Example URL to fetch
url = 'https://timesofindia.indiatimes.com/news'

# Save the web page content to a file
fetchandsavetofile(url, "data/times.html")

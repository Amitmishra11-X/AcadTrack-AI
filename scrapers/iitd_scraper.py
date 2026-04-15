import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_iitd():
    url = "https://home.iitd.ac.in/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching IIT Delhi: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []

    # Find all links (announcements)
    links = soup.find_all('a')

    keywords = ['recruitment', 'walk', 'jrf', 'project', 'faculty', 'intern']

    for link in links:
        text = link.get_text(strip=True).lower()
        href = link.get('href')

        if not text or not href:
            continue

        # Filter only job-related announcements
        if any(k in text for k in keywords):

            # Fix relative links
            if not href.startswith('http'):
                href = "https://home.iitd.ac.in/" + href

            jobs.append({
                'title': text,
                'institute': 'IIT Delhi',
                'deadline': 'Check link',
                'link': href,
                'category': None,
                'scraped_at': datetime.now().isoformat()
            })

    print(f"Found {len(jobs)} job-related announcements from IIT Delhi")
    return jobs

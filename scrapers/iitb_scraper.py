import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_iitb():
    url = "https://www.iitb.ac.in/en/careers"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching IIT Bombay: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    seen = set()   # 🔥 avoid duplicates

    keywords = ['recruitment', 'walk', 'jrf', 'project', 'faculty', 'intern']

    # 🔥 Target only meaningful sections
    for link in soup.select('a'):
        text = link.get_text(strip=True)
        href = link.get('href')

        if not text or not href:
            continue

        text_lower = text.lower()

        # 🔥 Filter job-related content only
        if any(k in text_lower for k in keywords):

            # 🔥 avoid duplicates
            if text_lower in seen:
                continue
            seen.add(text_lower)

            # 🔥 fix relative links
            if not href.startswith('http'):
                href = "https://www.iitb.ac.in" + href

            jobs.append({
                'title': text.strip(),
                'institute': 'IIT Bombay',
                'deadline': 'Check link',
                'link': href,
                'category': None,
                'scraped_at': datetime.now().isoformat()
            })

    print(f"Found {len(jobs)} job-related announcements from IIT Bombay")
    return jobs
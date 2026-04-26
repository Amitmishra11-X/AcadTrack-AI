import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_nitt():
    url = "https://www.nitt.edu/home/other/jobs/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"Error fetching NIT Trichy: {e}")
        return []

    soup = BeautifulSoup(res.text, 'html.parser')

    jobs = []
    seen = set()

    # 🔥 keywords to filter real job postings
    keywords = [
        'recruitment', 'project', 'jrf',
        'faculty', 'assistant', 'professor',
        'research', 'staff'
    ]

    links = soup.find_all('a')

    for link in links:
        text = link.get_text(strip=True)
        href = link.get('href')

        # skip empty
        if not text or not href:
            continue

        # skip very short / junk text
        if len(text) < 10:
            continue

        # filter job-related links
        if not any(k in text.lower() for k in keywords):
            continue

        # remove duplicates
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)

        # fix relative URLs
        if not href.startswith('http'):
            href = "https://www.nitt.edu" + href

        jobs.append({
            'title': text,
            'institute': 'NIT Trichy',
            'deadline': 'Check link',
            'link': href,
            'category': None,
            'scraped_at': datetime.now().isoformat()
        })

    print(f"Found {len(jobs)} jobs from NIT Trichy")
    return jobs
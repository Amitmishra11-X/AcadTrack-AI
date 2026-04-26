import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3

# disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def scrape_india_science():
    url = "https://www.indiascienceandtechnology.gov.in/listingpage/internships"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        res = requests.get(url, headers=headers, timeout=10, verify=False)
        res.raise_for_status()
    except Exception as e:
        print(f"Error fetching India Science portal: {e}")
        return []

    soup = BeautifulSoup(res.text, 'html.parser')

    jobs = []

    # 🔹 simple card selector (first visible items only)
    cards = soup.select('.view-content .views-row')

    for card in cards:
        title_tag = card.find('h3')
        title = title_tag.get_text(strip=True) if title_tag else None

        link_tag = card.find('a')
        link = link_tag['href'] if link_tag else None

        if link and not link.startswith('http'):
            link = "https://www.indiascienceandtechnology.gov.in" + link

        if title:
            jobs.append({
                'title': title,
                'institute': 'India Science Portal',
                'deadline': 'Check link',
                'link': link,
                'category': 'Internship',
                'scraped_at': datetime.now().isoformat()
            })

    print(f"Found {len(jobs)} internships from India Science portal")
    return jobs
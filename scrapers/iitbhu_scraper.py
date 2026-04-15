import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_iitbhu():
    url = "https://www.iitbhu.ac.in/positions"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching IIT BHU: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    rows = soup.select('table tr')

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) < 2:
            continue

        title = cols[0].get_text(strip=True)
        deadline = cols[-1].get_text(strip=True)

        link_tag = row.find('a')
        link = link_tag['href'] if link_tag else None

        if link and not link.startswith('http'):
            link = "https://www.iitbhu.ac.in" + link

        jobs.append({
            'title': title,
            'institute': 'IIT BHU',
            'deadline': deadline,
            'link': link,
            'category': None,
            'scraped_at': datetime.now().isoformat()
        })

    print(f"Found {len(jobs)} jobs from IIT BHU")
    return jobs
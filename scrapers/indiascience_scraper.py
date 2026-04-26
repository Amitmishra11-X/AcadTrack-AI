import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_india_science():
    url = "https://www.indiascienceandtechnology.gov.in/listingpage/internships"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"Error fetching India Science portal: {e}")
        return []

    soup = BeautifulSoup(res.text, 'html.parser')

    jobs = []

    rows = soup.select('table tr')

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) < 2:
            continue

        title = cols[0].get_text(strip=True)
        institute = cols[1].get_text(strip=True)

        eligibility = cols[2].get_text(strip=True) if len(cols) > 2 else ''
        area = cols[3].get_text(strip=True) if len(cols) > 3 else ''
        duration = cols[4].get_text(strip=True) if len(cols) > 4 else ''

        jobs.append({
            'title': title,
            'institute': institute,
            'eligibility': eligibility,
            'area': area,
            'deadline': duration,
            'link': url,
            'category': 'Internship',
            'scraped_at': datetime.now().isoformat()
        })

    print(f"Found {len(jobs)} internships from India Science portal")
    return jobs
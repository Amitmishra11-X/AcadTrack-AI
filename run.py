from scrapers.iitd_scraper import scrape_iitd
from scrapers.iitb_scraper import scrape_iitb
from scrapers.iitbhu_scraper import scrape_iitbhu
from database.save_jobs import save_jobs
from classifier.classify import classify_job
from scrapers.indiascience_scraper import scrape_india_science

def run_all():
    print('=== AcadTrack AI — Starting scrape ===')
    print()

    all_jobs = []

    # Step 1: Scrape all institutes
    print('Scraping institutes...')
    all_jobs += scrape_iitd()
    all_jobs += scrape_iitb()
    all_jobs += scrape_iitbhu()
    all_jobs += scrape_india_science()
    # Add more scrapers 
    # all_jobs += scrape_iitb()
    # all_jobs += scrape_nitr()

    # Step 2: Classify each job
    print(f'Classifying {len(all_jobs)} jobs...')
    for job in all_jobs:
        job['category'] = classify_job(job['title'])

    # Step 3: Save to MongoDB
    print('Saving to database...')
    if all_jobs:
        save_jobs(all_jobs)
    else:
        print('  No jobs found this run.')

    print()
    print('=== Done! ===')

if __name__ == '__main__':
    run_all()


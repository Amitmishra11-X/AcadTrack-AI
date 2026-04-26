from turtle import title

from ml.predict import predict_category
from scrapers.iitd_scraper import scrape_iitd
from database.save_jobs import save_jobs
from classifier.classify import classify_job
from scrapers.nitt_scraper import scrape_nitt
from scrapers.indiascience_scraper import scrape_india_science

def run_all():
    print('=== AcadTrack AI — Starting scrape ===')
    print()

    all_jobs = []

    # Step 1: Scrape all institutes
    print('Scraping institutes...')
    all_jobs += scrape_iitd()
    
    all_jobs += scrape_india_science()
    all_jobs += scrape_nitt()
    # Add more scrapers 
    # all_jobs += scrape_iitb()
    # all_jobs += scrape_nitr()

    # Step 2: Classify each job
    from ml.predict import predict_category
    category = predict_category(title)
   

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


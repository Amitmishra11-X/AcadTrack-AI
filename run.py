from ml.predict import predict_category
from scrapers.iitd_scraper import scrape_iitd
from scrapers.nitt_scraper import scrape_nitt
from scrapers.indiascience_scraper import scrape_india_science
from database.save_jobs import save_jobs


def run_all():
    print('=== AcadTrack AI — Starting scrape ===')
    print()

    all_jobs = []

    # 🔹 Step 1: Scrape
    print('Scraping institutes...')
    all_jobs += scrape_iitd()
    all_jobs += scrape_india_science()
    all_jobs += scrape_nitt()

    print(f"Total jobs scraped: {len(all_jobs)}")

    # 🔹 Step 2: Classify each job
    print('Classifying jobs...')

    for job in all_jobs:
        title = str(job.get("title", ""))

        if not title:
            continue

        try:
            category = predict_category(title)
        except Exception as e:
            print(f"Error classifying: {title} → {e}")
            category = "Other"

        job["category"] = category

    # 🔹 Step 3: Save
    print('Saving to database...')
    if all_jobs:
        save_jobs(all_jobs)
    else:
        print('No jobs found this run.')

    print()
    print('=== Done! ===')


if __name__ == '__main__':
    run_all()
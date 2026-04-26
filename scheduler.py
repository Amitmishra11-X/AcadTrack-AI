import schedule
import time
from run import run_all   # your main scraping function

def job():
    print("Running scraper...")
    run_all()
    print("Done")

# ⏰ Run every 6 hours
schedule.every(6).hours.do(job)

# Run once immediately
job()

while True:
    schedule.run_pending()
    time.sleep(60)
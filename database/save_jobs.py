from database.db_connect import get_collection
def save_jobs(jobs):
    collection = get_collection('jobs')
    new_count = 0

    for job in jobs:
        exists = collection.find_one({
            'title': job['title'],
            'institute': job['institute']
        })
        if not exists:
            collection.insert_one(job)
            new_count += 1

    institute = jobs[0]['institute'] if jobs else 'unknown'
    print(f'  Saved {new_count} new jobs from {institute}')

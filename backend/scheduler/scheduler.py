from apscheduler.schedulers.blocking import BlockingScheduler
from test_ai_pipeline import run_pipeline


scheduler = BlockingScheduler()

# run every 6 hours
scheduler.add_job(run_pipeline, "interval", hours=6)

print("Scheduler started. Crawling every 6 hours...")

scheduler.start()
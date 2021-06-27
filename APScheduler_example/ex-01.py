from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def print_time():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

scheduler = BlockingScheduler()
scheduler.add_job(print_time, 'cron', day_of_week='1-5', hour=10, minute=51)
scheduler.start()
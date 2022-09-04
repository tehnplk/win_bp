import time
import schedule
from datetime import datetime

if __name__ == '__main__':
    schedule.every(5).seconds.do(lambda: print(datetime.now().isoformat()))

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

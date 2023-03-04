import time

import schedule

from src.exchange.infrastructure.exchange_controller import perform_queued_purchases
from src.migrations import run_migrations

if __name__ == '__main__':
    run_migrations()
    schedule.every(5).seconds.do(perform_queued_purchases)
    while True:
        schedule.run_pending()
        time.sleep(1)

import logging, time
from datetime import datetime
from time_util import TimeUtil

# Configure logging
logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s",
  handlers=[logging.FileHandler("daily_tasks.log")],
)

tu = TimeUtil(-7)

def daily_task():
  print("Task executed at", tu.utc_to_local(datetime.now()))

# List of local times in HH:MM format when the task should run
run_times = ["15:35", "15:36", "15:37"]

def main():
  try:
    while True:
      for run_time in run_times:
        time_to_sleep = tu.seconds_till_future_time(run_time)
        print("(main-try) Time to sleep: ", time_to_sleep)
        time.sleep(time_to_sleep)
        daily_task()
      
  except KeyboardInterrupt:
    logging.info("User interrupted. Exiting gracefully.")
  except Exception as e:
    logging.error(f"An error occurred: {str(e)}")



if __name__ == "__main__":
  main()

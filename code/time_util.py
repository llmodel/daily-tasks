from datetime import datetime, timedelta, timezone

class TimeUtil:
  def __init__(self, offset_hours: int):
    self.utc_offset = offset_hours
    self.local_offset = timedelta(hours=self.utc_offset)
    self.local_tz = timezone(self.local_offset)

  def local_to_utc(self, local_time):
    # Attach the timezone to the local time
    local_time = local_time.replace(tzinfo=self.local_tz)

    # Convert to UTC
    utc_time = local_time.astimezone(timezone.utc)
    return utc_time

  def utc_to_local(self, utc_time):
    # Convert UTC time to local time
    local_time = utc_time.astimezone(self.local_tz)
    return local_time

  def convert_time_string_to_future_utc(self, time_str):
    # Parse the time string into a datetime object
    local_run_time = datetime.strptime(time_str, "%H:%M")

    # Get the current datetime with timezone information
    current_local_datetime = datetime.now(self.local_tz)
    # Get the current date and combine it with the time
    current_date = current_local_datetime.date()
    local_run_time_with_date = datetime.combine(current_date, local_run_time.time())
    # Attach the local timezone info to local_run_time_with_date
    local_run_time_with_date = local_run_time_with_date.replace(tzinfo=self.local_tz)

    # Check if the local time has already passed the current local time
    # Both sides of this comparison must be consistent with TZ info
    if local_run_time_with_date <= current_local_datetime:
      # Increment the date if the time has already passed
      local_run_time_with_date += timedelta(days=1)

    # Convert to UTC using the local_to_utc function
    utc_run_time = self.local_to_utc(local_run_time_with_date)
    return utc_run_time
  
  def seconds_till_future_time(self, time_str):
    '''Calculate number of seconds from now to time_str'''
    future_utc_time = self.convert_time_string_to_future_utc(time_str)
    current_utc_time = datetime.now(timezone.utc)
    delta = future_utc_time - current_utc_time
    return delta.total_seconds()


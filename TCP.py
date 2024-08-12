def add_time(start, duration, day_of_week=None):
    # Days of the week for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Extract start time and period (AM/PM)
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    
    # Convert start time to 24-hour format for easier calculation
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Extract duration time
    duration_hour, duration_minute = map(int, duration.split(":"))
    
    # Calculate the new time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + (end_minute // 60)
    end_minute = end_minute % 60
    days_later = end_hour // 24
    end_hour = end_hour % 24
    
    # Convert back to 12-hour format
    if end_hour == 0:
        end_hour = 12
        end_period = "AM"
    elif end_hour < 12:
        end_period = "AM"
    elif end_hour == 12:
        end_period = "PM"
    else:
        end_hour -= 12
        end_period = "PM"
    
    # Determine the resulting day of the week, if provided
    if day_of_week:
        day_of_week = day_of_week.capitalize()
        start_day_index = days_of_week.index(day_of_week)
        end_day_index = (start_day_index + days_later) % 7
        resulting_day = days_of_week[end_day_index]
        day_str = f", {resulting_day}"
    else:
        day_str = ""
    
    # Determine the (next day) or (n days later) string
    if days_later == 0:
        later_str = ""
    elif days_later == 1:
        later_str = " (next day)"
    else:
        later_str = f" ({days_later} days later)"
    
    # Format the final time string
    new_time = f"{end_hour}:{end_minute:02d} {end_period}{day_str}{later_str}"
    
    return new_time

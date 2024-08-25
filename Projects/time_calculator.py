def add_time(start, duration, start_day=''):
    """
    Add a duration to a start time, and return the result as a string.

    Args:
        start (str): The start time in 12-hour format, e.g. '3:45 PM'.
        duration (str): The duration to add to the start time, in format 'HH:MM'.
        start_day (str, optional): The day of the week that the start time is on.
            Defaults to None.

    Returns:
        str: The result of adding the duration to the start time, in 12-hour format.
            If start_day is given, the result will also include the day of the week.
    """
    # Days of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Extract start information
    start_parts = start.split()
    start_hours = int(start_parts[0].split(':')[0])
    start_minutes = int(start_parts[0].split(':')[1])
    period = start_parts[1]

    # Extract duration information
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    # Convert start time to 24-hour format
    if period == 'PM' and start_hours != 12:
        start_hours += 12
    if period == 'AM' and start_hours == 12:
        start_hours = 0

    # Calculate end time in 24-hour format
    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes

    # Adjust minutes and hours for overflow
    if end_minutes >= 60:
        end_hours += end_minutes // 60
        end_minutes = end_minutes % 60

    days_passed = end_hours // 24
    end_hours = end_hours % 24

    # Convert end time back to 12-hour format
    if end_hours >= 12:
        period = 'PM'
        if end_hours > 12:
            end_hours -= 12
    else:
        period = 'AM'
        if end_hours == 0:
            end_hours = 12

    # Format minutes to always be two digits
    end_minutes = f'{end_minutes:02}'

    # Construct the new time string
    new_time = f'{end_hours}:{end_minutes} {period}'

    # If start_day is given, calculate the day of the week at the end of addition
    if start_day:
        start_day_index = days.index(start_day.capitalize())
        new_day = days[(start_day_index + days_passed) % 7]
        new_time += f', {new_day}'
    # Add information about the number of days passed
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'
        
    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))

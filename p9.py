'''from datetime import time
def print_time(t):
    # Ensure time is in HH:MM:SS format
    print(t.strftime("%H:%M:%S"))
# Example usage
t = time(14, 30, 45)
print_time(t)


from datetime import timedelta, datetime
def add_seconds_to_time(t, seconds):
    # Convert time object to a datetime object
    dt = datetime.combine(datetime.today(), t)
    
    # Add the specified number of seconds
    dt += timedelta(seconds=seconds)
    
    # Return the updated time
    return dt.time()

# Example usage
t = time(1, 30, 0)
new_time = add_seconds_to_time(t, 7000)
print_time(new_time)'''
   

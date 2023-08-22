def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            # 12 am corresponds to 00:00 in 24-hour format
            hour_24 = 0
        else:
            hour_24 = hour  # No change needed for AM hours
    else:  # period == "pm"
        if hour == 12:
            hour_24 = 12  # 12 pm remains 12 in 24-hour format
        else:
            hour_24 = hour + 12  # Convert PM hours to 24-hour format

    # Format the time in 24-hour format as "HHMM"
    time_24_hour = f"{hour_24:02d}{minute:02d}"
    return time_24_hour

# Test cases
print(convert_to_24_hour(8, 30, "am"))  
print(convert_to_24_hour(8, 30, "pm"))  
print(convert_to_24_hour(12, 15, "am")) 
print(convert_to_24_hour(12, 15, "pm")) 

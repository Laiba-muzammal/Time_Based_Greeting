import time

def get_current_time():
    return time.strftime('%H:%M:%S')

def get_greeting():
    current_hour = int(time.strftime('%H'))
    if current_hour < 12:
        return "Good Morning!"
    elif current_hour < 18:
        return "Good Noon!"
    else:
        return "Good Night!"

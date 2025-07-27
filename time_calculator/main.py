"""
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
"""
# "X:Y"    -> ["X", "Y"] 
# "X:Y AM" -> ["X", "Y", "AM"] 
def take_time(time: str) -> list[str]:
    try:
        time, period = list(time.split(" "))
        return time.split(':') + [period]
    except ValueError:
        return time.split(":")
    
def cycle(start: str, time: int) -> str:
    MAX_INDEX_DAYS = 6
    DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    current_day = DAYS.index(start.lower().capitalize())

    for _ in range(time):
        if current_day < MAX_INDEX_DAYS:
            current_day += 1
        else:
            current_day = 0
    return DAYS[current_day]



days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def add_time(start: str, time:str, day:str = ''):
    h_start, m_start, p_s = take_time(start)
    h_time, m_time = take_time(time)
    past_days = 0

    if not day:
        pass
# "next day" if past_days == 1 else str(past_days) + " days later"

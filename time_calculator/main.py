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

    for _ in range(time % len(DAYS)):
        if current_day < MAX_INDEX_DAYS:
            current_day += 1
        else:
            current_day = 0
    return DAYS[current_day]

def add_time(start: str, time: str, day: str = '') -> str:

    MINUTES_PER_HOUR = 60
    HOURS_PER_PERIOD = 12
    HOURS_PER_DAY    = 24

    def change_period() -> None:
        nonlocal period
        if period == "AM":
            period = "PM"
        else:
            period = "AM"

    h_start, m_start, period = list(map(lambda x: int(x) if x.isdigit() else x, take_time(start)))
    h_time, m_time = list(map(lambda x: int(x), take_time(time)))
    past_days = h_time // HOURS_PER_DAY
    h_time -= past_days * HOURS_PER_DAY
    
    # Soma os minutos, se for > 60 converte um pra hora e reduz 60
    if (m_time + m_start) < MINUTES_PER_HOUR:
        m_time += m_start
    else:
        m_time += m_start - MINUTES_PER_HOUR
        h_time += 1
    
    # Soma as horas, se for >= 12 troca período, se trocar de PM pra AM aumenta um dia
    # Como meia-noite é representado como 12 PM ao invés de 00 PM, se h_time == 0 mudo pra 12
    if (h_time + h_start) < HOURS_PER_PERIOD:
        h_time += h_start

    else:
        h_time += h_start - HOURS_PER_PERIOD
            
        if h_time == 0:
            h_time = HOURS_PER_PERIOD
        if period == "PM":
            past_days += 1
        change_period()
    
    new_time = f'{h_time}:{m_time:02} {period}'
    
    if day:
        current_day = cycle(day, past_days)
        new_time += f', {current_day}'

    if past_days != 0:
        new_time += ' (next day)' if past_days == 1 else f" ({past_days} days later)"

    return new_time
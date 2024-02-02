def estimate_reading_time(reading_speed, words):
    word_count = len(words.split())
    time_in_minutes = word_count / reading_speed

    hours = int(time_in_minutes // 60)
    minutes = int(time_in_minutes % 60)
    
    if minutes < 1:
        return 'You can read that text less than a minute.'
    
    return f'{hours} h {minutes} min'
def addTime(start: str, duration: str, day_of_start: str = None):
    # SIMPLIFY PARAMETER
    simplify_start = start.replace(' ', ':')
    simple_start_distinguish = simplify_start.split(':')
    duration_distinguish = duration.split(':')
    if not day_of_start is None:
        lower_start_day = day_of_start.lower()
    else: pass
    # UNDERSTAND START AND DURATION WITH MINUTE
    start_with_minute = int(simple_start_distinguish[0]) * 60 + int(simple_start_distinguish[1])
    if simple_start_distinguish[2] == 'PM':
        start_with_minute += 12 * 60
    else: pass
    duration_with_minute = int(duration_distinguish[0]) * 60 + int(duration_distinguish[1])
    # DAY AND AM PM BOUNDARY TO CORRECT REVEAL
    day_boundary = 24 * 60
    am_pm_boundary = day_boundary / 2
    # TOTAL TIME CALCULATION
    total_time_with_minute = start_with_minute + duration_with_minute
    # CORRECT DAILY TIME AND AM PM
    daily_time = total_time_with_minute % day_boundary
    if not daily_time // am_pm_boundary < 1:
        correct_minute = daily_time % am_pm_boundary
        correct_hour = int(correct_minute // 60)
        if correct_hour == 0:
            correct_hour = 12
        else: pass
        addition_minute = int(correct_minute % 60)
        if len(str(addition_minute)) < 2:
            addition_minute = '0' + f'{addition_minute}'
        else: pass
        addition_am_pm = "PM"
    else:
        correct_hour = int(daily_time // 60)
        if correct_hour == 0:
            correct_hour = 12
        else: pass
        addition_minute = int(daily_time % 60)
        if len(str(addition_minute)) < 2:
            addition_minute = '0' + f'{addition_minute}'
        else: pass
        addition_am_pm = "AM"
    final_clock = f"{correct_hour}:{addition_minute} {addition_am_pm}"
    # INCLUDE DAY AS WELL
    end_day_count = total_time_with_minute // day_boundary
    if not day_of_start is None:
        day_correspondence = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
        invert_day_correspondence = {value: key for key, value in day_correspondence.items()}
        correspond_to_day = invert_day_correspondence[(day_correspondence[lower_start_day] + end_day_count) % 7]
        final_clock += f", {correspond_to_day.capitalize()}"
    else: pass
    # REVEAL PASS TIME
    if end_day_count == 1:
        paranthesis_indication = " (next day)"
        final_clock += paranthesis_indication
    elif end_day_count > 1:
        paranthesis_indication = (f" ({end_day_count} days later)")
        final_clock += paranthesis_indication
    else: pass
    return final_clock
print(addTime('11:43 PM', '24:20', 'monday'))
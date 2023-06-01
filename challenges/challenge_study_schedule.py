def study_schedule(permanence_period, target_time):
    if not all(
        isinstance(period[0], int) and isinstance(period[1], int)
        for period in permanence_period
    ):
        return None

    if not target_time:
        return None

    count_students = 0

    for period in permanence_period:
        if target_time >= period[0] and target_time <= period[1]:
            count_students += 1

    return count_students

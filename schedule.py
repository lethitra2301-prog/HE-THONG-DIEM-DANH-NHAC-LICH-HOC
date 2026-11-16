def validate_schedule(subject, time):
    if subject and time:
        return True
    return False


def create_schedule(subject, time):
    if validate_schedule(subject, time):
        return {
            "subject": subject,
            "time": time
        }
    return None

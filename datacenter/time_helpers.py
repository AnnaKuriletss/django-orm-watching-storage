from django.utils import timezone
from datacenter.constants import SECONDS_IN_HOUR, SECONDS_IN_MINUTE


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = timezone.now() - visit.entered_at
    return duration


def format_duration(duration):
    hours = duration.seconds // SECONDS_IN_HOUR
    minutes = (duration.seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = duration.seconds % SECONDS_IN_MINUTE
    return f"{hours:02}:{minutes:02}:{seconds:02}"

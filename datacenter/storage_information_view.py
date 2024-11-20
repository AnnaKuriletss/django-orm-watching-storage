from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_helpers import get_duration, format_duration


def storage_information_view(request):
    ongoing_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in ongoing_visits:
        duration = get_duration(visit)
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": format_duration(duration),
            }
        )

    return render(
        request, "storage_information.html", {"non_closed_visits": non_closed_visits}
    )

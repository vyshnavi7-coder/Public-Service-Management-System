from django.shortcuts import render
from .models import Complaint


def complaint_view(request):

    success = False

    if request.method == "POST":

        complaint = Complaint.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            department=request.POST["department"],
            description=request.POST["description"]
        )

        success = complaint.complaint_id

    return render(
        request,
        "services/complaint.html",
        {"success": success}
    )


def track_complaint(request):

    complaint = None

    if request.method == "POST":

        complaint_id = request.POST.get("complaint_id")

        try:
           complaint = Complaint.objects.create(
    user=request.user if request.user.is_authenticated else None,
    name=request.POST["name"],
    email=request.POST["email"],
    department=request.POST["department"],
    description=request.POST["description"]
)
        except Complaint.DoesNotExist:
            complaint = None

    return render(
        request,
        "services/track.html",
        {"complaint": complaint}
    )
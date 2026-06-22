from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from services.models import Complaint


def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("complaint")

    return render(request, "accounts/login.html")


def logout_view(request):

    logout(request)

    return redirect("login")
@login_required
def dashboard_view(request):

    complaints = Complaint.objects.filter(user=request.user)

    total = complaints.count()
    pending = complaints.filter(status='Pending').count()
    resolved = complaints.filter(status='Resolved').count()

    context = {
        'complaints': complaints,
        'total': total,
        'pending': pending,
        'resolved': resolved,
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )
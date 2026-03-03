from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Job
from .serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-applied_date')
    serializer_class = JobSerializer

    def filter_by_status(self, request, status=None):
        jobs = Job.objects.filter(status=status)
        serializer = self.get_serializer(jobs, many=True)
        return Response(serializer.data)


def dashboard(request):
    jobs = Job.objects.all()
    context = {
        "total": jobs.count(),
        "applied": jobs.filter(status="Applied").count(),
        "interview": jobs.filter(status="Interview").count(),
        "offer": jobs.filter(status="Offer").count(),
    }
    return render(request, "dashboard.html", context)


def applications(request):
    jobs = Job.objects.all().order_by("-applied_date")
    return render(request, "applications.html", {"jobs": jobs})


def add_job_page(request):
    if request.method == "POST":
        company = request.POST.get("company")
        role = request.POST.get("role")
        status = request.POST.get("status")
        Job.objects.create(company=company, role=role, status=status)
        return redirect("applications")
    return render(request, "add_job.html")


def analytics(request):
    jobs = Job.objects.all()
    context = {
        "applied": jobs.filter(status="Applied").count(),
        "interview": jobs.filter(status="Interview").count(),
        "rejected": jobs.filter(status="Rejected").count(),
        "offer": jobs.filter(status="Offer").count(),
    }
    return render(request, "analytics.html", context)


def about(request):
    return render(request, "about.html")
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from assessments.models import TestAttempt, IQCategory
from careers.models import CareerBookmark
from django.db.models import Count
from django.utils.timezone import now, timedelta

@staff_member_required
def dashboard(request):
    # 1. Tests per day (last 7 days)
    today = now().date()
    last_week = today - timedelta(days=7)
    tests_per_day = (
        TestAttempt.objects.filter(created_at__date__gte=last_week)
        .values("created_at__date")
        .annotate(count=Count("id"))
        .order_by("created_at__date")
    )

    # 2. Popular careers (based on bookmarks)
    popular_careers = (
        CareerBookmark.objects.values("career__title")
        .annotate(count=Count("id"))
        .order_by("-count")[:5]
    )

    # 3. IQ distribution
    iq_distribution = (
        TestAttempt.objects.values("iq_category")
        .annotate(count=Count("id"))
    )

    return render(request, "admin_reports/dashboard.html", {
        "tests_per_day": list(tests_per_day),
        "popular_careers": list(popular_careers),
        "iq_distribution": list(iq_distribution),
    })

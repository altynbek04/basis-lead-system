from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from .models import Lead
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Q

# 🔹 Dashboard
@login_required
def dashboard(request):
    total_leads = Lead.objects.count()
    hot_leads = Lead.objects.filter(is_hot=True).count()
    avg_budget = Lead.objects.aggregate(Avg("budget"))["budget__avg"] or 0

    last_7_days = timezone.now() - timedelta(days=7)

    leads_last_week = (
        Lead.objects.filter(created_at__gte=last_7_days)
        .extra({"day": "date(created_at)"})
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )

    closed_leads = Lead.objects.filter(status="closed").count()

    conversion = 0
    if total_leads > 0:
        conversion = round((closed_leads / total_leads) * 100, 1)

    context = {
        "total_leads": total_leads,
        "hot_leads": hot_leads,
        "avg_budget": int(avg_budget),
        "chart_data": list(leads_last_week),
        "closed_leads": closed_leads,
        "conversion": conversion,
    }

    return render(request, "dashboard.html", context)


# 🔥 Горячие лиды
@login_required
def hot_leads(request):
    leads = Lead.objects.filter(is_hot=True).order_by("-created_at")
    return render(request, "hot_leads.html", {"leads": leads})
def update_status(request, lead_id, new_status):
    lead = Lead.objects.get(id=lead_id)
    lead.status = new_status
    lead.save()
    return redirect("all_leads")

# 📋 Все лиды с фильтрацией
@login_required
def all_leads(request):
    status = request.GET.get("status")
    search_query = request.GET.get("search")

    leads = Lead.objects.all().order_by("-created_at")

    if status:
        leads = leads.filter(status=status)

    if search_query:
        leads = leads.filter(
            Q(name__icontains=search_query) |
            Q(phone__icontains=search_query)
        )

    paginator = Paginator(leads, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "all_leads.html", {
        "page_obj": page_obj,
        "search_query": search_query,
    })
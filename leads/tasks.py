from celery import shared_task
from .models import Lead

@shared_task
def process_hot_lead(lead_id):
    lead = Lead.objects.get(id=lead_id)
    print(f"🔥 Обработка горячего лида: {lead.name}")
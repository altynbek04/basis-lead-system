from django.db import models

class Lead(models.Model):

    SERVICE_CHOICES = (
        ("training", "Обучение"),
        ("constructor", "Конструктор"),
        ("furniture", "Мебель"),
    )

    STATUS_CHOICES = (
        ("new", "Новый"),
        ("in_progress", "В работе"),
        ("closed", "Закрыт"),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    budget = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    score = models.IntegerField(default=0)
    is_hot = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
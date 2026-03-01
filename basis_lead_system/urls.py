from django.contrib import admin
from django.urls import path
from leads.views import dashboard
from leads.views import dashboard, hot_leads, all_leads
from django.contrib.auth import views as auth_views
from leads.views import dashboard, hot_leads, all_leads, update_status
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', dashboard, name="dashboard"),
    path('hot/', hot_leads, name="hot_leads"),
    path('leads/', all_leads, name="all_leads"),

    path('lead/<int:lead_id>/<str:new_status>/', update_status, name='update_status'),
]
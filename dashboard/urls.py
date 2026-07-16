from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_overview, name='dashboard'),
    path('users/', views.seekers_view, name='seekers'),
    path('users/<int:pk>/', views.seeker_detail, name='seeker_detail'),
    path('walis/', views.walis_view, name='walis'),
    path('imams/', views.imams_view, name='imams'),
    path('matches/', views.matches_view, name='matches'),
    path('chats/', views.chat_oversight_view, name='chats'),
    path('moderation/', views.reports_view, name='reports'),
    path('verifications/', views.verifications_view, name='verifications'),
    path('revenue/', views.revenue_view, name='revenue'),
    path('regions/', views.regions_view, name='regions'),
    path('settings/', views.settings_view, name='settings'),
    
    # API endpoints
    path('api/login/', views.api_login, name='api_login'),
    path('api/seekers/', views.api_seekers, name='api_seekers'),
    path('api/verify/', views.api_submit_verification, name='api_submit_verification'),
    path('api/premium-upgrade/', views.api_premium_upgrade, name='api_premium_upgrade'),
    path('api/matches/<int:match_id>/audit-modal/', views.chat_audit_modal_partial, name='chat_audit_modal_partial'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('input/', views.input_view, name='input'),
    path('chart/', views.chart_view, name='chart'),
    path('download_excel/', views.export_to_excel_view, name='download_excel'),  # URL mapping for downloading Excel
    path('calendar/', views.calendar_view, name='calendar'),
    path('delete-quote/<int:id>/', views.delete_quote, name='delete_quote'),


]

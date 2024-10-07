from django.urls import path
from .views import input_view, chart_view

urlpatterns = [
    path('', input_view, name='input_view'),
    path('chart/', chart_view, name='chart_view'),
]

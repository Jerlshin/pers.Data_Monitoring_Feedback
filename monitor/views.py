from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import UserInput
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime

def input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_input = form.save(commit=False)
            user_input.date = timezone.now()  # Set the current date
            user_input.save()
            return redirect('chart_view')  # Redirect to the chart view after saving
    else:
        form = UserInputForm()
    
    return render(request, 'monitor/input.html', {'form': form})

def chart_view(request):
    # Retrieve all UserInput records
    inputs = UserInput.objects.all().order_by('date')  # Order by date for time series
    
    # Prepare cumulative data for the line chart
    date_labels = []
    cumulative_data = []
    current_score = 0  # Start with a score of 0

    # Prepare data for the bar chart
    total_read_bible = []
    total_prayed = []
    total_exercised = []
    total_satisfied = []
    total_hurt_someone = []

    for input in inputs:
        date_labels.append(input.date.strftime('%Y-%m-%d'))  # Use the date field for x-axis labels

        # Calculate cumulative score based on user inputs
        if input.read_bible:
            current_score += 1
        if input.prayed:
            current_score += 1
        if input.exercised:
            current_score += 1
        if input.satisfied:
            current_score += 1
        if input.hurt_someone:
            current_score -= 1  # Decrease the score if the user hurt someone

        cumulative_data.append(current_score)  # Append the current score to the data list
        
        # Count individual inputs for bar chart
        total_read_bible.append(1 if input.read_bible else 0)
        total_prayed.append(1 if input.prayed else 0)
        total_exercised.append(1 if input.exercised else 0)
        total_satisfied.append(1 if input.satisfied else 0)
        total_hurt_someone.append(1 if input.hurt_someone else 0)

    line_chart_data = {
        'labels': date_labels,
        'cumulative_score': cumulative_data,
    }

    # Prepare bar chart data by summing individual inputs over the entire period
    bar_chart_data = {
        'labels': ['Read Bible', 'Prayed', 'Exercised', 'Satisfied', 'Hurt Someone'],
        'values': [
            sum(total_read_bible),
            sum(total_prayed),
            sum(total_exercised),
            sum(total_satisfied),
            -sum(total_hurt_someone)  # Show hurt as a negative value
        ],
    }

    return render(request, 'monitor/chart.html', {
        'line_chart_data': line_chart_data,
        'bar_chart_data': bar_chart_data,
    })

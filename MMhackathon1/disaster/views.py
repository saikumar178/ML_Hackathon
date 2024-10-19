from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Disaster, Volunteer
from .forms import DisasterForm, VolunteerForm

# Home view displaying volunteer counts
def home(request):
    volunteer_count = Volunteer.objects.count()
    user_volunteer_count = request.session.get('volunteer_counter', 0)  # Get user-specific count
    return render(request, 'disaster/index.html', {
        'volunteer_count': volunteer_count,
        'user_volunteer_count': user_volunteer_count
    })

# Geolocation view (static)
def geolocation(request):
    return render(request, 'disaster/geolocation.html')

# List of disasters
def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster/disaster_list.html', {'disasters': disasters})

# Report a disaster
def report_disaster(request):
    if request.method == 'POST':
        form = DisasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disaster_list')
    else:
        form = DisasterForm()
    return render(request, 'disaster/report_disaster.html', {'form': form})

# Volunteer registration view
def register_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()  # Save volunteer to the database
            return redirect('thanks')  # Redirect to the homepage after successful registration
    else:
        form = VolunteerForm()
    return render(request, 'disaster/register_volunteer.html', {'form': form})


# Example home view
def home_view(request):
    return render(request, 'disaster/home.html')  # Ensure you have home.html
def thanks_view(request):
    return render(request, 'disaster/thanks.html')  # Ensure the path is correct
def index_view(request):
    return render(request, 'disaster/index.html')  # Make sure this path is correct
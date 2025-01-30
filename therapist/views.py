from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth import get_user_model
from django.shortcuts import render

def home(request):
    return render(request, 'therapist/home.html')

def about(request):
    return render(request, 'therapist/about.html')

def services(request):
    return render(request, 'therapist/services.html')

@staff_member_required
def admin_dashboard(request):
    # Replace 'admin_dashboard.html' with your actual template name
    return render(request, 'adminpanel/admin_dashboard.html')

@login_required
def dashboard(request):
    # Fetch the latest 5 diary entries for the logged-in user
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'dashboard.html', {'entries': entries})

@login_required
def diary(request):
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'therapist/diary.html', {'entries': entries})


@login_required
def add_diary_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        DiaryEntry.objects.create(user=request.user, title=title, content=content)
        return redirect('diary')  # Redirect to the diary page
    return redirect('diary')  # Fallback redirect

User = get_user_model()

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
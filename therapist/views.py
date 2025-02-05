from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry,  Client, Assessment
from .forms import DiaryEntryForm, AssessmentForm
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

def Experiences(request):
    return render(request, 'therapist/Experiences.html')


def Blog(request):
    return render(request, 'therapist/Blog.html')



def assessment_list(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    assessments = Assessment.objects.filter(client=client)
    return render(request, 'assessment_list.html', {'client': client, 'assessments': assessments})


def add_assessment(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.client = client
            assessment.save()
            return redirect('assessment_list', client_id=client.id)
    else:
        form = AssessmentForm()
    return render(request, 'add_assessment.html', {'form': form, 'client': client})


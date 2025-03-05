from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Client, Intake
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.forms.models import model_to_dict




def custom_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username") or form.cleaned_data.get("email")  # Handle username/email
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)  # Authenticate User

            if user is not None:
                login(request, user)  # Log in user
                request.session.set_expiry(86400)  # Keep session for 1 day
                return redirect("dashboard")  # Redirect to Dashboard
            else:
                form.add_error(None, "Invalid username or password.")  # Show error message

    else:
        form = AuthenticationForm()

    return render(request, "account/login.html", {"form": form})





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



CustomUser = get_user_model()

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})



def Experiences(request):
    return render(request, 'therapist/Experiences.html')


def Blog(request):
    return render(request, 'therapist/Blog.html')





from .forms import RegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_backends
from .models import CustomUser  # Ensure this is imported


def Registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)

            # ✅ Explicitly get the authentication backend
            backend = get_backends()[0]  # Use the first backend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"

            login(request, user, backend=user.backend)  # ✅ Set backend explicitly

            return redirect('dashboard')  # Change this to your actual redirect
    else:
        form = RegistrationForm()

    return render(request, 'therapist/Registration.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PreliminaryIntakeForm
from .models import Client, Intake
@login_required
def intake_form(request):
    """Handles the intake form submission and updates existing data if available."""
    user = request.user

    # ✅ Ensure the client exists
    client, created = Client.objects.get_or_create(
        email=user.email,
        defaults={"name": request.user.get_full_name() or "Unknown"}
    )

    # ✅ Retrieve the existing intake form for this client if it exists
    intake = Intake.objects.filter(client=client).first()

    if request.method == "POST":
        form = PreliminaryIntakeForm(request.POST, instance=intake)  # ✅ Bind form to existing intake instance
        if form.is_valid():
            intake = form.save(commit=False)
            intake.client = client  # Attach client to the intake form
            intake.date = timezone.now().date()  # ✅ Always set date to today
            intake.save()
            messages.success(request, "טופס האינטייק שלך נשמר בהצלחה!")  # ✅ Confirmation message
            return redirect("intake_summary")  # Redirect to the intake summary page

    else:
        # ✅ Pre-fill form with the latest intake data except for `date`
        initial_data = {"date": timezone.now().date()}  # Default today's date
        if intake:
            initial_data.update(model_to_dict(intake, exclude=["date"]))  # Copy all fields except `date`

        form = PreliminaryIntakeForm(initial=initial_data, instance=intake)

    return render(request, "therapist/preliminary_intake.html", {"form": form})



@login_required
def intake_summary(request):
    """Retrieve and display the intake form for the logged-in user."""
    user = request.user

    client = Client.objects.filter(email=user.email).first()
    if not client:
        messages.error(request, "No client record found. Please complete the intake form first.")
        return redirect("/intake/")  # ✅ Redirect to intake form

    intake = Intake.objects.filter(client=client).first()
    if not intake:
        messages.error(request, "No intake form found. Please complete the intake form first.")
        return redirect("/intake/")  # ✅ Redirect to intake form

    # ✅ Use the correct variable name (`intake`)
    form = PreliminaryIntakeForm(instance=intake)

    return render(request, "therapist/intake_summary.html", {
        "form": form,
        "boolean_fields": ["smoking", "substance_use"],
    })




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry

@login_required
def dashboard_view(request):
    """Main dashboard page that includes the diary."""
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, "therapist/dashboard.html", {"entries": entries})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm, DeleteEntryForm

@login_required
def diary_view(request):
    """Handles adding and deleting diary entries, then reloads the dashboard with diary open."""
    if request.method == "POST":
        if "delete_entry" in request.POST:
            entry_id = request.POST.get("delete_entry")
            entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
            entry.delete()
        else:
            entry_form = DiaryEntryForm(request.POST)
            if entry_form.is_valid():
                new_entry = entry_form.save(commit=False)
                new_entry.user = request.user
                new_entry.save()

        # Redirect to the dashboard and trigger toggleDiary() via hash fragment
        return redirect("/dashboard/#open-diary")

    # Default behavior: return the diary content
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, "therapist/diary.html", {
        "entries": entries,
        "entry_form": DiaryEntryForm(),
        "delete_form": DeleteEntryForm()
    })


###########################################################################################################################################
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TherapyGoal, PositiveAffirmation
from .forms import TherapyGoalForm, PositiveAffirmationForm
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def therapist_dashboard(request):
    clients = User.objects.filter(is_staff=False)  # Assuming therapists are staff users
    return render(request, "therapist/dashboard.html", {"clients": clients})

@login_required
def client_dashboard(request, client_id):
    client = get_object_or_404(User, id=client_id, is_staff=False)
    goals = TherapyGoal.objects.filter(client=client)
    affirmations = PositiveAffirmation.objects.filter(client=client)
    return render(request, "therapist/client_dashboard.html", {
        "client": client, 
        "goals": goals, 
        "affirmations": affirmations
    })

@login_required
def add_therapy_goal(request, client_id):
    client = get_object_or_404(User, id=client_id, is_staff=False)
    if request.method == "POST":
        form = TherapyGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.therapist = request.user
            goal.client = client
            goal.save()
            return redirect("client_dashboard", client_id=client.id)
    else:
        form = TherapyGoalForm()
    return render(request, "therapist/add_goal.html", {"form": form, "client": client})

@login_required
def add_positive_affirmation(request, client_id):
    client = get_object_or_404(User, id=client_id, is_staff=False)
    if request.method == "POST":
        form = PositiveAffirmationForm(request.POST)
        if form.is_valid():
            affirmation = form.save(commit=False)
            affirmation.therapist = request.user
            affirmation.client = client
            affirmation.save()
            return redirect("client_dashboard", client_id=client.id)
    else:
        form = PositiveAffirmationForm()
    return render(request, "therapist/add_affirmation.html", {"form": form, "client": client})


###########################################################################################################################################




@login_required
def dashboard(request):
    # Fetch the latest 5 diary entries for the logged-in user
    entries = DiaryEntry.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'dashboard.html', {'entries': entries})

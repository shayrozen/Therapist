from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone



# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = "email"  # Set email as the primary identifier
    REQUIRED_FIELDS = []  # No need for a username

    objects = CustomUserManager()

    def __str__(self):
        return self.email


from django.db import models
from django.conf import settings
from django.utils.timezone import now

class DiaryEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=now)

    def __str__(self):
        return self.title




####################################################################################################################

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TherapyGoal(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapy_goals")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_goals")
    goal_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Goal for {self.client.username}: {self.goal_text[:50]}"

class PositiveAffirmation(models.Model):
    therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="positive_affirmations")
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_affirmations")
    affirmation_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Affirmation for {self.client.username}: {self.affirmation_text[:50]}"



####################################################################################################################


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Intake(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  
    date = models.DateField(default=timezone.now)  # Set default to today
    phone = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    country_of_birth = models.CharField(max_length=255, null=True)
    marital_status = models.CharField(max_length=255, null=True)
    current_occupation = models.TextField(blank=True, null=True)
    physical_activity = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    nutrition_habits = models.TextField(blank=True, null=True)
    smoking = models.BooleanField(default=False)
    substance_use = models.BooleanField(default=False)
    addictions = models.TextField(blank=True, null=True)
    past_treatments = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    emotional_physical_issues = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    life_turning_points = models.TextField(blank=True, null=True)
    body_pain = models.TextField(blank=True, null=True)
    family_background = models.TextField(blank=True, null=True)
    religious_beliefs = models.TextField(blank=True, null=True)
    repeating_patterns = models.TextField(blank=True, null=True)
    strengths_and_resources = models.TextField(blank=True, null=True)
    reason_for_therapy = models.TextField(blank=True, null=True)
    therapy_goals = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Intake Form for {self.client.name}"

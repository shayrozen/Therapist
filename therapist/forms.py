from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class ClientSignupForm(SignupForm):
    email = forms.EmailField(required=True)

    def save(self, request):
        user = super(ClientSignupForm, self).save(request)
        user.is_client = True  # Assign client role
        user.save()
        return user



class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(
        label="שם מלא", max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    email = forms.EmailField(
        label="כתובת דוא\"ל", widget=forms.EmailInput(attrs={'class': 'form-input'})
    )
    password1 = forms.CharField(
        label="סיסמה", widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )
    password2 = forms.CharField(
        label="אימות סיסמה", widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )

    class Meta:
        model = CustomUser  # ✅ Ensure it uses CustomUser
        fields = ['full_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("האימייל הזה כבר רשום במערכת.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("הסיסמאות לא תואמות. אנא נסה שוב.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Hash the password
        user.is_client = True  # Assign client role
        if commit:
            user.save()
        return user


from .models import DiaryEntry
class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['content']
        
        
from django import forms
from .models import Intake
from django.utils.timezone import now  # Import current date

class PreliminaryIntakeForm(forms.ModelForm):
    """ טופס ראיון ראשוני עם מטופל - מבוסס על המסמך המצורף """
    CLIENT_STATUS_CHOICES = [
        ("existing", "אני כבר מטופל קיים"),
        ("new", "אני מטופל חדש"),
    ]

    client_status = forms.ChoiceField(
        choices=CLIENT_STATUS_CHOICES,
        widget=forms.RadioSelect,
        label="האם אתה מטופל קיים או חדש?"
    )
    
    date = forms.DateField(label="תאריך:", widget=forms.DateInput(attrs={'type': 'date'}),initial=now().date())  # Set today's date by default
    full_name = forms.CharField(label="שם המטופל/ת:", max_length=255)
    phone = forms.CharField(label="טלפונים:", max_length=15)
    email = forms.EmailField(label="אימייל:")
    address = forms.CharField(label="כתובת:", max_length=255, required=False)
    age = forms.IntegerField(label="גיל:")
    country_of_birth = forms.CharField(label="ארץ לידה:", max_length=255)
    marital_status = forms.CharField(label="מצב משפחתי:", max_length=255)
    
    current_occupation = forms.CharField(
        label="עיסוק בהווה ועיסוקים בעבר:", 
        widget=forms.Textarea(attrs={'rows': 2}), 
        required=False
    )

    physical_activity = forms.CharField(
        label="האם יש לך שגרה של פעילות גופנית? פרט:",
        widget=forms.Textarea(attrs={'rows': 2}), 
        required=False
    )

    hobbies = forms.CharField(
        label="תחביבים:",
        widget=forms.Textarea(attrs={'rows': 2}), 
        required=False
    )

    nutrition_habits = forms.CharField(
        label="הרגלי תזונה ושתייה (כולל קפה ואלכוהול):",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )

    smoking = forms.BooleanField(label="האם את מעשנת?", required=False)
    substance_use = forms.BooleanField(label="האם את צורכת חומרים אחרים?", required=False)
    addictions = forms.CharField(
        label="התמכרויות:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )

    past_treatments = forms.CharField(
        label="האם את מטופלת כעת או טופלת בעבר בטיפול אלטרנטיבי מכל סוג שהוא? או בטיפול פסיכולוגי או רפואי קבוע:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )
    
    medications = forms.CharField(
        label="האם את צורכת תרופות? ואם כן אילו ומה מטרתן? האם את סובלת מתופעות לוואי:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )

    emotional_physical_issues = forms.CharField(
        label="האם ישנן בעיות פיזיות מהן את סובלת או בעיות רגשיות כגון פחדים, דאגות? האם ניסית לפתור אותן בעבר ואם כן מה היו התוצאות:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    additional_notes = forms.CharField(
        label="צייני כל מצב או בעיה נוספת עליהם צריכה המטפלת לדעת:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    
    life_turning_points = forms.CharField(
        label="האם ישנן נקודות מפנה משמעותיות בחייך:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    
    body_pain = forms.CharField(
        label="האם ישנם כאבים בגוף:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )

    family_background = forms.CharField(
        label="רקע משפחתי - הורים, אחים, יחסים לדמויות קרובות אחרות שאולי גידלו כמו סבים, סבתות, היחסים בין ההורים, קשרים במשפחה:",
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )

    religious_beliefs = forms.CharField(
        label="אמונות דתיות ורוחניות:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )
    
    repeating_patterns = forms.CharField(
        label="האם קיימים תכנים מסוימים המתמחזרים בחייך:",
        widget=forms.Textarea(attrs={'rows': 2}),
        required=False
    )
    
    strengths_and_resources = forms.CharField(
        label="נקודות חוזקה ומשאבים - פנימיים, חיצוניים:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    
    reason_for_therapy = forms.CharField(
        label="מהי הסיבה שבגללה הגעת לטיפול הנוכחי? במה היית רוצה שהטיפול יעזור לך:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True
    )
    
    therapy_goals = forms.CharField(
        label="מה מטרת הטיפול:",
        widget=forms.Textarea(attrs={'rows': 3}),
        required=True
    )
    
    class Meta:
        model = Intake
        fields = "__all__"  # ✅ Automatically include all fields from the Intake model, no need to manually list them
        exclude = ["client", "created_at"]  # ✅ Client is set in views.py, and created_at should be auto-generated

    
    def clean(self):
        """ Validate required fields for new clients """
        cleaned_data = super().clean()
        client_status = cleaned_data.get("client_status")
        full_name = cleaned_data.get("full_name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")

        if client_status == "new":  # If new client, full details are required
            if not full_name:
                self.add_error("full_name", "יש להזין שם מלא אם אתה מטופל חדש.")
            if not email:
                self.add_error("email", "יש להזין כתובת אימייל אם אתה מטופל חדש.")
            if not phone:
                self.add_error("phone", "יש להזין מספר טלפון אם אתה מטופל חדש.")

        return cleaned_data





from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "כותרת הרשומה", "class": "diary-input"}),
            "content": forms.Textarea(attrs={"placeholder": "כתבי כאן את התחושות והמחשבות שלך...", "class": "diary-textarea", "rows": 4}),
        }

class DeleteEntryForm(forms.Form):
    entry_id = forms.IntegerField(widget=forms.HiddenInput())




from django import forms
from .models import TherapyGoal, PositiveAffirmation

class TherapyGoalForm(forms.ModelForm):
    class Meta:
        model = TherapyGoal
        fields = ["goal_text"]
        widgets = {
            "goal_text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class PositiveAffirmationForm(forms.ModelForm):
    class Meta:
        model = PositiveAffirmation
        fields = ["affirmation_text"]
        widgets = {
            "affirmation_text": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

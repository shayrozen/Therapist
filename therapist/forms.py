from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, Assessment

class ClientSignupForm(SignupForm):
    def save(self, request):
        user = super(ClientSignupForm, self).save(request)
        user.is_client = True
        user.save()
        return user

from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['content']
        
        


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['assessment_type', 'score', 'notes']


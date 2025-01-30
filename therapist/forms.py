from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser

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
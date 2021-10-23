from django import forms

from .models import Login


class LoginCreation(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['name', 'address','spec', 'experience','phone_no','email','desc','thumbnail']

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
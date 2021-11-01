from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'mobile', 'program']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.TextInput(attrs={'class': 'form-control'}),

        }


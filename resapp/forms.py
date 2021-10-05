from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *


class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = ('first_name', 'last_name', 'gender', 'age',
                  'address', 'email', 'github', 'linkedin')

        widgets = {
            'first_name': forms.TextInput(attrs={'title': 'First Name'}),
            'last_name': forms.TextInput(attrs={'title': 'Last Name'}),
            'gender': forms.RadioSelect(attrs={'title': 'Gender'}),
            'age': forms.DateInput(attrs={'title': 'Age'}),
            'address': forms.TextInput(attrs={'title': 'Address'}),
            'email': forms.EmailInput(attrs={'title': 'Email'}),
            'github': forms.URLInput(attrs={'title': 'Github Link'}),
            'linkedin': forms.URLInput(attrs={'title': 'LinkedIn Link'})
        }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('degree', 'stream', 'passing_year', 'result')

        widgets = {
            'degree': forms.Select(attrs={'title': 'Select Degree'}),
            'stream': forms.TextInput(attrs={'title': 'Stream'}),
            'passing_year': forms.DateInput(attrs={'title': 'Passing Year'}),
            'result': forms.TextInput(attrs={'title': 'Result'})
        }


class ProjectOrJobForm(forms.ModelForm):
    class Meta:
        model = ProjectOrJob
        fields = ('work', 'title', 'start_date', 'end_date', 'description')

        widgets = {
            'work': forms.RadioSelect(attrs={'title': 'Work'}),
            'title': forms.TextInput(attrs={'title': 'Title'}),
            'start_date': forms.DateInput(attrs={'title': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'title': 'End Date'}),
            'description': forms.Textarea(attrs={'title': 'Description'})
        }


class ProfessionalSkillsForm(forms.ModelForm):
    class Meta:
        model = ProfessionalSkills
        fields = ('skill_details',)

        widgets = {
            'skill_details': forms.Textarea(attrs={'title': 'Professional Skills'})
        }


class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = ('academic_details',)

        widgets = {
            'academic_details': forms.Textarea(attrs={'title': 'Academic Details'})
        }


class AreaOfInterestForm(forms.ModelForm):
    class Meta:
        model = AreaOfInterest
        fields = ('area_of_interest',)

        widgets = {
            'area_of_interest': forms.Textarea(attrs={'title': 'Area Of Interest'})
        }

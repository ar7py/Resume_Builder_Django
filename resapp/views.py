from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from django.contrib.sites.requests import RequestSite
from django.views.generic import CreateView

from .models import Person, Education, ProjectOrJob, ProfessionalSkills, Academic, AreaOfInterest
from .forms import PersonForm, EducationForm, ProjectOrJobForm, ProfessionalSkillsForm, AcademicForm, AreaOfInterestForm


# Create your views here.

""" class CreateResumeView(CreateView):
    redirect_field_name = 'resapp/resume_view.html'
    form_class = (PersonForm, EducationForm, ProjectOrJobForm,
                  ProfessionalSkillsForm, AcademicForm, AreaOfInterestForm)
    model = (Person, Education, ProjectOrJob,
             ProfessionalSkills, Academic, AreaOfInterest) """


def resumeForm(request):
    if request.method == 'POST':
        personform = PersonForm()
        educationform = EducationForm()
        projectorjobform = ProjectOrJobForm()
        professinalskillsform = ProfessionalSkillsForm()
        academicform = AcademicForm()
        areaofinterestform = AreaOfInterestForm()

        if personform.is_valid():
            personform.save()

        if educationform.is_valid():
            educationform.save()

        if projectorjobform.is_valid():
            projectorjobform.save()

        if professinalskillsform.is_valid():
            professinalskillsform.save()

        if academicform.is_valid():
            academicform.save()

        if areaofinterestform.is_valid():
            areaofinterestform.save()

    return render(request, 'resapp/resume_form.html', {
        'personform': PersonForm(),
        'educationform': EducationForm(),
        'projectorjobform': ProjectOrJobForm(),
        'professionalskillsform': ProfessionalSkillsForm(),
        'academicform': AcademicForm(),
        'areaofinterestform': AreaOfInterestForm(),
    })


def resumeView(request):
    site_name = RequestSite(request).domain
    person = Person.objects.all()[:1]
    education = Education.objects.all()
    projectorjob = ProjectOrJob.objects.all()[:5]
    professionalskills = ProfessionalSkills.objects.all()[:5]
    academic = Academic.objects.all()[:5]
    areaofinterest = AreaOfInterest.objects.all()

    return render('resapp/resume_views.html', {
        'site_name': site_name,
        'person': person,
        'education': education,
        'projectorjob': projectorjob,
        'professionalskills': professionalskills,
        'academic': academic,
        'areaofinterest': areaofinterest,
    })

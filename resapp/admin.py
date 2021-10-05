from django.contrib import admin
from .models import Person, Education, ProjectOrJob, ProfessionalSkills, Academic, AreaOfInterest

# Register your models here.

admin.site.register(Person)
admin.site.register(Education)
admin.site.register(ProjectOrJob)
admin.site.register(ProfessionalSkills)
admin.site.register(Academic)
admin.site.register(AreaOfInterest)

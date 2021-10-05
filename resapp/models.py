from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=270)
    last_name = models.CharField(max_length=270)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    address = models.CharField(max_length=355)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def full_name(self):
        return ([self.first_name + " " + self.last_name])


class Education(models.Model):
    DEGREE_CHOICES = (
        ('Phd', 'Male'),
        ('Mtech/MA/MSc/MCom/MBA', 'Masters'),
        ('Btech/BA/BSc/BCom/BBA', 'Bachelors'),
        ('12th/Diploma', 'School/College'),
        ('10th', 'School')
    )

    person = models.ForeignKey(Person, on_delete=CASCADE)
    degree = models.CharField(max_length=200, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=200)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)

    def __str__(self):
        return self.degree


class ProjectOrJob(models.Model):
    EXPERIENCES_CHOICES = (
        ('J', 'Job'),
        ('P', 'Project')
    )

    person = models.ForeignKey(Person, on_delete=CASCADE)
    work = models.CharField(max_length=1, choices=EXPERIENCES_CHOICES)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.work


class ProfessionalSkills(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    skill_details = models.TextField()

    # def __str__(self):
    # return self.skill_details


class Academic(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    academic_details = models.TextField()


class AreaOfInterest(models.Model):
    person = models.ForeignKey(Person, on_delete=CASCADE)
    area_of_interest = models.TextField()

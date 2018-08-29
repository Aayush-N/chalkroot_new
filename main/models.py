from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserType(models.Model):
    """
        UserType: Used to store the type of user Ex: Student, Principal, Professor etc.
    """

    name = models.CharField("Type of User", max_length=50)

    def __str__(self):
        return self.name

class School(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	address = models.TextField()
	description = models.TextField()
	facilities = models.ForeignKey('Facilities')
	contact_number = models.CharField(max_length=20)
	website = models.CharField(max_length=30, blank=True, null=True)
	photos = models.TextField()
	admission_info = models.TextField()
	overall_rating = models.FloatField(blank=True)
	academic_record = models.TextField()

	def __str__(self):
		return self.name


class User(AbstractUser):
	user_type = models.ForeignKey("UserType")
	school_admin = models.ForeignKey('School', blank=True, null=True)
	employment_details = models.TextField(blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	photo = models.TextField(blank=True, null=True)
	child_school = models.ForeignKey('School', blank=True, null=True)
	facility_preferred = models.ManyToManyField('Facilities')


class Facilities(models.Model):
    """
    Description: Model Description
    """
    name = models.TextField(blank=True, null=True)
    facility_type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
	school = models.ForeignKey('School', blank=True, null=True)
	parent = models.ForeignKey('User', blank=True, null=True)
	review_content = models.TextField(blank=True, null=True)
	rating = models.CharField(max_length=10)

	def __str__(self):
		return parent.name


	
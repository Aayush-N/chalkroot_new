from django.db import models
from django.contrib.auth.models import AbstractUser

import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.

class UserType(models.Model):
	"""
		UserType: Used to store the type of user Ex: Student, Principal, Professor etc.
	"""
	name = models.CharField("Type of User", max_length=50)

	def __str__(self):
		return self.name

class School(models.Model):
	"""
	School: Strores all details about the school
	"""
	sid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30, blank=True, null=True)
	address_line1 = models.CharField(max_length=30, blank=True, null=True)
	address_line2 = models.CharField(max_length=30, blank=True, null=True)
	area = models.CharField(max_length=30, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=30, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	facilities = models.ForeignKey('Facilities',blank=True, null=True)
	contact_number = models.CharField(max_length=20,blank=True, null=True)
	website = models.CharField(max_length=30, blank=True, null=True)
	photos = CloudinaryField('image')
	admission_info = models.TextField(blank=True, null=True)
	overall_rating = models.FloatField(blank=True, null=True)
	board = models.ForeignKey('Board', blank=True, null=True)
	added_by = models.ForeignKey("User", blank=True, null=True, related_name='school_creator')
	def __str__(self):
		return self.name


class User(AbstractUser):
	user_type = models.ForeignKey("UserType", blank=True, null=True)
	school_admin = models.ForeignKey('School', blank=True, null=True, related_name='school_admin')
	employment_details = models.TextField(blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	photo = models.TextField(blank=True, null=True)
	child_school = models.ForeignKey('School', blank=True, null=True, related_name='child_school')
	facility_preferred = models.ManyToManyField('Facilities')


class Facilities(models.Model):
	"""
	Facilities: Stores individual facility provided info
	"""
	name = models.TextField(blank=True, null=True)
	facility_type = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


class Board(models.Model):
	"""
	Facilities: Stores individual facility provided info
	"""
	name = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.name


class Reviews(models.Model):
	"""
	Reviews: Stores reviews for each school
	"""
	school = models.ForeignKey('School', blank=True, null=True)
	parent = models.ForeignKey('User', blank=True, null=True)
	review_content = models.TextField(blank=True, null=True)
	rating = models.CharField(max_length=10)

	def __str__(self):
		return parent.name


	
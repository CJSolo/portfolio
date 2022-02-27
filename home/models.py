from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
	name = models.CharField(max_length = 40, help_text = 'Customer name')
	phone = models.IntegerField(help_text = 'Phone Number')
	address = models.CharField(max_length = 40, help_text = 'Mailing Address')
	city = models.CharField(max_length = 20, help_text = 'City')
	state = models.CharField(max_length = 2, help_text = 'State')
	zip_code = models.IntegerField(help_text = 'Zip Code')
	email_add = models.EmailField(max_length = 25, help_text = 'Email Address')

# Metadata
	class Meta:
		ordering = ['name']

# Methods
	def get_absolute_url(self):
		return reverse('customer-detail', args=[str(self.id)])

	def __str__(self):
		return self.name


class customer_notes(models.Model):
	note_owner = models.ForeignKey('customer', on_delete = models.SET_NULL, null = True, related_name='mynote')
	made_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name='madenote')
	date_made = models.DateTimeField(auto_now_add=True)
	note_subject = models.CharField(max_length = 40, help_text = 'Note Subject', blank=True)
	customer_note = models.TextField(help_text = 'Enter Note Comments')

	class Meta:
		ordering = ['date_made']

	def __str__(self):
		return self.note_subject

	def get_absolute_url(self):
		return reverse('note-detail', args=[str(self.id)])


class dog(models.Model):
	dog_name = models.CharField(max_length = 20, help_text = 'Dog Name')
	dog_owner = models.ForeignKey('customer', on_delete = models.SET_NULL, null = True, related_name='mydog')
	dog_breed = models.ForeignKey('dog_breeds', on_delete = models.SET_NULL, null = True, related_name='mybreed')
	dog_color = models.CharField(max_length = 10, help_text = 'Dog Fur Color')
	dog_age = models.IntegerField(help_text = 'Dog Age')
	dog_weight = models.IntegerField(help_text = 'Dog Weight')
	dog_photo = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = 100, blank=True)

	class Meta:
		ordering = ['dog_name']

	def __str__(self):
		return self.dog_name

	def get_absolute_url(self):
		return reverse('dog-detail', args=[str(self.id)])

class dog_breeds(models.Model):
	breed_name = models.CharField(max_length = 20, help_text = 'Enter a breed name')

	def __str__(self):
		return self.breed_name

class announcement(models.Model):
	made_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
	date_made = models.DateTimeField(auto_now_add=True)
	announce = models.TextField(help_text = 'Enter Announcement')

	class Meta:
		ordering = ['date_made']

	def __str__(self):
		return self.announce

	def get_absolute_url(self):
		return reverse('announcement-detail', args=[str(self.id)])


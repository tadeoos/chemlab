# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cgi
import uuid
from django.db import models


class Country(models.Model):
	""" Substance's country of origin.
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class City(models.Model):
	""" Substance's city of origin.
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=40)
	def __unicode__(self):
		return self.name


class Origin(models.Model):
	""" Substance's type of origin (online, offline etc.).
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class Source(models.Model):
	""" Substance's source of origin (user, anonymouse, etc).
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class Kind(models.Model):
	""" Kind of substance (stimulant, psychedelic etc).
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class TestMethod(models.Model):
	""" Testing methods used to analyze substance.
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)	
	def __unicode__(self):
		return self.name


class Apperance(models.Model):
	""" Substance's apperance
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class Color(models.Model):
	""" Substance's color.
	"""
	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class OriginCode(models.Model):
	""" Code of origin.
	"""
	modified = models.DateTimeField(auto_now=True)
	code = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.code


class Region(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class AcquiredFrom(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class UserCode(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	code = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.code


class SampleCode(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	code = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.code


class Substance(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.name


class Alias(models.Model):
	""" Substance origin's region """

	modified = models.DateTimeField(auto_now=True)
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.name


class Drug(models.Model):
	name = models.CharField(max_length=50)
	summary = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name


class SubstanceSurvey(models.Model):
	""" Substance survey """

	# Meta
	added = models.DateField(auto_now_add=True)
	uuid = models.UUIDField(primary_key=True,
							editable=False, 
							unique=True,
							default=uuid.uuid4)

	# Sample information
	region = models.ForeignKey(Region, null=True, blank=True)
	city = models.ForeignKey(City, null=True, blank=True)
	acquired_from = models.ForeignKey(AcquiredFrom, null=True, blank=True)
	origin = models.ForeignKey(Origin, null=True, blank=True)
	date_acquired = models.DateField(null=True, blank=True)
	price = models.CharField(max_length=255, blank=True)
	sample_code = models.CharField(max_length=255, null=True, blank=True)

	# Origin user
	user_code = models.ForeignKey(UserCode, null=True, blank=True)
	contact = models.CharField(null=True, blank=True, max_length=255)

	# Substance
	alias = models.ForeignKey(Alias, null=True, blank=True)
	substance = models.ForeignKey(Substance, null=True, blank=True)
	apperance = models.ForeignKey(Apperance, null=True, blank=True)
	kinds = models.ManyToManyField(Kind, blank=True)
	color = models.ManyToManyField(Color, blank=True)
	image = models.ImageField(upload_to='substances', blank=True)

	# Survey
	observations = models.TextField(blank=True)
	testmethods = models.ManyToManyField(TestMethod, blank=True)

	detected = models.ManyToManyField(Drug, blank=True)

	def get_detected(self):
		r = []
		for drug in self.detected.all():
			r.append("<span class='drug-tooltip badge badge-pill badge-primary' title='{}'>{}</span>".format(drug.summary, drug.name))
		return r

	def get_image_url(self):
		if self.image:
			return self.image.url
		else:
			return ""
			
	def __unicode__(self):
		return str(self.uuid)

	class Meta:
		ordering = ['-added']

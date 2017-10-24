# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models


class Country(models.Model):
	""" Substance's country of origin.
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class City(models.Model):
	""" Substance's city of origin.
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=40)
	def __unicode__(self):
		return self.name


class Origin(models.Model):
	""" Substance's type of origin (online, offline etc.).
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class Source(models.Model):
	""" Substance's source of origin (user, anonymouse, etc).
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class Kind(models.Model):
	""" Kind of substance (stimulant, psychedelic etc).
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class TestMethod(models.Model):
	""" Testing methods used to analyze substance.
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)	
	def __unicode__(self):
		return self.name


class Apperance(models.Model):
	""" Substance's apperance
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=30)
	def __unicode__(self):
		return self.name


class Color(models.Model):
	""" Substance's color.
	"""
	name = models.CharField(primary_key=True,
							unique=True,
							max_length=20)
	def __unicode__(self):
		return self.name


class OriginCode(models.Model):
	""" Code of origin.
	"""
	code = models.CharField(primary_key=True,
							unique=True,
							max_length=50)
	def __unicode__(self):
		return self.code


class SubstanceSurvey(models.Model):
	""" Substance survey.
	"""
	uuid = models.UUIDField(primary_key=True,
							editable=False, 
							unique=True,
							default=uuid.uuid4)

	added = models.DateTimeField(auto_now_add=True)
	date = models.CharField(max_length=255, blank=True)
	country = models.ForeignKey(Country, blank=True)
	city = models.ForeignKey(City, blank=True)
	origin = models.ForeignKey(Origin, blank=True)
	origin_code = models.ForeignKey(OriginCode, blank=True)
	source = models.ForeignKey(Source, blank=True)
	price = models.CharField(max_length=255, blank=True)

	alias = models.CharField(max_length=255, blank=True)
	substance = models.CharField(max_length=255, blank=True)
	apperance = models.ForeignKey(Apperance, blank=True)
	kind = models.ManyToManyField(Kind, blank=True)
	color = models.CharField(max_length=255, blank=True)
	image = models.ImageField(upload_to='substances', blank=True)
	observations = models.TextField(blank=True)
	test_methods = models.ManyToManyField(TestMethod, blank=True)

	def __unicode__(self):
		return self.substance

	class Meta:
		ordering = ['-added']
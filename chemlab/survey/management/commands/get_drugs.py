#-*- encode: utf-8 -*-

import requests
from survey.models import Drug
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

	def handle(self, *args, **options):
		r = requests.get('http://tripbot.tripsit.me/api/tripsit/getAllDrugNames')
		r_json = r.json()
		drug_list = r_json['data'][0]
		for drug in drug_list:
			if drug is not None:
				encoded_drug = drug.encode('utf-8')
				try:
					r = requests.get('http://tripbot.tripsit.me/api/tripsit/getDrug?name={}'.format(encoded_drug,))
					drug_json = r.json()
					summary = drug_json['data'][0]['properties']['summary']
				except:
					print('No summary for {}?'.format(encoded_drug,))
					summary = None

				Drug.objects.create(name=encoded_drug, summary=summary)
				print("'{}' added.".format(encoded_drug,))
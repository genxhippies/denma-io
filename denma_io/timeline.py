# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from common.models import Episode

def showPage(request):
	return render(request, 'timeline.html')

def showPubData(request):
	episodes = Episode.objects.all()
	pubDates = ''

	for episode in episodes:
		pubDates += '"' + episode.publish_date.strftime('%s') + '": 1,\n'

	pubDates = '{' + pubDates[:-2] + '}'

	return HttpResponse(pubDates, content_type='application/json')

# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from common.models import Episode

import json

def showPage(request):
	return render(request, 'timeline.html')

def showPubDate(request):
	episodes = Episode.objects.all()
	pubDates = ''

	for episode in episodes:
		pubDates += '"' + episode.publish_date.strftime('%s') + '": 1,\n'

	pubDates = '{' + pubDates[:-2] + '}'

	return HttpResponse(pubDates, content_type='application/json')

def showEpisode(request):

	if request.method == "POST":
		return HttpResponse('{}', content_type='application/json')

	queryDict = request.GET
	targetDate = queryDict.get('date')

	targetEpisode = Episode.objects.get(publish_date=targetDate);

	data = {
		"num": targetEpisode.num,
		"subtitle": targetEpisode.subtitle,
    	"publish_date": targetEpisode.publish_date.strftime('%Y-%m-%d'),
	    "note": targetEpisode.note,
    	"characters": targetEpisode.getCharacters(),
    	"url": targetEpisode.getUrl()
	}

	return HttpResponse(json.dumps(data), content_type='application/json')












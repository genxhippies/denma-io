# -*- coding: utf-8 -*-
from django.db import models

class Character(models.Model):
    id_en = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)
    desc = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.name

class Episode(models.Model):
    num = models.SmallIntegerField(unique=True)
    subtitle = models.CharField(max_length=1024)
    publish_date = models.DateField()
    note = models.TextField(default='', blank=True)
    characters = models.ManyToManyField(Character, blank=True)

    def __unicode__(self):
        return self.subtitle

    def save(self, *args, **kwargs):
        try:
            o = Episode.objects.get(
                num = self.num, 
            )
            self.id = o.id
            kwargs['force_update'] = True
        except Episode.DoesNotExist as e:
            kwargs['force_insert'] = True
            self.id = None  # To make new id using AutoField

        super(Episode, self).save(*args, **kwargs) # Call the "real" save() method.

    def getUrl(self):
        url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no={num}'.format(num=self.num)
        return url

    # for list_display() in Admin page
    def getCharacters(self):
        return ', '.join([str(c) for c in self.characters.all()])
    getCharacters.short_description = 'Characters' 


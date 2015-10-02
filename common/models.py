# -*- coding: utf-8 -*-
from django.db import models

class Episode(models.Model):
    num = models.SmallIntegerField()
    subtitle = models.CharField(max_length=1024)
    publish_date = models.DateTimeField()
    note = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.subtitle

    def getUrl(self):
        url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no={num}'.format(num=self.num)
        return url


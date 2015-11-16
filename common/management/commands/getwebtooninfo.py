#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from optparse import make_option

from common.models import Episode

import re
import time
import urllib2
import datetime
import traceback

class Command(BaseCommand):
    help = "Download & store DENMA webtoon information"

    option_list = BaseCommand.option_list + (
        make_option('--start-num', 
            action='store', 
            type='int',
            dest='start_num',
            default=1,
            help='First episode num to fetch',
        ),
        make_option('--end-num', 
            action='store', 
            type='int',
            dest='end_num',
            default=1,
            help='Last episode num to fetch',
        ),
        make_option('--latest', 
            action='store_true', 
            dest='latest',
            default=False,
            help='Last episode num to fetch',
        ),
        make_option('--sleep', 
            action='store', 
            type='int',
            dest='sleep',
            default=1,
            help='Sleep N seconds between download',
        ),
    )

    class PatternNotMatched(Exception):
        def __init__(self, message):
            self.message = message
        def __unicode__(self):
            return repr(self.message)

    def handle(self, *args, **options):
        subtitle_ptn = re.compile('<meta\s+property="og:description"\s+content="([^"]+)"\s+>')
        publishdate_ptn = re.compile('<dd\s+class="date">([0-9]+).([0-9]+).([0-9]+)</dd>')
        image_ptn = re.compile('<img[^>]+src="(http://imgcomic.naver.net/webtoon/119874/[^"]+)"')

        if options['latest'] == True:
            try:
                episode = Episode.objects.order_by('-num')[0]
                options['start_num'] = episode.num + 1
            except IndexError:
                options['start_num'] = 1
            options['end_num'] = options['start_num'] + 1

        for num in range(options['start_num'], options['end_num']):
            obj = Episode(num=num)
            opener = urllib2.build_opener()
            try:
                url = obj.getUrl()
                print 'Downloading {url}'.format(url=url)

                request = urllib2.Request(url)
                request.add_header('User-Agent', 'DenmaBot/1.0 +http://denma.io/')
                body = opener.open(request).read()

                m = subtitle_ptn.search(body)
                if m == None:
                    raise Command.PatternNotMatched('subtitle not matched')
                obj.subtitle = m.group(1)

                m = publishdate_ptn.search(body)
                if m == None:
                    raise Command.PatternNotMatched('publish_date not matched')
                obj.publish_date = datetime.date(
                    int(m.group(1)),
                    int(m.group(2)),
                    int(m.group(3)),
                )

                pos = 0
                note = ''
                while True:
                    m = image_ptn.search(body, pos)
                    if m == None:
                        break
                    note += m.group(1) + ';'
                    pos = m.end(1) + 1
                obj.note = note

                obj.save()

            except Command.PatternNotMatched as e:
                print "Episode {n} not yet uploaded.".format(n=num)
                break
            except Exception as e:
                print traceback.format_exc()
                raise e

            time.sleep(options['sleep'])



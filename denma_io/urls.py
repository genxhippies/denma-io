"""denma_io URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/js/pubDate', 'denma_io.timeline.showPubDate', name='timeline_pubData'),
    url(r'^timeline/js/episode', 'denma_io.timeline.showEpisode', name='timeline_episode'),
    url(r'^timeline/edit', 'denma_io.timeline.showEditPage', name='timeline_edit'),
    url(r'^timeline/', 'denma_io.timeline.showPage', name='timeline_index'),
    url(r'^$', 'denma_io.timeline.showPage'),
]

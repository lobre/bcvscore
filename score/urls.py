from django.conf.urls import patterns, url

urlpatterns = patterns(
    'score.views',
    url(r'^$', 'home'),
    url(r'^upcoming', 'upcoming')
)

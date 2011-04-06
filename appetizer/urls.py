from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url('^.*\.webapp$', 'appetizer.views.manifest', name='appetizer_manifest'),
)

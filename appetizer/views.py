from django.conf import settings

try:
    from django.contrib.sites.models import get_current_site
    current_site = get_current_site
except ImportError:
    from django.contrib.sites.models import Site
    current_site = Site.objects.get_current

from django.shortcuts import render_to_response

def manifest(request, template='appetizer/manifest.json'):
    site = current_site()
    site_name = site.name
    return render_to_response(template, locals(), mimetype='application/x-web-app-manifest+json')

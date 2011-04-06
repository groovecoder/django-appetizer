from django.conf import settings
from django.contrib.sites.models import Site, get_current_site
from django.shortcuts import render_to_response

def manifest(request, template='appetizer/manifest.json'):
    current_site = None
    try: get_current_site
    except NameError:
        current_site = Site.objects.get_current()
    else:
        current_site = get_current_site()
    site_name = current_site.name
    return render_to_response(template, locals(), mimetype='application/x-web-app-manifest+json')

from django.shortcuts import render_to_response

def manifest(request, template='appetizer/manifest.json'):
    return render_to_response(template, mimetype='application/x-web-app-manifest+json')

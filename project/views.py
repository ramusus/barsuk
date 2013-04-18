from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from forms import ContactForm

def index(request):
    setattr(settings, 'MEDIA_URL', '/media/%s/' % request.subdomain)
    context = RequestContext(request, {
        'form': ContactForm(request=request),
    })
    return render_to_response('%s/index.html' % request.subdomain, context)
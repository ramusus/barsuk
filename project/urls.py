from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from forms import ContactForm
from contact_form.views import contact_form

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static('/static/', document_root=settings.STATIC_ROOT) \
    + patterns('',
        url(r'^$', 'project.views.index', name='index'),
        url(r'^contact_form/$',
            contact_form,
            {'form_class': ContactForm, 'success_url': '/'},
            name='contact_form'),
#        url(r'^sent/$',
#            TemplateView,
#            { 'template': 'contact_form/contact_form_sent.html' },
#            name='contact_form_sent'),
)
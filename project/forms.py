# -*- coding: utf-8 -*-
from django import forms
from contact_form.forms import ContactForm as ContactFormOriginal, attrs_dict

class ContactForm(ContactFormOriginal):

    def __init__(self, data=None, files=None, request=None, *args, **kwargs):
        super(ContactForm, self).__init__(data=data, files=files, request=request, *args, **kwargs)
        self.subject_template_name = str(request.subdomain) + '/' + self.subject_template_name
        self.template_name = str(request.subdomain) + '/' + self.template_name
        self.fields['name'].label = u'Имя'
        self.fields['email'].label = u'E-mail'
        self.fields['body'].label = u'Телефон'
        self.fields['body'].widget = forms.TextInput(attrs=attrs_dict)
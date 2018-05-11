from django.shortcuts import render
from core.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {'form': form,
                   'success': success}
    return render(request, 'contact/contact.html', context)
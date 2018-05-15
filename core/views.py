from django.shortcuts import render
from core.forms import ContactForm


def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {'form': form,
               'success': success}
    return render(request, 'contact/contact.html', context)

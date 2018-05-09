from django.shortcuts import render
from account.forms import EditAccountForm
from account.forms import PasswordChangeCustomForm
from django.contrib.auth.decorators import login_required


@login_required()
def panel_user(request):
    template_name = 'account/panel.html'
    return render(request, template_name)


@login_required()
def edit_account(request):
    template_name = 'account/edit_account.html'
    form = EditAccountForm()
    context = {'form': form}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['sucess'] = True  # Essa variavel sucess sera usada no template
    else:
        form = EditAccountForm(instance=request.user)
    context = {'form': form}
    return render(request, template_name, context)


@login_required()
def edit_password(request):
    template_name = 'account/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeCustomForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['sucess'] = True
    else:
        form = PasswordChangeCustomForm(user=request.user)
    context = {'form': form}
    return render(request, template_name, context)

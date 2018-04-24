from django.shortcuts import render
from account.forms import EditAccountForm
from django.contrib.auth.decorators import login_required
from account.forms import PasswordChangeCustomForm


@login_required
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
    # def edit_user(request, perfil_id):
    #     user = User.objects.get(pk=perfil_id)
    #     user_form = UserProfileForm(instance=user)
    #     ProfileInlineFormset = inlineformset_factory(User, Profile, fields=(
    #                                                  'address', 'city', 'birth_date', 'phone',))
    #     formset = ProfileInlineFormset(instance=user)
    #
    #     if request.user.is_authenticated() and request.user.id == user.id:
    #         if request.method == 'POST':
    #             user_form = UserProfileForm(request.POST, request.FILES, instance=user)
    #             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
    #
    #             if user_form.is_valid():
    #                 created_user = user_form.save(commit=False)
    #                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
    #
    #                 if formset.is_valid():
    #                     created_user.save()
    #                     formset.save()
    #                     return HttpResponse('Formulario Atualizado!')
    #         return render(request, 'account/panel.html', {'noodle': perfil_id,
    #                                                                'noodle_form': user_form,
    #                                                                'formset': formset})
    #     else:
    #         raise PermissionDenied

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
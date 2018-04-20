from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from app_profile.forms import UserProfileForm
from app_profile.models import Profile
from django.forms import inlineformset_factory
from account.forms import EditAccountForm


@login_required
def panel_user(request):
    template_name = 'account/panel.html'
    return render(request, template_name)

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
#     ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('address', 'city', 'birth_date', 'phone',))
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
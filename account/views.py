from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from account.forms import RegisterUserForm
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class RegisterUserView(TemplateView):
    template_name = 'account/register.html'

    def get(self, request):
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password') # password criptografado
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse_lazy('account:home'))
        args = {'form': form}
        return render(request, self.template_name, args)


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'account/home.html'

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)


def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, 'account/home.html', {'user': user})
    return render(request, 'account/login.html')


def do_logout(request):
    logout(request)
    return redirect(reverse_lazy('account:login'))

from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': ''}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': ''}),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'E-mail', 'required': ''})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            return self.adiciona_erro("Password don't match")
        return cd['password2']

    def is_valid(self):
        valid = True
        if not super(RegisterUserForm, self).is_valid():
            valid = False

        user_exists = User.objects.filter(username=self.data['username']).exists()
        email_exists = User.objects.filter(email=self.data['email']).exists()

        if user_exists:
            self.adiciona_erro('A user with that username already exists.')
            valid = False

        if email_exists:
            self.adiciona_erro('A user with that e-mail already exists.')
            valid = False

        return valid

    def adiciona_erro(self, message):
        erros = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        erros.append(message)

    def save(self, commit=True):  # Metodo para encriptar password do formulario para enviar ao banco.
        user = super(RegisterUserForm, self).save(
            commit=False)  # Não salva no banco ainda, tenho que fazer mais uma coisa
        user.set_password(self.cleaned_data['password'])  # Encriptando password
        if commit:
            user.save()
        return user



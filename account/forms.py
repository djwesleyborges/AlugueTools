from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class RegisterUserForm(forms.ModelForm):
    # password = forms.RegexField(label='Password', regex='^(?=.*\W+).*$',
    #                             help_text='Password must be six characters long and contain at least one '
    #                                       'non-alphanumeric character.',
    #                             widget=forms.PasswordInput(
    #                                 attrs={'class': 'form-control', 'placeholder': 'Password'})
    #                             )
    #
    # password2 = forms.RegexField(label='Password confirmation', regex='^(?=.*\W+).*$',
    #                              help_text='Password must be six characters long and contain at least one '
    #                                        'non-alphanumeric character.',
    #                              widget=forms.PasswordInput(
    #                                  attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'})
    #                              )

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


class EditAccountForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'birth_date', 'phone']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('A user with that e-mail already exists.')
        return email


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # A implementacao acima compacta esta abaixo em um for.
            # self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
            # self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
            # self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


# class FormLogin(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
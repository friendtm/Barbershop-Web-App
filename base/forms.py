from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegistrationForm(UserCreationForm):
    fname = forms.CharField(max_length=30, required=True)
    lname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = "Username"
        self.fields['username'].help_text = "Deve conter menos do que 12 caracteres. Letras, números e @/./+/-/_"
        
        self.fields['fname'].label = "Nome"
        self.fields['fname'].help_text = "<br>"
        
        self.fields['lname'].label = "Apelido"
        
        self.fields['email'].label = "Email"
        self.fields['email'].help_text = "<br>"
        
        self.fields['password1'].label = "Password"
        self.fields['password1'].help_text = "Obrigatório mais do que 8 caracateres. Evita usar apenas números."
        self.fields['password2'].label = "Confirmar Password"
        self.fields['password2'].help_text = " "
        
        self.helper = FormHelper()
        self.helper.form_method = "POST"

  
class UpdateProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Atualizar'))

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"
        
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
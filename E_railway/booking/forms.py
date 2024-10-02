from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User
from .models import Contact




class RegistrationForm(UserCreationForm):
    ROLES = [
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('passenger', 'Passenger'),
        ('maintenance', 'Maintenance'),
    ]
    role = forms.ChoiceField(choices=ROLES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=254)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

from .models import Task, CustomUser
from .models import Communication


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type', 'ticket_quota', 'is_on_guard', 'status', 'sanction', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'task_type': forms.Select(attrs={'class': 'form-control'}),
            'sanction': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ['name', 'description', 'photo', 'destination']

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            if photo.size > 4 * 1024 * 1024:
                raise forms.ValidationError("Image file too large ( > 4MB )")
            if not photo.content_type.startswith('image'):
                raise forms.ValidationError("File is not an image")
        return photo


from .models import DamageReport

class DamageReportForm(forms.ModelForm):
    class Meta:
        model = DamageReport
        fields = ['damage_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'damage_type': forms.Select(attrs={'class': 'form-control'}),
        }
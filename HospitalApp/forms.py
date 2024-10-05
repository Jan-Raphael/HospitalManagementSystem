from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import PatientAccount, DoctorAccount, Appointment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = PatientAccount
        fields = ['phone_number', 'address']

class DoctorSignupForm(forms.ModelForm):
    class Meta:
        model = DoctorAccount
        fields = ['specialty', 'qualification', 'years_of_experience']

class PatientLoginForm(AuthenticationForm):
    class Meta:
        model = PatientAccount
        fields = ['username', 'password']

class DoctorLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=DoctorAccount.objects.filter(is_doctor=True),
        label="Select Doctor",
        required=True
    )
    appointment_date = forms.DateField(
        widget=forms.SelectDateWidget,
        label="Appointment Date",
        required=True
    )
    appointment_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'),
        label="Appointment Time",
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label="Reason for Appointment",
        required=False
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'description']
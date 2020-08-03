from django import forms
from .models import User


class JoinForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ['email', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super(JoinForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'email address', 'style': 'margin-bottom:10px'})
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'date_of_birth', 'style': 'margin-bottom:10px'})

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

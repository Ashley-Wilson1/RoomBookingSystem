from django import forms

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    role = forms.ChoiceField(choices=[('staff', 'Staff'), ('student', 'Student')], required=True)

    def signup(self, request, user):
        from allauth.account.forms import SignupForm  # Lazy import here
        user = super(CustomSignupForm, self).signup(request, user)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.role = self.cleaned_data.get('role')
        user.save()
        return user

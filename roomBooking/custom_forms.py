# roomBooking/custom_forms.py
from django import forms

def get_signup_form():
    from allauth.account.forms import SignupForm  # Import inside function to avoid circular import

    class CustomSignupForm(SignupForm):
        first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
        last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
        role = forms.ChoiceField(choices=[('staff', 'Staff'), ('student', 'Student')], required=True)

        def signup(self, request, user):
            # Call the original signup method
            user = super().signup(request, user)
            # Save custom fields to the user model
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.role = self.cleaned_data.get('role')
            user.save()
            return user

    return CustomSignupForm

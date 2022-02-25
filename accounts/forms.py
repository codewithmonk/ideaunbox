from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Adding custom user creation form to handle the user creation.
    Add in any new fields required in here post adding it to the fields in the CustomUserModel if it needs to be addressed during creation
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username') # password is implicitly included hence need not mention explicitly



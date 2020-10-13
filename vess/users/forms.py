from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import HealthCareUser

class HealthCareUserCreationForm(UserCreationForm):

    class Meta:
        model = HealthCareUser
        fields = UserCreationForm.Meta.fields + ('id', 'first_name', 'last_name', 'email', 'role')

class HealthCareUserChangeForm(UserChangeForm):

    class Meta:
        model = HealthCareUser
        fields = UserChangeForm.Meta.fields
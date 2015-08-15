from django.forms import ModelForm, PasswordInput
from score.models import SiteConfiguration


class SiteConfigurationForm(ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }

from django import forms
from basicapp.models import User
from django.core import validators

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','email')

    #AFTER POST VALIDATION
    def clean(self):
        all_clean_data=super().clean()
        last_name= all_clean_data['first_name']
        if len(last_name)>3:
            raise forms.ValidationError('first name is too long')

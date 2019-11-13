from django import forms

from .models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_registration', 'date_birthday')


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

from django import forms
from .models import Personaldetails

class PersonaldetailsForm(forms.ModelForm):
    class Meta:
        model=Personaldetails
        fields=('name','register_no','year','cgpa','ph_no') 
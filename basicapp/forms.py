from django import forms
from django.core import validators
import datetime 
from faker import Faker
fakegen = Faker()
class FormName(forms.Form):
    name = forms.CharField(initial=fakegen.name())
    email = forms.EmailField(initial=fakegen.email())
    text = forms.CharField(initial=fakegen.sentence(nb_words=10), widget=forms.Textarea) 
    date = forms.DateField(initial=fakegen.date_between_dates(date_start=datetime.date(2020,1,1), date_end=datetime.date(2022,12,31)))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Gotcha bot!")
        return botcatcher
    
    def clean_name(self):
        return fakegen.name()
    def clean_email(self):
        return fakegen.email()
    def clean_text(self):
        return fakegen.sentence(nb_words=10)
    def clean_date(self):
        return fakegen.date_between_dates(date_start=datetime.date(2020,1,1), date_end=datetime.date(2022,12,31))


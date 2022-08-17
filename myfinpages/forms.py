from django import forms

from myfinpages.models import Income


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'date', 'type', 'notes']
        widgets = {
            'date': DateInput()
        }

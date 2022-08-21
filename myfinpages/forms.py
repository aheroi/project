from django import forms
from datetime import date

from myfinpages.models import Income, Outcome, Balance


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['value', 'date', 'type', 'notes', 'comment_to_notes']
        # widgets = {
        #     'date': DateInput()
        # }
    date = forms.DateField(widget=DateInput, initial=date.today())
    # comment_to_notes = forms.CharField(required=False, widget=forms.Textarea(
    #     attrs = {
    #         'placeholder': 'give some comment',
    #         'class': 'some-class-for-html',
    #         'id': 'some-id-for-html',
    #         'rows': 10  # won't work with crispy
    #         'cols': 10  # won't work with crispy
    #     }), help_text='this comment is not required')
    ##
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    def is_valid(self):
        is_valid = super().is_valid()

        return is_valid

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     # do sth here...
    #     if commit:
    #         instance.save()
    #     return instance


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ['value', 'date', 'type', 'notes', 'comment_to_notes']

    date = forms.DateField(widget=DateInput, initial=date.today())


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'date', 'type', 'notes', 'comment_to_notes']

    date = forms.DateField(widget=DateInput, initial=date.today())

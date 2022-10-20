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
    comment_to_notes = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'you can give some comment',
            'rows': 1,
        }), help_text='this comment is not required')
    ##
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    def is_valid(self):
        is_valid = super().is_valid()
        value = self.cleaned_data.get('value')

        if value <= 0:
            self.add_error('value', 'Value must be a positive number')
            is_valid = False

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
    comment_to_notes = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'you can give some comment',
            'rows': 1,
        }), help_text='this comment is not required')

    def is_valid(self):
        is_valid = super().is_valid()
        value = self.cleaned_data.get('value')

        if value <= 0:
            self.add_error('value', 'Value must be a positive number')
            is_valid = False

        return is_valid


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['value', 'date', 'type', 'notes', 'comment_to_notes']

    date = forms.DateField(widget=DateInput, initial=date.today())
    comment_to_notes = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'placeholder': 'you can give some comment',
            'rows': 1,
        }), help_text='this comment is not required')

    def is_valid(self):
        is_valid = super().is_valid()
        value = self.cleaned_data.get('value')

        if value <= 0:
            self.add_error('value', 'Value must be a positive number')
            is_valid = False

        return is_valid

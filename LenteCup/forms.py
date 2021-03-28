from django import forms

from LenteCup.models import Week, Scores


class WeekForm(forms.ModelForm):

    class Meta:
        model = Week
        fields = "__all__"


class ScoresForm(forms.ModelForm):

    class Meta:
        model = Scores
        fields = "__all__"


class ChangeFirstNameForm(forms.Form):
    firstname = forms.CharField(max_length=30, help_text="Enter your Name")


class StandInvoerForm(forms.Form):
    score = forms.IntegerField(min_value=0, max_value=40)
    week = forms.Select()
    qualifying = forms.BooleanField(required=True)
    baan = forms.CharField()
    lus = forms.CharField()

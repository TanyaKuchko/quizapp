from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from .models import Quiz, Game


class CreateQuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ("name", "logo", "city", "max_number_of_participants")


class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ("date_of_event", "place", "max_number_of_teams")


class TeamRegistrationForm(forms.Form):

    def __init__(self, quiz, *args, **kwargs):
        super(TeamRegistrationForm, self).__init__(*args, **kwargs)
        self.quiz = quiz

    team_name = forms.CharField(max_length=50)
    number_of_participants = forms.IntegerField()
    contact_person = forms.CharField()
    email = forms.EmailField()
    phone_number = PhoneNumberField()

    def clean_number_of_participants(self):
        value = self.cleaned_data["number_of_participants"]
        max_number_of_participants = self.quiz.max_number_of_participants
        if value > max_number_of_participants:
            raise ValidationError(f"Number of participants should be less or equal {max_number_of_participants}")
        return value




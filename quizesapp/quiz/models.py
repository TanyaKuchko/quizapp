from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=60, unique=True)
    logo = models.ImageField(upload_to="quizes/", blank=True)
    city = models.CharField(max_length=30)
    max_number_of_participants = models.IntegerField(null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Game(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date_of_event = models.DateTimeField()
    place = models.CharField(max_length=100)
    max_number_of_teams = models.IntegerField(null=False)

    def is_registration_open(self):
        registrations_count = self.gameregistration_set.count()
        if registrations_count >= self.max_number_of_teams:
            return False
        return True

    def __str__(self):
        return str(self.quiz)


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="teams/", blank=True)

    def __str__(self):
        return self.name


class GameRegistration(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number_of_participants = models.IntegerField(null=False)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    phone_number = PhoneNumberField(null=False, blank=False)

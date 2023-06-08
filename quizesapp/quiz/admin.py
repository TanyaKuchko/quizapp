from django.contrib import admin
from .models import Quiz, Game, Team, GameRegistration


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "city", "max_number_of_participants", "owner")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("quiz", "date_of_event", "place", "max_number_of_teams")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")


@admin.register(GameRegistration)
class GameRegistrationAdmin(admin.ModelAdmin):
    list_display = ("game", "team", "number_of_participants", "contact_person", "email", "phone_number")


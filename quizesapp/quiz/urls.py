from django.urls import path
from .views import (
    QuizView,
    QuizOwnersView,
    TeamRegistrationView,
    UpcomingEventsView,
    SearchView,
    CreateQuizView,
    DeleteQuiz,
    CreateEventView,
    QuizDetailsView,

)


urlpatterns = [
    path("", QuizView.as_view(), name='quiz-index'),
    path("forquizowners/", QuizOwnersView.as_view(), name='quizowners-index'),
    path("teamregistration-<int:game_id>", TeamRegistrationView.as_view(), name='teamregistration'),
    path("upcomingevents/", UpcomingEventsView.as_view(), name='upcomingevents-index'),
    path("search/", SearchView.as_view(), name='quiz-search'),
    path("create_quiz/", CreateQuizView.as_view(), name='create-quiz'),
    path("delete_quiz-<int:quiz_id>", DeleteQuiz.as_view(), name="delete-quiz"),
    path("create_event-<int:quiz_id>", CreateEventView.as_view(), name="create-event"),
    path("quiz_details-<int:quiz_id>", QuizDetailsView.as_view(), name='quiz-details'),

]

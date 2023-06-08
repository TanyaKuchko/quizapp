from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from .forms import CreateQuizForm, CreateEventForm, TeamRegistrationForm
from .models import Quiz, Game, Team, GameRegistration


class QuizView(TemplateView):
    template_name = "quiz/quiz.html"

    def get(self, request):
        games = Game.objects.all().order_by('date_of_event')
        available_games = []
        for game in games:
            if game.is_registration_open():
                available_games.append(game)

        params = {
            'games': available_games,
        }

        return render(request, self.template_name, params)


class QuizOwnersView(TemplateView):
    template_name = "quiz/forquizowners.html"

    @method_decorator(login_required)
    def get(self, request):
        quizzes = Quiz.objects.filter(owner=request.user).order_by('name')

        params = {
            'quizzes': quizzes,
        }

        return render(request, self.template_name, params)


class UpcomingEventsView(TemplateView):
    template_name = "quiz/upcoming_events.html"

    def get(self, request):
        games = Game.objects.all().order_by('date_of_event')
        available_games = []
        for game in games:
            if game.is_registration_open():
                available_games.append(game)

        params = {
            'games': available_games,
        }

        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = "quiz/upcoming_events.html"

    def get(self, request):
        search = request.GET['search']

        search_list = search.split()
        keyword = search_list.pop(0)
        quizzes = Quiz.objects.filter(name__icontains=keyword) | Quiz.objects.filter(city__icontains=keyword)
        games = Game.objects.filter(quiz__in=quizzes)

        params = {
            "games": games,
        }

        return render(request, self.template_name, params)


class CreateQuizView(TemplateView):
    template_name = "quiz/create_quiz.html"

    def post(self, request):
        if request.method == 'POST':
            form = CreateQuizForm(request.POST, request.FILES)
            if form.is_valid():
                new_quiz = form.save(commit=False)
                new_quiz.owner = request.user
                new_quiz.save()
                return redirect('quizowners-index')
            else:
                return render(request, self.template_name, {'form': form})


class DeleteQuiz(View):
    @method_decorator(login_required)
    def post(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        if request.user == quiz.owner:
            quiz.delete()
            return redirect('quizowners-index')
        else:
            return redirect('quizowners-index')


class CreateEventView(TemplateView):
    template_name = "quiz/create_event.html"

    def post(self, request, quiz_id):
        if request.method == 'POST':
            form = CreateEventForm(request.POST, request.FILES)
            if form.is_valid():
                quiz = Quiz.objects.get(id=quiz_id)
                new_game = form.save(commit=False)
                new_game.quiz = quiz
                new_game.save()
                return redirect('quizowners-index')
            else:
                return render(request, self.template_name, {'form': form})


class TeamRegistrationView(TemplateView):
    template_name = "registration/teamregistration.html"

    def post(self, request, game_id):
        game = Game.objects.get(id=game_id)
        form = TeamRegistrationForm(game.quiz, request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            team_name = cleaned_data["team_name"]
            team, _ = Team.objects.get_or_create(name=team_name)
            number_of_participants = cleaned_data["number_of_participants"]
            contact_person = cleaned_data["contact_person"]
            email = cleaned_data["email"]
            phone_number = cleaned_data["phone_number"]
            GameRegistration.objects.create(
                game=game,
                team=team,
                number_of_participants=number_of_participants,
                contact_person=contact_person,
                email=email,
                phone_number=phone_number
            )
            return render(request, "registration/successful_registration.html")
        else:
            return render(request, self.template_name, {'form': form})


class QuizDetailsView(TemplateView):
    template_name = "quiz/quiz_details.html"

    def get(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id, owner=request.user)
        games = Game.objects.filter(quiz=quiz).order_by('date_of_event')

        params = {
            'games': games,
        }

        return render(request, self.template_name, params)

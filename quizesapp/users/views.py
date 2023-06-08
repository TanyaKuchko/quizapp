from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class SignUpView(TemplateView):
    template_name = "registration/quizownerregistration.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            new_user = authenticate(
                email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password2']
            )
            login(request, new_user)
            return redirect('quizowners-index')
        return render(request, self.template_name, {'user_form': user_form})

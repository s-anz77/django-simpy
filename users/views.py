from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form':form})

@login_required
def profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileImageForm(request.POST, request.FILES, instance=user_profile)
        update_user_form = UserUpdateForm(request.POST, instance=request.user)

        if profile_form.is_valid() and update_user_form.is_valid():
            update_user_form.save()
            profile_form.save()

            messages.success(request, 'Ваши данные были успешно обновлены!')
            return redirect('profile')
    else:
        profile_form = ProfileImageForm(instance=user_profile)
        update_user_form = UserUpdateForm(instance=request.user)

    data = {
        'profile_form': profile_form,
        'update_user_form': update_user_form
    }
    
    return render(request, 'users/profile.html', data)

class CustomLoginView(LoginView):
    template_name = 'users/user.html'

    def form_valid(self, form):
        username = form.get_user().username
        messages.success(self.request, f'Приветствуем вас {username}!')
        return super().form_valid(form)
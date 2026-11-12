from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Введите логин', 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Придумайте логин', "autocomplete": "off"})
        )
    email = forms.CharField(
        label='Введите Email', 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш Email', "autocomplete": "off"})
        )
    # users = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль', 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Придумайте пароль', "autocomplete": "new-password"}), 
        )
    password2 = forms.CharField(
        label='Подтвердите пароль', 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', "autocomplete": "new-password"})
        )

    def clean_email(self):
        email = self.cleaned_data["email"].strip()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Пользователь с такой почтой уже зарегистрирован."
            )

        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Новый логин', 
        required=False, 
        help_text='Нельзя вводить символы: @, #, &',
        widget=forms.TextInput(attrs={'placeholder': 'Ваш новый логин'})
        )
    
    email = forms.CharField(
        label='Новый Email', 
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш новый Email'})
        )

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImageForm(forms.ModelForm): 
    img = forms.ImageField(
        label='Обновить фото', 
        required=False,
        widget=forms.FileInput
        )

    SEX_CHOICES = [
            ("undefined", "Не выбрано"),
            ("male", "Мужской"),
            ("female", "Женский"),
        ]
    sex = forms.ChoiceField(
        label='Ваш пол',
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={"class": "sex-select"})
        )

    privacy = forms.BooleanField(
        label="Я согласен на уведомления на почту",
        required=False,
    )

    class Meta:
        model = Profile
        fields = ['img', 'sex', 'privacy']

from django import forms
from .models import Messages
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    title = forms.CharField(
        label='Тема письма', 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Тема письма'})
        )

    email = forms.EmailField(
            label='Ваш Email', 
            required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Ваш Email'})
            )

    text = forms.CharField(
            label='Текст письма', 
            required=True,
            widget=forms.Textarea(attrs={'placeholder': 'Текст письма'})
            )
    
    

    class Meta:
        model = Messages
        fields = ['title', 'email', 'text']
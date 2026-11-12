from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['title'] = f'Статьи пользователя: {self.kwargs.get('username')}'

        return ctx

class NewsDetailView(DetailView):
    model = News
    context_object_name = 'post'

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        messages.success(self.request, 'Статья успешно добавлена!')
        return super().form_valid(form)

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/update_news.html'
    
    fields = ['title', 'text']
    
    def form_valid(self, form):
        form.instance.avtor = self.request.user
        messages.success(self.request, 'Статья успешно обновлена!')
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['title'] = self.object.title

        return ctx

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete_news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
    
            ctx['title'] = self.object.title
    
            return ctx

def uslugi(request):
    return render(request, 'blog/uslugi.html')

def about(request):
    return render(request, 'blog/about.html')


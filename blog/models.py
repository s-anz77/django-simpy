from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")
    

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
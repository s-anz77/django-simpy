from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='user_images/default.png', upload_to='user_images')
    SEX_CHOICES = [
        ("undefined", "Не выбрано"),
        ("male", "Мужской"),
        ("female", "Женский"),
    ]
    sex = models.TextField(
        'Пол', 
        max_length=10,
        choices=SEX_CHOICES,
        default="undefined",)

    privacy = models.BooleanField(
        'Согласие на рассылку',
        default=False
    )

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        old = Profile.objects.filter(pk=self.pk).first() if self.pk else None
        old_image = old.img if old else None

        super().save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

        if old_image and old_image.name != self.img.name:
            default_image = 'user_images/default.png'
            if old_image.name != default_image and os.path.isfile(old_image.path):
                os.remove(old_image.path)

    class Meta:
            verbose_name = 'Профиль'
            verbose_name_plural = 'Профили'

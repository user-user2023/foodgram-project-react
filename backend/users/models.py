from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+'
            )
        ]
    )
    email = models.EmailField(
        'email address',
        max_length=254,
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=False,
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email', ],
                name='unique_name'
            ),
        ]
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='Автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followings',
        verbose_name='Подписчик',
        null=False,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique-author-user'
            )
        ]
        ordering = ('id',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user} подписан на {self.author}'

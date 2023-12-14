from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .validators import validate_username

import uuid


class UserManager(models.Manager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('Имя пользователя обязательно')
        if not password:
            raise ValueError('Пароль обязателен')
        
        validate_username(username)
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        """Извлекает экземпляр пользователя, используя значение USERNAME_FIELD"""
        return self.get(**{self.model.USERNAME_FIELD: username})


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=64, 
        unique=True, 
        validators=[validate_username],
    )
    last_login = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return self.username

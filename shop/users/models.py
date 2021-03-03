from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
                                       BaseUserManager, \
                                       PermissionsMixin


class MyUserManager(BaseUserManager):
    """Класс менеджера пользователей"""

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        """Метод для создания обычного пользователя"""

        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        """Создание админа сайта"""

        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username']  # Список имён полей для Superuser

    objects = MyUserManager()  # методы класса MyUserManager

    def __str__(self):
        return self.username

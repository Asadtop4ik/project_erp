from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser, PermissionsMixin):
    ADMIN = 'admin'
    MANAGER1 = 'manager1'
    MANAGER2 = 'manager2'
    MANAGER3 = 'manager3'
    CASHIER = 'cashier'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER1, 'Manager1'),
        (MANAGER2, 'Manager2'),
        (MANAGER3, 'Manager3'),
        (CASHIER, 'Cashier'),
    )
    password = models.CharField(_('password'), max_length=128)
    username = models.CharField(_('username'), max_length=150, unique=True)
    role = models.CharField(_('role'), max_length=10, choices=ROLE_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


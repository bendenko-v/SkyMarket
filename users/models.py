from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(TextChoices):
    ADMIN = 'admin', _('Admin')
    USER = 'user', _('User')


class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50, null=False, blank=False)
    last_name = models.CharField(_('Last name'), max_length=150, null=False, blank=False)
    phone = PhoneNumberField(_('Phone number'))
    role = models.CharField(_('Role'), max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

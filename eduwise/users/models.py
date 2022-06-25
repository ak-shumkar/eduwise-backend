from django.contrib.auth.models import UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

AGENT = 'A'
STUDENT = 'S'

ROLE_CHOICES = [
    (AGENT, 'Agent'),
    (STUDENT, 'Student'),
]


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=128, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    role = models.CharField(choices=ROLE_CHOICES, default=STUDENT, max_length=1)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):  # pragma: no cover
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def fullname(self):
        """ Return the first_name plus the last_name, with a space in between."""
        return f'{self.first_name} {self.last_name}'.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send email to this user"""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_student(self):
        return self.role == STUDENT

    @property
    def is_agent(self):
        return self.role == AGENT


class StudentProfile(models.Model):
    first_name = models.CharField(max_length=128, default="")
    last_name = models.CharField(max_length=128, default="")
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=8, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey("locations.Country", null=True, blank=True, on_delete=models.PROTECT)
    phone = PhoneNumberField(blank=True, null=True)

    education_level = models.CharField(max_length=64, null=True, blank=True)
    motivation = models.TextField(null=True, blank=True)

    user = models.OneToOneField(User, related_name="profile", on_delete=models.PROTECT)

    class Meta:
        db_table = "student_profile"

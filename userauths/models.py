from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

class User(AbstractUser):
    phone_validator = RegexValidator(
        regex=r'^(07|01)\d{8}$',
        message="Phone number must start with 07 or 01 and be exactly 10 digits."
    )

    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[phone_validator],
        default="0700000000",  # Default phone number
        help_text="Enter a valid phone number starting with 07 or 01"
    )

    username = models.CharField(max_length=100, unique=True)
    bio = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "phone"  # Authenticate with phone instead of email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image")
    full_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200) # +234 (456) - 789
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.full_name} - {self.bio}"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200) # +234 (456) - 789
    subject = models.CharField(max_length=200) # +234 (456) - 789
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return self.full_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)




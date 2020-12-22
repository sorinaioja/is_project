from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

import os


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None, ):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.is_applicant = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'


def get_default_profile_image():
    return "codingwithmitch/logo_1080_1080.png"


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                      default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def set_applicant(self):
        self.is_applicant = True


class Applicant(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    user.is_applicant = True
    aid = models.AutoField(unique=True, primary_key=True)  # applicant identification
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    user.is_company = True
    cip = models.AutoField(unique=True, primary_key=True)  # unique physician identification number
    name = models.CharField(max_length=100, blank=True)
    field = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=500, blank=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to='company_image')


    def __str__(self):
        return self.user.username


# = models.CharField(max_length=20)
# days_available = models.DateTimeField(null=True)


@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_applicant:
            Applicant.objects.create(user=instance)
        # elif instance.is_company:
        #     Company.objects.create(user=instance)

# @receiver(post_save, sender=Account)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.is_applicant:
#         instance.applicant.save()
#     elif instance.is_company:
#         instance.company.save()

# class Company(models.Model):
# 	name = models.CharField(max_length=100, unique=True)
# 	about = models.TextField(max_length=500)
# 	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
# 	field = models.CharField(max_length=50)
#
# 	def __str__(self):
# 		return self.name

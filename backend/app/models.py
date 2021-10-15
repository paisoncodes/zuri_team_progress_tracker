from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=300, null=True)
    about = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Intern(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    username = models.CharField(unique=True, max_length=255, verbose_name="Slack name")
    full_name = models.CharField(max_length=100)
    stack = models.CharField(max_length=1000)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField()
    state = models.CharField(max_length=200)
    batch = models.IntegerField(verbose_name="Year")
    is_employed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Jobs(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name="job")
    job_title = models.CharField(max_length=255)
    gotten_at = models.DateTimeField()
    company_name = models.CharField(max_length=255, verbose_name="Organization name")
    last_updated_at = models.DateTimeField()
    job_description = models.CharField(max_length=255)
    currently_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    job_logo = models.URLField()

    def __str__(self):
        return self.company_name


class NewsLetter(models.Model):
    subscriber_email = models.EmailField(max_length=200, blank=False)

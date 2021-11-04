from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
import uuid

# Create your models here.

# ==================================================================================================================
class User(AbstractBaseUser):
    PERMISSION_CHOICES = (("S", "Staff"), ("A", "Admin"))
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, default="Admin")
    last_name = models.CharField(max_length=100, default="Admin")
    date = models.DateTimeField(auto_now_add=True)
    permissions = models.CharField(max_length=1, choices=PERMISSION_CHOICES, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    image = models.URLField(default="https://www.seekpng.com/ima/u2y3q8t4t4o0a9a9/")

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


# ==================================================================================================================


class Stack(models.Model):
    """Model definition for Stack."""

    # TODO: Define fields here
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=50)
    batch = models.IntegerField()

    class Meta:
        """Meta definition for Stack."""

        verbose_name = "Stack"
        verbose_name_plural = "stacks"
        unique_together = [["name", "batch"]]

    def __str__(self):
        """Unicode representation of Stack."""
        return str(self.name)


# ==================================================================================================================


class Intern(models.Model):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField()
    state = models.CharField(max_length=200)
    batch = models.IntegerField(verbose_name="Year")
    is_employed = models.BooleanField(default=False)
    current_salary = models.IntegerField(default=0)
    picture = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    stack = models.ManyToManyField(Stack, related_name="intern_stack", blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-created_at",)


# ==================================================================================================================


class Jobs(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name="job")
    job_title = models.CharField(max_length=255)
    gotten_at = models.DateField()
    company_name = models.CharField(max_length=255, verbose_name="Organization name")
    job_description = models.CharField(max_length=255)
    currently_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    job_logo = models.URLField(default="https://www.seekpng.com/ima/u2y3q8t4t4o0a9a9/")

    def __str__(self):
        return self.company_name


# ==================================================================================================================


class NewsLetter(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    subscriber_email = models.EmailField(max_length=200, blank=False)


# ==================================================================================================================


class Statistic(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    male = models.IntegerField()
    female = models.IntegerField()
    year = models.IntegerField(unique=True)
    finalist = models.IntegerField()

    def __str__(self):
        return str(self.year)

    @property
    def participant(self):
        return self.male + self.female


# ==================================================================================================================


class Sponsor(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=800)
    logo = models.URLField(
        default="https://ingressive.org/wp-content/uploads/2020/05/I4G-Logo-Color-Cropped.png"
    )

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class HealthCareUser(AbstractUser):

    class Role(models.TextChoices):

        ADMIN = ('ADMIN', 'Admin')
        DOCTOR = ('DOCTOR', 'Doctor')
        LABORATORY = ('LABORATORY', 'Laboratory')
        IMAGING = ('IMAGING', 'imaging')
        NURSE = ('NURSE', 'nurse')

    id = models.PositiveIntegerField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    email = models.EmailField(blank=False)
    role = models.CharField(max_length=32, choices=Role.choices, default=Role.ADMIN)

    REQUIRED_FIELDS = ['id', 'first_name', 'last_name', 'email', 'role']

    def __str__(self):
        return str(self.id)

class AdminHealthCareUserManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(HealthCareUser.Role.ADMIN)

class AdminHealthCareUser(HealthCareUser):

    objects = AdminHealthCareUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = HealthCareUser.Role.ADMIN
        return super().save(*args, **kwargs)

class DoctorHealthCareUserManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(HealthCareUser.Role.DOCTOR)

class DoctorHealthCareUser(HealthCareUser):

    objects = DoctorHealthCareUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = HealthCareUser.Role.DOCTOR
        return super().save(*args, **kwargs)

class LaboratoryHealthCareUserManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(HealthCareUser.Role.LABORATORY)

class LaboratoryHealthCareUser(HealthCareUser):

    objects = LaboratoryHealthCareUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = HealthCareUser.Role.LABORATORY
        return super().save(*args, **kwargs)

class ImagingHealthCareUserManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(HealthCareUser.Role.IMAGING)

class ImagingHealthCareUser(HealthCareUser):

    objects = ImagingHealthCareUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = HealthCareUser.Role.IMAGING
        return super().save(*args, **kwargs)

class NurseHealthCareUserManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(HealthCareUser.Role.NURSE)

class NurseHealthCareUser(HealthCareUser):

    objects = NurseHealthCareUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = HealthCareUser.Role.NURSE
        return super().save(*args, **kwargs)
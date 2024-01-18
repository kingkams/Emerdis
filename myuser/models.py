from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import uuid
import pyotp


class UserAccountManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, contact, password, **kwargs):
        if contact is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')

        user = self.model(contact=contact)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, contact, password, **kwargs):
        user = self.create_user(
            contact=contact,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        PEOPLE = "PEOPLE", "people"
        ASSEMBLY = "ASSEMBLY", "assembly"

    public_id = models.UUIDField(db_index=True,  unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    type = models.CharField(max_length=8, choices=Types.choices, default=Types.PEOPLE)
    contact = PhoneNumberField(unique=True)
    institution = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    town = models.CharField(max_length=255)
    is_people = models.BooleanField(default=False)
    is_assembly = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "contact"

    # defining the manager for the UserAccount model
    objects = UserAccountManager()

    def __str__(self):
        return str(self.first_name)

    def save(self, *args, **kwargs):
        if not self.type or self.type is None:
            self.type = UserAccount.Types.PEOPLE
            self.is_people=True
        return super().save(*args, **kwargs)


class PeopleManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, contact, password):

        if contact is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')
        user = self.model(
            contact=contact,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.PEOPLE)
        return queryset


class People(UserAccount):
    class Meta:
        proxy = True

    objects = PeopleManager()

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.PEOPLE
        self.is_people = True
        super().save(*args, **kwargs)
        self.groups.add(Group.objects.get(name='People'))


class AssemblyManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, username, contact, password):
        if contact is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')
        user = self.model(
            contact=contact
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=UserAccount.Types.ASSEMBLY)

        return queryset


class Assembly(UserAccount):
    class Meta:
        proxy = True

    objects = AssemblyManager()

    def __str__(self):
        return str(self.institution)

    def save(self, *args, **kwargs):
        self.type = UserAccount.Types.ASSEMBLY
        self.is_assembly = True
        super().save(*args, **kwargs)
        self.groups.add(Group.objects.get(name='assembly'))
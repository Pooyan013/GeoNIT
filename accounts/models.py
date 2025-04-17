from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_jalali.db import models as jmodels

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('کاربر باید ایمیل داشته باشد')
        if not username:
            raise ValueError('کاربر باید نام کاربری داشته باشد')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Added phone_number field
    uni_name = models.CharField(max_length=100, blank=True, null=True)
    facility_name = models.CharField(max_length=100, blank=True, null=True)
    date_joined = jmodels.jDateTimeField(auto_now_add=True)
    last_login = jmodels.jDateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

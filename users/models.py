from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models



#--------------------------------------------------------------------------------------------------- Person model
class Users( AbstractBaseUser, PermissionsMixin ):
    username = models.CharField(
        blank = False,
        null = False,
        unique = True,
        max_length = 32,
        editable = True,
        db_column = 'txt_username'
    )
    email = models.EmailField(
        blank = False,
        null = False,
        unique = True,
        max_length = 256,
        editable = True,
        db_column = 'txt_email'
    )
    telephone_number = models.CharField(
        blank = True,
        null = False,
        unique = False,
        max_length = 16,
        editable = True,
        db_column = 'txt_telephone_number'
    )
    extension = models.CharField(
        blank = True,
        null = False,
        unique = False,
        max_length = 8,
        editable = True,
        db_column = 'txt_extension'
    )
    profile_image = models.BinaryField(
        blank = True,
        null = True,
        unique = False,
        editable = True,
        default = None,
        db_column = 'bin_image'
    )
    profile_image_name = models.CharField(
        blank = True,
        null = True,
        unique = False,
        max_length = 256,
        editable = True,
        default = None,
        db_column = 'txt_image'
    )
    is_deleted = models.BooleanField(
        blank = False,
        null = False,
        unique = False,
        editable = True,
        default = False,
        db_column = 'bool_is_deleted'
    )
    datetime = models.DateTimeField(
        blank = False,
        null = False,
        unique = False,
        editable = False,
        auto_now_add = True,
        db_column = 'datetime'
    )
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    class Meta:
        db_table = 'data_users'
        managed = True

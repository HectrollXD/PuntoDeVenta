from django.utils.text import slugify
from django.utils import timezone
from locals.models import Locals
from users.models import Users
from django.db import models



#--------------------------------------------------------------------------------------------------- Person model
class Employes( models.Model ):
    employe_id = models.SlugField(
        blank = False,
        null = False,
        max_length = 20,
        editable = True,
        unique = True,
        db_column = 'txt_employe'
    )
    name = models.CharField(
        blank = False,
        null = False,
        max_length = 128,
        editable = True,
        unique = False,
        default = '',
        db_column = 'txt_name'
    )
    first_lastname = models.CharField(
        blank = False,
        null = False,
        max_length = 128,
        editable = True,
        unique = False,
        default = '',
        db_column = 'txt_first_lastname'
    )
    second_lastname = models.CharField(
        blank = False,
        null = False,
        max_length = 128,
        editable = True,
        unique = False,
        default = '',
        db_column = 'txt_second_lastname'
    )
    is_active = models.BooleanField(
        blank = False,
        null = False,
        editable = True,
        unique = False,
        default = True,
        db_column = 'bool_is_active'
    )
    is_deleted = models.BooleanField(
        blank = False,
        null = False,
        editable = True,
        unique = False,
        default = False,
        db_column = 'bool_is_deleted'
    )
    register_date = models.DateField(
        blank = False,
        null = False,
        editable = False,
        unique = False,
        default = timezone.now,
        db_column = 'dte_register_date'
    )
    datetime = models.DateTimeField(
        blank = False,
        null = False,
        editable = False,
        unique = False,
        default = timezone.now,
        db_column = 'datetime'
    )
    user = models.OneToOneField(
        to = Users,
        on_delete = models.DO_NOTHING,
        blank = False,
        null = False
    )
    local = models.ForeignKey(
        to = Locals,
        on_delete = models.DO_NOTHING,
        blank = False,
        null = False,
        db_column = 'int_local_id',
        related_name = 'local_employe'
    )

    class Meta:
        db_table = 'data_employes'
        managed = True
        pass

    def __str__(self):
        return '%s %s %s' % (
            self.first_lastname.title(),
            self.second_lastname.title(),
            self.name.title()
        )

    def save(self, *args, **kwargs):
        employe_id = '%s%s%s%s' % (
            self.first_lastname[0:2],
            ('X' if self.second_lastname == '' else self.second_lastname[0:1]),
            self.name[0:1],
            self.register_date.strftime('%d%m%y')
        )
        self.employe_id = slugify(employe_id).upper()
        self.name = self.name.upper()
        self.first_lastname = self.first_lastname.upper()
        self.second_lastname = self.second_lastname.upper()
        super(Employes, self).save(*args, **kwargs)
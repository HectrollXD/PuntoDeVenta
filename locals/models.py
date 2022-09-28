from django.db import models
from django.utils.text import slugify


#--------------------------------------------------------------------------------------------------- Locals Model
class Locals( models.Model ):
    local_alias = models.SlugField(
        null = False,
        blank = False,
        max_length = 136,
        db_column = 'txt_alias'
    )
    local_name = models.CharField(
        null = False,
        blank = False,
        max_length = 128,
        db_column = 'txt_local_name'
    )
    street = models.CharField(
        null = False,
        blank = False,
        max_length = 128,
        db_column = 'txt_street'
    )
    number = models.CharField(
        null = False,
        blank = False,
        max_length = 16,
        db_column = 'txt_number'
    )
    postal_code = models.CharField(
        null = False,
        blank = False,
        max_length = 8,
        db_column = 'txt_postal_code'
    )
    city = models.CharField(
        null = False,
        blank = False,
        max_length = 64,
        db_column = 'txt_city'
    )
    state = models.CharField(
        null = False,
        blank = False,
        max_length = 64,
        db_column = 'txt_state'
    )

    class Meta:
        db_table = 'catalog_locals'
        managed = True

    def __str__(self):
        return self.local_name

    def save(self, *args, **kwargs):
        alias = '%s %s' % (self.postal_code, self.local_name)
        self.local_alias = slugify(alias)
        self.local_name = self.local_name.upper()
        self.street = self.street.upper()
        self.city = self.city.upper()
        self.state = self.state.upper()
        super(Locals, self).save(*args, **kwargs)
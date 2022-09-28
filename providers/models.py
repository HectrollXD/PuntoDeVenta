from django.utils.text import slugify
from django.db import models



#--------------------------------------------------------------------------------------------------- Providers
class Providers( models.Model ):
    provider_alias = models.SlugField(
        blank = False,
        null = False,
        max_length = 128,
        unique = True,
        db_column = 'txt_provider_alias'
    )
    provider_name = models.CharField(
        blank = False,
        null = False,
        max_length = 128,
        unique = True,
        db_column = 'txt_provider_name'
    )

    class Meta:
        db_table = 'catalog_providers'
        managed = True

    def save(self, *args, **kwargs):
        self.provider_alias = slugify(self.provider_name)
        self.provider_name = self.provider_name.upper()
        super(Providers, self).save(*args, **kwargs)

    def __str__(self):
        return self.provider_name

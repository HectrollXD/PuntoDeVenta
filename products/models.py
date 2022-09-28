from providers.models import Providers
from category.models import Categories
from django.utils.text import slugify
from django.db import models



#--------------------------------------------------------------------------------------------------- Products
class Products( models.Model ):
    product_alias = models.SlugField(
        blank = False,
        null = False,
        unique = True,
        max_length = 64,
        db_column = 'txt_product_alias'
    )
    product_code = models.CharField(
        blank = False,
        null = False,
        unique = True,
        max_length = 16,
        db_column = 'txt_code'
    )
    product_name = models.CharField(
        blank = False,
        null = False,
        max_length = 64,
        db_column = 'txt_name'
    )
    product_description = models.CharField(
        blank = True,
        null = True,
        max_length = 256,
        db_column = 'txt_description'
    )
    deseable_stock = models.IntegerField(
        blank = False,
        null = False,
        default = 32,
        db_column = 'int_deseable_stock'
    )
    stock = models.IntegerField(
        blank = False,
        null = False,
        default = 0,
        db_column = 'int_stock'
    )
    category = models.ForeignKey(
        to = Categories,
        on_delete = models.DO_NOTHING,
        blank = False,
        null = False,
        db_column = 'int_category_id',
        related_name = 'product_category'
    )
    provider = models.ForeignKey(
        to = Providers,
        on_delete = models.DO_NOTHING,
        blank = False,
        null = False,
        db_column = 'int_provider_id',
        related_name = 'product_provider'
    )

    class Meta:
        db_table = 'catalog_products'
        managed = True

    def save(self, *args, **kwargs):
        self.product_alias = slugify(self.product_name)
        self.product_name = self.product_name.upper()
        self.product_description = self.product_description.upper()
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name
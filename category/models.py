from django.utils.text import slugify
from django.db import models



#--------------------------------------------------------------------------------------------------- Categories
class Categories( models.Model ):
    category_alias = models.SlugField(
        blank = False,
        null = False,
        max_length = 64,
        unique = True,
        db_column = 'txt_category_alias'
    )
    category_name = models.CharField(
        blank = False,
        null = False,
        max_length = 64,
        unique = True,
        db_column = 'txt_category_name'
    )

    class Meta:
        db_table = 'catalog_categories'
        managed = True

    def save(self, *args, **kwargs):
        self.category_alias = slugify(self.category_name)
        self.category_name = self.category_name.upper()
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

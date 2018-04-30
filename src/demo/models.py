"""
DJANGO MATERIAL WIDGETS DEMO MODELS
demo/models.py
"""
# pylint: disable=too-few-public-methods
from django.db import models

class MaterialWidgetsForeignKeyDemoModel(models.Model):
    """Secondary demo model for ForeignKey."""
    item = models.IntegerField()

    class Meta:
        """Meta settings for MaterialWidgetsDemoModel"""
        app_label = 'demo'


class MaterialWidgetsManyToManyDemoModel(models.Model):
    """Secondary demo model for ManyToManyField."""
    item = models.IntegerField()

    class Meta:
        """Meta settings for MaterialWidgetsDemoModel"""
        app_label = 'demo'


class MaterialWidgetsDemoModel(models.Model):
    """Demo model containing all model fields with representative form fields.
    https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#field-types
    """
    big_integer_field = models.BigIntegerField(null=True, blank=True)
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=32, null=True, blank=True)
    date_field = models.DateField(null=True, blank=True)
    date_time_field = models.DateTimeField(null=True, blank=True)
    decimal_field = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        )
    email_field = models.EmailField(null=True, blank=True)
    file_field = models.FileField(blank=True)
    file_path_field = models.FilePathField(path='/demo/images', blank=True)
    float_field = models.FloatField(null=True, blank=True)
    foreign_key = models.ForeignKey(
        MaterialWidgetsForeignKeyDemoModel,
        models.CASCADE,
        null=True,
        blank=True,
        )
    #image_field = models.ImageField(blank=True) ### pillow required
    integer_field = models.IntegerField(null=True, blank=True)
    generic_ip_address_field = models.GenericIPAddressField(null=True, blank=True)
    many_to_many_field = models.ManyToManyField(
        MaterialWidgetsManyToManyDemoModel,
        blank=True,
        )
    null_boolean_field = models.NullBooleanField()
    positive_integer_field = models.PositiveIntegerField(null=True, blank=True)
    positive_small_integer_field = models.PositiveSmallIntegerField(null=True, blank=True)
    slug_field = models.SlugField(null=True, blank=True)
    small_integer_field = models.SmallIntegerField(null=True, blank=True)
    text_field = models.TextField(null=True, blank=True)
    time_field = models.TimeField(null=True, blank=True)
    url_field = models.URLField(null=True, blank=True)

    class Meta:
        """Meta settings for MaterialWidgetsDemoModel"""
        app_label = 'demo'

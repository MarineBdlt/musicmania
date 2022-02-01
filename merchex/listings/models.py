from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    image = models.ImageField()

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)


class Listing(models.Model):
    def __str__(self):
        return f"{self.title}"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=2000)
    year = models.fields.DateField(null=True)
    sold = models.fields.BooleanField(default=True)
    image = models.ImageField(upload_to="assets/img/")

    class Type(models.TextChoices):
        RECORDS = "RC"
        CLOTHING = "CT"
        POSTERS = "PS"
        MISCELLANEOUS = "MC"

    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

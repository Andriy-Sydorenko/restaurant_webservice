from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Dish Type"
        verbose_name_plural = "Dish Types"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("restaurant:dish-type-detail", args=[str(self.id)])


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cook-detail", args=[str(self.id)])


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.CASCADE,
                                  related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self) -> str:
        return (f"{self.name} (price: "
                f"{self.price}, type: {self.dish_type.name})")

    def get_absolute_url(self):
        return reverse("restaurant:dish-detail", args=[str(self.id)])

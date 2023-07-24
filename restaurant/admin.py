from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import DishType, Dish, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type", "price", "cooks"]
    search_fields = ["price",
                     "name",
                     "cooks__first_name",
                     "cooks__last_name",
                     "cooks_username"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (("Additional info",
                                        {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info",
         {"fields": ("first_name", "last_name", "years_of_experience")}),
    )
    search_fields = ["username",
                     "first_name",
                     "last_name",
                     "years_of_experience"]


admin.site.register(DishType)

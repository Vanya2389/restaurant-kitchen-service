from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from kitchen.models import DishType, Dish, Cook


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ("dish_type",)
    search_fields = ("name",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

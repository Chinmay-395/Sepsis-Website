from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    fields = ["email",
              "name",
              "user_type",
              "photo"]

    list_filter = (
        'user_type',
    )

    list_display = ["email",
                    "name",
                    "user_type", "id", "photo"]


admin.site.register(UserProfile, UserProfileAdmin)

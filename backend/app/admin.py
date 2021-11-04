from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Jobs)


class AccountUserAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False


# Register your models here.
admin.site.register(User)
admin.site.register(Intern)
admin.site.register(Sponsor)
admin.site.register(Stack)
""" admin.site.register(User, AccountUserAdmin)
admin.site.register(Intern, AccountUserAdmin)
admin.site.register(Sponsor, AccountUserAdmin)
admin.site.register(Stack, AccountUserAdmin) """


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ["year", "male", "female", "finalist", "participant"]

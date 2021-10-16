from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Jobs)


# Register your models here.
admin.site.register(User)
admin.site.register(Intern)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['year','male','female','finalist','participant']

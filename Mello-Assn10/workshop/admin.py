from django.contrib import admin
from registration.models import Workshop


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'session', 'room', 'start', 'end')
    search_fields = ('title', 'session', 'room', 'start', 'end')
    list_filter = ('title', 'session', 'room', 'start', 'end')

admin.site.register(Workshop, WorkshopAdmin)

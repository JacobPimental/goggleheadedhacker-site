from django.contrib import admin
from .models import Resume, Section, Contact_Info

# Register your models here.
admin.site.register(Resume)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('header',)

admin.site.register(Section, SectionAdmin)

class Contact_InfoAdmin(admin.ModelAdmin):
    list_display = ('method',)

admin.site.register(Contact_Info, Contact_InfoAdmin)

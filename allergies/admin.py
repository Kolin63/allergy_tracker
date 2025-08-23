from django.contrib import admin
from .models import Allergy

# Register your models here.

class AllergyAdmin(admin.ModelAdmin):
    list_display = ("allergyname", "test_level")
admin.site.register(Allergy, AllergyAdmin)

from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working')
    list_editable=('working',)
    search_fields=('name',)

admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)
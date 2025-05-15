# admin.py

from django.contrib import admin
from .models import Service, HeroImage, Testimonial, Subscriber, Product

from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Consultation
from .models import Equipment

from .models import Job, Application

from .models import CropSolution

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_bestseller')
    search_fields = ('name', 'category')
    list_filter = ('category', 'is_bestseller')

# Optionally, you can define how the fields are displayed in the form
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price', 'short_description', 'image', 'is_bestseller')
        }),
    )

@admin.register(CropSolution)
class CropSolutionAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'is_featured')

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Equipment)

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'location', 'created_at')
    search_fields = ('name', 'email', 'phone', 'location')
    list_filter = ('created_at',)

class EcoHopeAdmin(ModelAdmin):
    list_per_page = 25
    save_on_top = True
    date_hierarchy = 'created_at'
    
    class Media:
        css = {
            'all': ('admin/css/admin.css',)
        }

admin.site.register(HeroImage)
admin.site.register(Testimonial)
admin.site.register(Subscriber)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


from .models import TeamMember
admin.site.register(TeamMember)

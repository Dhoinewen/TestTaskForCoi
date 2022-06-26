from django.contrib import admin

from .models import Doctor, Category


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'work_experience', 'get_cat')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'birthday')
    list_filter = ('work_experience', 'cat')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_doctors')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Category, CategoryAdmin)

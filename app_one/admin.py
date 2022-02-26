from django.contrib import admin
from app_one.models import Contact,Add_BlogModel
# Register your models here.
admin.site.register(Contact)

@admin.register(Add_BlogModel)
class Add_blog(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'tags', 'image' ]

from django.contrib import admin
from .models import Blog, ContactMe

# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email","message")
    # fields = ( 'subcategory', 'tags')
    list_filter = ("fullname",)
    search_fields = ["fullname", "email"]

admin.site.register(ContactMe, ContactAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_post", "admin_name","message_number")
    # fields = ( 'subcategory', 'tags')
    list_filter = ("admin_name",)
    search_fields = ["admin_name", "blog_post"]
    # prepopulated_fields = {"slug": ("fullname",)}
admin.site.register(Blog, BlogAdmin)

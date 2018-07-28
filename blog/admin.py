from django.contrib import admin
from .models import Post, Tag, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','views','hash_value',)

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)

admin.site.register(Tag, TagAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)

admin.site.register(Category, CategoryAdmin)

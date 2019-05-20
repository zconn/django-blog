from django.contrib import admin
from blogging.models import Post, Category

#admin.site.register(Post)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ("title", "text", "author", "published_date")
    inlines = [CategoryInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)

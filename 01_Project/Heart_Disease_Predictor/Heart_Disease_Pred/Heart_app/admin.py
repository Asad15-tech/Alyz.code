from django.contrib import admin
from .models import BlogPost, AboutPage

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted', 'author')
    date_hierarchy = 'date_posted'

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')
    def has_add_permission(self, request):
        # Check if there's already an About page
        return not AboutPage.objects.exists()

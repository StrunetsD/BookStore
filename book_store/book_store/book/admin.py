from django.contrib import admin
from .models import Author, Category, Book, Review

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'biography_short')
    search_fields = ('name',)

    def biography_short(self, obj):
        return obj.biography[:50] + '...' if len(obj.biography) > 50 else obj.biography
    biography_short.short_description = 'Biography Preview'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author_name', 'category', 'publishing_house')
    list_filter = ('category', 'publishing_house')
    search_fields = ('title', 'author_name__name')


    def author_name(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    author_name.short_description = 'Authors'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('book', 'rating')
    search_fields = ('user__username', 'book__title')



admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
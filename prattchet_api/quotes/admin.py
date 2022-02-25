from django.contrib import admin

from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'quote',
        'heroes_of_the_excerpt',
        'book',
        'book_author',
    )
    list_filter = ('book',)


admin.site.register(Quote, QuoteAdmin)

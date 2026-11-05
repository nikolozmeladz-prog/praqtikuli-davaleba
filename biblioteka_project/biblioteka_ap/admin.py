from django.contrib import admin
from .models import books, autor, categories, Reader

admin.site.register(books)
admin.site.register(autor)
admin.site.register(categories)
admin.site.register(Reader)
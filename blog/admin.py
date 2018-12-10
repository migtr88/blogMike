from django.contrib import admin

from .models import Post,Comments, Autor, Category


# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Autor)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]


admin.site.register(Category,CategoryAdmin)
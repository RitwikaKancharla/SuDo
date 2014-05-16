from django.contrib import admin
from my_first_app.myapp.models import Author

class User(admin.ModelAdmin):
    pass
admin.site.register(Author, User)

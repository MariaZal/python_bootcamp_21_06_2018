from django.contrib import admin
from example.models import Example

# Register your models here.

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass



admin.register(Example,ExampleAdmin)
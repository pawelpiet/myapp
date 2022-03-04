from django.contrib import admin

# Register your models here.


from .models import Region, Test, Land, Race


admin.site.register(Region)
admin.site.register(Test)
admin.site.register(Land)
admin.site.register(Race)
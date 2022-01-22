from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Ideologist)
admin.site.register(Builder)
admin.site.register(Technology)
admin.site.register(TechnologyBuilder)
admin.site.register(Match)
admin.site.register(Project)
admin.site.register(User)
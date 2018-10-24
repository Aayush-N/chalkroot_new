from django.contrib import admin
from .models import *

admin.site.site_header = 'School Aggregator Administration'

admin.site.register(UserType)
admin.site.register(User)
admin.site.register(School)
admin.site.register(Reviews)
admin.site.register(Board)
admin.site.register(Category)
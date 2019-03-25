from django.contrib import admin
from .models import Order,Comment,Profile,Counter

admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Counter)


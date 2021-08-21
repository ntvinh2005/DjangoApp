from django.contrib import admin
from .models import Note, Item, Date,Topic
# Register your models here.
admin.site.register(Note)
admin.site.register(Item)
admin.site.register(Date)
admin.site.register(Topic)
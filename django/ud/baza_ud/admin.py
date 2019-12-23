from django.contrib import admin
from .models import Staff, Position, Place, Artist, Concert, Ad,Ad_Agency,Ad_Type


admin.site.register(Staff)
admin.site.register(Position)
admin.site.register(Place)
admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Ad)
admin.site.register(Ad_Agency)
admin.site.register(Ad_Type)
from django.contrib import admin

# Register your models here.
from .models import Personal, Califications,Chamba,Category,Document,Skill,Task, Location
# Register your models here.

admin.site.register(Personal)
admin.site.register(Califications)
admin.site.register(Chamba)
admin.site.register(Category)
admin.site.register(Document)
admin.site.register(Skill)
admin.site.register(Task)
admin.site.register(Location)
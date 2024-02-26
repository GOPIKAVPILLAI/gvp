from django.contrib import admin
from .models import fff
from .models import Member
from .models import msg
# Register your models here.

admin.site.register(Member)
admin.site.register(msg)
admin.site.register(fff)

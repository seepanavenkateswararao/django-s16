from django.contrib import admin

from .models import Status, PresentLocation, BasicDetails, MoneyTransfer
from .models import User

admin.site.register(User)
admin.site.register(BasicDetails)
admin.site.register(PresentLocation)
admin.site.register(Status)
admin.site.register(MoneyTransfer)

# Register your models here.

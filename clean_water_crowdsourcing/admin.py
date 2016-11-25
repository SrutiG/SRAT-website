from django.contrib import admin
from .models import Account
from .models import WaterPurityReport
from .models import WaterSourceReport

admin.site.register(Account)
admin.site.register(WaterPurityReport)
admin.site.register(WaterSourceReport)
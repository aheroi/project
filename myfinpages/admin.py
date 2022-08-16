from django.contrib import admin
from myfinpages.models import Income, Outcome, Balance

# Register your models here.
admin.site.register(Income)
admin.site.register(Outcome)
admin.site.register(Balance)

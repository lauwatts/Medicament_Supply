from django.contrib import admin
from .models import *

admin.site.register(Medicament)
admin.site.register(Bill)
admin.site.register(MedicamentBill)

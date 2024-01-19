from django.contrib import admin

from home.models import HowKnowAboutClinic, Patient, DentalPlan, Product, Transaction, Expense, Supplier

# Register your models here.
admin.site.register(HowKnowAboutClinic)
admin.site.register(Patient)
admin.site.register(DentalPlan)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Expense)
admin.site.register(Supplier)

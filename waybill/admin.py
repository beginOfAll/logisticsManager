from django.contrib import admin
from .models import Waybill, Customer


class WaybillAdmin(admin.ModelAdmin):
	list_display = ('waybill_number', 'create_time', 'user')
	list_filter = ['create_time', 'user']
	search_fields = ['waybill_number']


class ConsumerAdmin(admin.ModelAdmin):
	list_display = ('user', 'real_name')
	search_fields = ['real_name']


admin.site.register(Waybill, WaybillAdmin)
admin.site.register(Customer, ConsumerAdmin)

#coding=utf-8

from django.contrib import admin
from record.models import Record


class RecordAdmin(admin.ModelAdmin):

#    list_filter = ('flight_no','arrive_airport', 'arrive')
    list_display = ('name','arrive','flight_company','flight_no','arrive_airport','qq','email','phone','package','need_room','expect_district','incharge')
    search_fields = ['name','flight_company','flight_no']
    date_hierarchy = 'arrive'
#    list_editable=('price','amount')
'''
    fieldsets=(
        (None,{
            'fields':('title','price','amount','for_sale','active')
            }),#        ('More options',{
            'classes':('collapse',),
            'fields':('description','pic','year','singer',
                      'genre','company','isbn','is_digital','store')
            }),

        )
'''
admin.site.register(Record,RecordAdmin)

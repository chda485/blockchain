from django.contrib import admin
from .models import Transaction
from django.urls import reverse_lazy
from django.utils.html import format_html

class TransactionAdmin(admin.ModelAdmin):
     
    def add_descr(self, obj):
        url = reverse_lazy('add_descr', kwargs={'id_t':obj.pk})
        return format_html("<a href={}>{}</a>", url, "Добавить описание")
        
    def view_description(self, obj):
        url = reverse_lazy('decr', kwargs={'id_t':obj.pk})
        D = obj.description[:10] + "..." if obj.description is not None else "..."
        return format_html("<a href={}>{}</a>", url, D)
    
    view_description.short_description = "Описание"
    add_descr.short_description = "Добавить описание"
    
    list_display=('id_transaction', 'data_transaction', 'view_description', 'add_descr')
    fields=('id_transaction',)
    
#admin.site.register(Transaction)
admin.site.register(Transaction, TransactionAdmin)
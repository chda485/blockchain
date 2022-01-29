from django.db import models

class Transaction(models.Model):
    id_transaction = models.TextField(db_index=True, verbose_name="Id транзакции")
    data_transaction = models.DateField(auto_now_add=True, verbose_name="Дата совершения транзакции")
    description = models.TextField(null=True, blank=True, verbose_name="Описание транзакции")
    
    def __str__(self):
        return self.id_transaction
    
    class Meta:
        ordering = ['id_transaction', '-data_transaction']
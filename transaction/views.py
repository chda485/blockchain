from django.shortcuts import render
from .models import Transaction
from .utils import make_transaction
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect

def list_transaction(request):
    if request.method == 'POST':
        t = Transaction()
        id_ = make_transaction()
        t.id_transaction = id_
        t.save()
        transactions = Transaction.objects.values_list('id_transaction')
        
    elif request.method == 'GET':
        transactions = Transaction.objects.values_list('id_transaction')
        
    if len(transactions) == 0:
        null_list = True
        transactions = []
    else:
        null_list = False
        transactions = [t[0] for t in transactions]
    context = {'transactions': transactions, 'null_list': null_list}
    return render(request, 'list_transaction.html', context=context)

def description(request, id_t):
    transaction = Transaction.objects.get(pk=id_t)
    context = {"t": transaction}
    return render(request, 'description.html', context=context)

def add_descr(request, id_t):   
    if request.method == 'POST':
        transaction = Transaction.objects.get(pk=id_t)
        D = request.POST.get('descr')
        transaction.description = D
        transaction.save()
        context = {"t": transaction}
        return render(request, 'description.html', context=context) 
    
    elif request.method == 'GET':
        context = {"id_": id_t}
        return render(request, 'add_descr.html', context=context)
    
      
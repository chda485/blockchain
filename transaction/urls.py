from django.urls import path
from . import views

#<int:cat_id>/
urlpatterns = [
    path('', views.list_transaction, name='list'),
    path('tx/tx<int:id_t>/', views.description, name='decr'),
    path('<int:id_t>/edit_descr/', views.add_descr, name='add_descr'),
]

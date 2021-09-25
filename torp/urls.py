from django.urls import path
from . import views


urlpatterns = [
    path('', views.torp, name='torp'),
    path('inventory/', views.inventory, name="inventory"),
    path('queuing/', views.queuing, name="queuing"),
    path('linprog/', views.linprog, name='linprog'),
    path('linprog/results/', views.get_linprog_results, name='linprog_results'),
    path('inventory/results/', views.get_inv_results, name="inv_results"),
    path('queuing/results/', views.get_queue_results, name="que_results"),
]

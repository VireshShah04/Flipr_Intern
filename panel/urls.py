from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_a_customer/', views.add_a_customer, name='add_a_customer'),
    path('purchase_order/', views.purchase_order, name='purchase_order'),
    path('shipping_details/', views.shipping_details, name='shipping_details'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dasboard'),
    path('purchase_order_dashboard/', views.purchase_order, name='purchase_order_dashboard'),
    path('shipping_details_dashboard', views.shippig_details_dashboard, name='shipping_details_dashboard')
]

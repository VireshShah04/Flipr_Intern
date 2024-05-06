from django.shortcuts import render, redirect
from .models import Customer, PurchaseOrder, ShippingDetail
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def add_a_customer(request):
    print(request.POST)
    if request.method == 'POST':
        customer_name = request.POST.get('customerName')
        customer_email = request.POST.get('email')
        customer_mobile_number = request.POST.get('mobileno')
        customer_city = request.POST.get('city')
        
        # Create a new customer object and save it to the database
        customer = Customer(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_mobile_number=customer_mobile_number,
            customer_city=customer_city
        )
        customer.save()
        return redirect('panel:index')
        
    return render(request, 'add_a_customer.html')


@login_required
def purchase_order(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('pricing')
        mrp = request.POST.get('mrp')
        customer_id = request.POST.get('customer_id')  # Assuming customer_id is provided in the form

        # Retrieve the customer object based on the provided customer_id
        customer = Customer.objects.get(customer_id=customer_id)

        # Create a new purchase order object and save it to the database
        purchase = PurchaseOrder(
            product_name=product_name,
            quantity=quantity,
            pricing=price,
            mrp=mrp,
            customer_id=customer
        )
        purchase.save()
        return redirect('panel:index')
    return render(request, 'purchase_order.html')


@login_required
def shipping_details(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        purchase_id = request.POST.get('purchase_id')
        customer_id = request.POST.get('customer_id')

        # Retrieve the customer and purchase order object
        customer = Customer.objects.get(customer_id=customer_id)
        purchase_order = PurchaseOrder.objects.get(purchase_order_id=purchase_id)

        # Create a new shipping detail object and save it to the database
        shipping = ShippingDetail(
            address = address,
            city = city,
            pincode = pincode,
            purchase_order = purchase_order,
            customer = customer
        )
        shipping.save()
        return redirect('panel:index')
    return render(request, 'shipping_details.html')


@login_required
def customer_dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

@login_required
def purchase_order(request):
    purchase_order = PurchaseOrder.objects.all()
    return render(request, 'purchase_order_dashboard.html', {'purchase_orders' : purchase_order})


@login_required
def shippig_details_dashboard(request):
    shipping_details = ShippingDetail.objects.all()
    return render(request, 'shipping_details_dashboard.html', {'shipping_details' : shipping_details})
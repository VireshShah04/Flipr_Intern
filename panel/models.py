from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True, editable=False)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_mobile_number = models.CharField(max_length=15)
    customer_city = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Generate customer_id if it's not provided
        if not self.customer_id:
            self.customer_id = self.generate_customer_id()
        super().save(*args, **kwargs)

    def generate_customer_id(self):
        last_customer = Customer.objects.order_by('-id').first()
        if last_customer:
            last_id = int(last_customer.customer_id.split('-')[-1])
            new_id = last_id + 1
        else:
            new_id = 1
        return f"CID-{new_id}"

    def __str__(self):
        return self.customer_name
    

class PurchaseOrder(models.Model):
    purchase_order_id = models.CharField(max_length=20, unique=True, editable=False)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    pricing = models.IntegerField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Generate purchase_order_id if it's not provided
        if not self.purchase_order_id:
            self.purchase_order_id = self.generate_purchase_order_id()
        super().save(*args, **kwargs)

    def generate_purchase_order_id(self):
        last_purchase_order = PurchaseOrder.objects.order_by('-id').first()
        if last_purchase_order:
            last_id = int(last_purchase_order.purchase_order_id.split('-')[-1])
            new_id = last_id + 1
        else:
            new_id = 1
        return f"PO-{new_id}"

    def __str__(self):
        return f"Purchase Order #{self.purchase_order_id}"
    

class ShippingDetail(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shipping Detail for Order #{self.purchase_order_id} ({self.customer.customer_name})"
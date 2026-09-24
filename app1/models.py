from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
import os
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone
from .utils import apply_rating, send_async_login_email
from .utils import send_async_order_email
from django.utils.html import strip_tags
import threading
import traceback
import random
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/',null=True,blank=True,default='default.jpg')
    mobile = models.CharField(max_length=15, blank=True, null=True)
    delivery_address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.user.username
class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=100)
    def __str__(self):
        return self.categoryname
class Productview(models.Model):
    productviewid = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    productimage1 = models.URLField(blank=True, null=True)
    productimage2 = models.URLField(blank=True, null=True)
    productimage3 = models.URLField(blank=True, null=True)
    productimage4 = models.URLField(blank=True, null=True)
    productimage5 = models.URLField(blank=True, null=True)
    productimage6 = models.URLField(blank=True, null=True)
    productimage7 = models.URLField(blank=True, null=True)
    productimage8 = models.URLField(blank=True, null=True)
    productimage9 = models.URLField(blank=True, null=True)
    productimage10 = models.URLField(blank=True, null=True)
    productname = models.CharField(max_length=100)
    producttitle = models.TextField()
    productprice = models.BigIntegerField()
    productmrpprice = models.IntegerField()
    productprice1 = models.BigIntegerField(blank=True, null=True)
    productmrpprice1 = models.IntegerField(blank=True, null=True)
    productprice2 = models.BigIntegerField(blank=True, null=True)
    productmrpprice2 = models.IntegerField(blank=True, null=True)
    productprice3 = models.BigIntegerField(blank=True, null=True)
    productmrpprice3 = models.IntegerField(blank=True, null=True)
    productdiscountrate = models.CharField(max_length=255, blank=True, null=True)
    productsize = models.CharField(max_length=100)
    productsize1 = models.CharField(max_length=100)
    productsize2 = models.CharField(max_length=100)
    productsize3 = models.CharField(max_length=100)
    productcolor1 = models.CharField(max_length=20, blank=True, null=True)
    productcolor2 = models.CharField(max_length=20, blank=True, null=True)
    productcolor3 = models.CharField(max_length=20, blank=True, null=True)
    productcolor4 = models.CharField(max_length=20, blank=True, null=True)
    productcolor5 = models.CharField(max_length=20, blank=True, null=True)
    productrating = models.DecimalField(max_digits=2,decimal_places=1,default=4.0)
    producttophighlights1 = models.CharField(max_length=400)
    producttophighlights2 = models.CharField(max_length=400)
    producttophighlights3 = models.CharField(max_length=400)
    producttophighlights4 = models.CharField(max_length=400)
    producttophighlights5 = models.CharField(max_length=400)
    producttophighlights6 = models.CharField(max_length=400)
    productaboutitem1 = models.CharField(max_length=400)
    productaboutitem2 = models.CharField(max_length=400)
    productaboutitem3 = models.CharField(max_length=400)
    productaboutitem4 = models.CharField(max_length=400)
    productaboutitem5 = models.CharField(max_length=400)
    productitemdetail1 = models.CharField(max_length=400)
    productitemdetail2 = models.CharField(max_length=400)
    productitemdetail3 = models.CharField(max_length=400)
    productitemdetail4 = models.CharField(max_length=400)
    stock = models.PositiveIntegerField(default=5)
    sold_count = models.PositiveIntegerField(default=0)
    low_stock_alert = models.PositiveIntegerField(default=5)
    in_stock = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        self.in_stock = self.stock > 0
        super().save(*args, **kwargs)
    def get_main_image(self):
        images = [self.productimage1,]
        for img in images:
            if img:
                return img
        return "/static/IMAGES/default.png"
    @property
    def get_sizes(self):
        sizes = [self.productsize, self.productsize1, self.productsize2, self.productsize3]
        return [s.strip() for s in sizes if s and s.strip() and '85' not in str(s) and str(s).lower() != 'none']
    def __str__(self):
        return self.producttitle
class ProductViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('user', 'product')
class ProductColor(models.Model):
    product = models.ForeignKey(Productview,on_delete=models.CASCADE,related_name="colors")
    color_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=20)
    image = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.product.productname} - {self.color_name}"
class ProductVariant(models.Model):
    product = models.ForeignKey(Productview,on_delete=models.CASCADE,related_name="variants")
    color = models.CharField(max_length=30)
    color_code = models.CharField(max_length=20)
    image = models.URLField()
    def __str__(self):
        return f"{self.product.productname} - {self.color}"
class Review(models.Model):
    reviewid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.user.username
    @property
    def delivered_date(self):
        order_item = Orderitem.objects.filter(order_id__user_id=self.user,productview_id=self.product,order_id__orderstatus='Delivered').order_by('-order_id__delivered_at').first()
        if order_item and order_item.order_id.delivered_at:
            return order_item.order_id.delivered_at
        return None
class Cart(models.Model):
    cartid = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Productview, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    selected_size = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.userid.username
    def get_unit_price(self):
        product = self.product_id
        if self.selected_size:
            size_clean = self.selected_size.strip().lower()
            if product.productsize and product.productsize.strip().lower() == size_clean:
                return product.productprice
            elif product.productsize1 and product.productsize1.strip().lower() == size_clean:
                return product.productprice1 if product.productprice1 is not None else product.productprice
            elif product.productsize2 and product.productsize2.strip().lower() == size_clean:
                return product.productprice2 if product.productprice2 is not None else product.productprice
            elif product.productsize3 and product.productsize3.strip().lower() == size_clean:
                return product.productprice3 if product.productprice3 is not None else product.productprice
        return product.productprice
    def subtotal(self):
        return self.get_unit_price() * self.quantity
class SearchHistory(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)
    search_count = models.PositiveIntegerField(default=1) 
    class Meta:
        ordering = ['-searched_at']
    def __str__(self):
        return self.keyword
class Otracker(models.Model):
    otrackerid = models.AutoField(primary_key=True)
    myuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.myuser.username} - {self.status}"
class Coupon(models.Model):
    couponid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    discount = models.PositiveIntegerField(help_text="Discount Percentage")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    minimum_amount = models.PositiveIntegerField(default=0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.code
    def is_valid(self):
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to
    @property
    def productimage1(self):
        if self.category:
            product_view = Productview.objects.filter(category_id=self.category).first()
            if product_view:
                return product_view.productimage1
        return None
class Order(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ('Out for Delivery', 'Out for Delivery'),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )
    orderstatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    paymentstatus = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    cancelled_at = models.DateTimeField(null=True, blank=True)
    orderid = models.AutoField(primary_key=True)
    otracker_id = models.ForeignKey('Otracker', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    username = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    subtotal = models.IntegerField()
    deliverycharges = models.IntegerField()
    total = models.IntegerField()
    paymentmethod = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    processing_at = models.DateTimeField(null=True, blank=True)
    coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, null=True, blank=True)
    coupon_discount = models.IntegerField(default=0)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    user_order_seq = models.IntegerField(editable=False, null=True, blank=True)
    amazon_order_id = models.CharField(max_length=20, blank=True, null=True)
    stock_updated = models.BooleanField(default=False)
    def __str__(self):
        return self.user_id.username
    @property
    def status_step(self):
        mapping = {
            'Pending': 1,
            'Ordered': 1,
            'Paid': 2,
            'Confirmed': 2,
            'Processing': 3,
            'Shipped': 4,
            'Out for Delivery': 5,
            'Delivered': 6,
            'Cancelled': 0,
        }
        return mapping.get(self.orderstatus, 1)
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            if self.user_id:
                user_orders_count = Order.objects.filter(user_id=self.user_id).count()
                self.user_order_seq = user_orders_count + 1
            else:
                self.user_order_seq = 1   
        old_orderstatus = None
        if not is_new:
            try:
                original = Order.objects.get(pk=self.pk)
                old_orderstatus = original.orderstatus
            except Order.DoesNotExist:
                pass
        if not is_new and old_orderstatus != self.orderstatus:
            if self.orderstatus == 'Processing' and not self.processing_at:
                self.processing_at = timezone.now()
            elif self.orderstatus == 'Shipped' and not self.shipped_at:
                if not self.processing_at:
                    self.processing_at = timezone.now()
                self.shipped_at = timezone.now()
            elif self.orderstatus == 'Delivered' and not self.delivered_at:
                if not self.processing_at:
                    self.processing_at = timezone.now()
                if not self.shipped_at:
                    self.shipped_at = timezone.now()
                self.delivered_at = timezone.now()
                pm = str(self.paymentmethod).strip().lower()
                if ('cod' in pm or 'cash' in pm) and self.paymentstatus == 'Pending':
                    self.paymentstatus = 'Paid'
            elif self.orderstatus == 'Cancelled' and not self.cancelled_at:
                self.cancelled_at = timezone.now()
        send_processing = False
        send_shipped = False
        send_out_for_delivery = False
        send_delivered = False
        if is_new and self.orderstatus == 'Processing':
            send_processing = True
        elif not is_new and old_orderstatus != self.orderstatus:
            if self.orderstatus == 'Processing':
                send_processing = True
            elif self.orderstatus == 'Shipped':
                send_shipped = True
            elif self.orderstatus == 'Out for Delivery':
                send_out_for_delivery = True
            elif self.orderstatus == 'Delivered':
                send_delivered = True
        super().save(*args, **kwargs)
        if not self.amazon_order_id:
            if self.user_id:
                user_order_no = Order.objects.filter(user_id=self.user_id, orderid__lte=self.orderid).count()
                self.amazon_order_id = f"{user_order_no:05d}"
            else:
                self.amazon_order_id = f"{self.orderid:05d}"
            Order.objects.filter(pk=self.pk).update(amazon_order_id=self.amazon_order_id)
        if send_processing:
            self.send_processing_email()
        elif send_shipped:
            self.send_shipped_email()
        elif send_out_for_delivery:
            self.send_out_for_delivery_email()
        elif send_delivered:
            self.send_delivery_email()
    def send_processing_email(self):
        if self.user_id and self.user_id.email:
            try:
                email_context = {
                    'order': self,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/order_processing.html', email_context)
                subject = f"Order Confirmation & Processing - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_shipped_email(self):
        if self.user_id and self.user_id.email:
            try:
                email_context = {
                    'order': self,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/order_shipped.html', email_context)
                subject = f"Your Order has been Shipped - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_out_for_delivery_email(self):
        if self.user_id and self.user_id.email:
            try:
                email_context = {
                    'order': self,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/order_out_for_delivery.html', email_context)
                subject = f"Your Order is Out for Delivery - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_delivery_email(self):
        if self.user_id and self.user_id.email:
            try:
                email_context = {
                    'order': self,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/order_delivered.html', email_context)
                subject = f"Order Delivered Successfully - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
class Orderitem(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Cancelled", "Cancelled"),
        ("Delivered", "Delivered"),
        ("Return Requested", "Return Requested"),
        ("Refunded", "Refunded"),
    ]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="Pending")
    orderitemid = models.AutoField(primary_key=True)
    productview_id = models.ForeignKey(Productview, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    selected_size = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return f"{self.productview_id.producttitle} - {self.order_id.user_id.username}"
class PickupAgent(models.Model):
    agentid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
class ReturnRequest(models.Model):
    RETURN_STATUS = (
        ("Requested", "Requested"),
        ("Approved", "Approved"),
        ("Agent Assigned", "Agent Assigned"),
        ("Accepted by Pickup Agent", "Accepted by Pickup Agent"),
        ("Out for Pickup", "Out for Pickup"),
        ("Pickup Completed", "Pickup Completed"),
        ("Refund Initiated", "Refund Initiated"),
        ("Refunded", "Refunded"),
        ("Rejected", "Rejected"),
    )
    orderitem = models.OneToOneField('Orderitem', on_delete=models.CASCADE, related_name="returnrequest", null=True, blank=True)
    delivery_agent = models.ForeignKey('PickupAgent', on_delete=models.SET_NULL, null=True, blank=True, related_name="return_requests")
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=30, choices=RETURN_STATUS, default="Requested")
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    pickup_otp = models.CharField(max_length=6, blank=True, null=True)
    pickup_otp_verified = models.BooleanField(default=False)
    pickup_completed_at = models.DateTimeField(null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    refund_completed_at = models.DateTimeField(null=True, blank=True)
    def generate_pickup_otp(self):
        self.pickup_otp = str(random.randint(100000, 999999))
        self.pickup_otp_verified = False
    def __str__(self):
        return f"{self.order} - {self.status}"
    @property
    def amazon_order_id(self):
        return self.order.amazon_order_id if self.order else ""
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_status = None
        if not is_new:
            try:
                original = ReturnRequest.objects.get(pk=self.pk)
                old_status = original.status
            except ReturnRequest.DoesNotExist:
                pass
        if not is_new and old_status != self.status:
            if self.status == 'Approved' and not self.approved_at:
                self.approved_at = timezone.now()
            elif self.status == 'Pickup Completed' and not self.pickup_completed_at:
                self.pickup_completed_at = timezone.now()
            elif self.status == 'Refunded' and not self.refund_completed_at:
                self.refund_completed_at = timezone.now()
        send_agent_email = False
        send_accepted_email = False
        send_otp_email = False
        send_refund_initiated_email = False
        send_refunded_email = False
        if not is_new and old_status != self.status:
            if self.status == 'Agent Assigned':
                send_agent_email = True
            elif self.status == 'Accepted by Pickup Agent':
                send_accepted_email = True
            elif self.status == 'Out for Pickup':
                send_otp_email = True
            elif self.status == 'Refund Initiated':
                send_refund_initiated_email = True
            elif self.status == 'Refunded':
                send_refunded_email = True
        super().save(*args, **kwargs)
        if send_agent_email:
            self.send_agent_assigned_email()
        elif send_accepted_email:
            self.send_pickup_accepted_email()
        elif send_otp_email:
            self.send_pickup_otp_email()
        elif send_refund_initiated_email:
            self.send_refund_initiated_email()
        elif send_refunded_email:
            self.send_refund_completed_email()
    def send_agent_assigned_email(self):
        if self.delivery_agent and self.delivery_agent.user and self.delivery_agent.user.email:
            try:
                email_context = {
                    'return_request': self,
                    'pickup_agent': self.delivery_agent,
                    'order': self.order,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                subject = f"New Pickup Assigned - EiserShop (#{self.amazon_order_id})"
                html_content = render_to_string('emails/agent_assigned.html', email_context)
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.delivery_agent.user, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_pickup_accepted_email(self):
        if self.order and self.order.user_id and self.order.user_id.email:
            try:
                customer_name = self.order.user_id.first_name or self.order.user_id.username
                agent_name = self.delivery_agent.user.username if self.delivery_agent and self.delivery_agent.user else "Assigned Agent"
                context = {
                    'return_request': self,
                    'customer_name': customer_name,
                    'agent_name': agent_name,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/pickup_accepted.html', context)
                subject = f"Pickup Request Accepted - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.order.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_pickup_otp_email(self):
        if self.order and self.order.user_id and self.order.user_id.email:
            try:
                customer_name = self.order.user_id.first_name or self.order.user_id.username
                context = {
                    'return_request': self,
                    'customer_name': customer_name,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/pickup_otp.html', context)
                subject = f"Pickup OTP - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.order.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_refund_initiated_email(self):
        if self.order and self.order.user_id and self.order.user_id.email:
            try:
                customer_name = self.order.user_id.first_name or self.order.user_id.username
                context = {
                    'return_request': self,
                    'customer_name': customer_name,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/refund_initiated.html', context)
                subject = f"Refund Initiated - EiserShop (#{self.amazon_order_id})"
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.order.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
    def send_refund_completed_email(self):
        if self.order and self.order.user_id and self.order.user_id.email:
            try:
                customer_name = self.order.user_id.first_name or self.order.user_id.username
                refund_amt_str = f"₹{self.refund_amount:,.2f}" if self.refund_amount else "₹0.00"
                context = {
                    'return_request': self,
                    'order': self.order,
                    'customer_name': customer_name,
                    'refund_amount': refund_amt_str,
                    'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string('emails/refund_completed.html', context)
                subject = f"Refund Completed - EiserShop (#{self.amazon_order_id})"
                
                email_thread = threading.Thread(
                    target=send_async_order_email, 
                    args=(self.order.user_id, html_content, subject), 
                    daemon=True
                )
                email_thread.start()
            except Exception as e:
                traceback.print_exc()
class Compare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("user", "product")
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        unique_together = ("user", "product", "size")
    def __str__(self):
        return f"{self.user.username} - {self.product.productname} ({self.size})"
class FlashSale(models.Model):
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    sale_price = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    def is_live(self):
        now = timezone.now()
        return self.is_active and self.start_time <= now <= self.end_time
    def __str__(self):
        return self.product.producttitle
class CouponUsage(models.Model):
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.coupon.code}"
class RecentlyViewed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-viewed_at"]
        unique_together = ("user", "product")
    def __str__(self):
        return f"{self.user.username} - {self.product.producttitle}"
class ProductReview(models.Model):
    product = models.ForeignKey(Productview, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)  # 1 to 5 stars
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.product.producttitle} ({self.rating} Stars)"
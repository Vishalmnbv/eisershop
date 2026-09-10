from .models import Category, Cart, Wishlist, Coupon, Order, Productview
from django.utils import timezone
from django.urls import reverse
from .utils import apply_rating
def cat(request):
    subtotal = 0
    deliverycharge = 0
    discount = 0
    total = 0
    cartcount = 0
    wishlist_count = 0
    order_count = 0  
    category = Category.objects.all()
    browsing_list = []
    browsing_history_url = ""
    banner = None
    if request.user.is_authenticated:
        cartdata = Cart.objects.filter(userid=request.user)
        cartcount = cartdata.count()
        wishlistdata = Wishlist.objects.filter(user=request.user)
        wishlist_count = wishlistdata.count()
        order_count = Order.objects.filter(user_id=request.user).count()
        for i in cartdata:
            subtotal += i.subtotal()
        if 0 < subtotal < 300:
            deliverycharge = 30
        else:
            deliverycharge = 0
        coupon_code = request.session.get("coupon_code", None)
        if coupon_code and subtotal > 0:
            try:
                coupon = Coupon.objects.get(code__iexact=coupon_code)
                now = timezone.now()
                if coupon.active and (coupon.valid_from <= now <= coupon.valid_to) and (subtotal >= coupon.minimum_amount):
                    discount = int((subtotal * coupon.discount) / 100)
                    request.session["coupon_discount"] = discount
                else:
                    request.session.pop("coupon_code", None)
                    request.session.pop("coupon_discount", None)
                    discount = 0
            except Coupon.DoesNotExist:
                request.session.pop("coupon_code", None)
                request.session.pop("coupon_discount", None)
                discount = 0
        else:
            discount = 0
        if discount > subtotal:
            discount = subtotal
        total = max(0, subtotal - discount + deliverycharge)
    # Browsing History Logic
    product_ids = [
        int(pid)
        for pid in request.session.get("recently_viewed", [])
        if str(pid).isdigit()
    ]
    if product_ids:
        browsing_products = list(Productview.objects.filter(productviewid__in=product_ids).select_related("category_id"))
        browsing_products.sort(key=lambda x: product_ids.index(int(x.productviewid)))
        for product in browsing_products[:14]:
            if product.productimage1:
                img_url = (
                    product.productimage1.url
                    if hasattr(product.productimage1, "url")
                    else product.productimage1
                )
                browsing_list.append({
                    "image": img_url,
                    "product_id": product.productviewid,
                    "category_id": product.category_id.categoryid if product.category_id else "",
                })
        browsing_history_url = reverse("browsing_history")
    # Banner Logic
    banner = Productview.objects.filter(in_stock=True).order_by("?").first()
    if banner:
        apply_rating(banner)
    return {
        "category": category,
        "subtotal": subtotal,
        "discount": discount,
        "deliverycharge": deliverycharge,
        "total": total,
        "cartcount": cartcount,
        "wishlist_count": wishlist_count,
        "order_count": order_count, 
        "browsing_list": browsing_list,
        "browsing_history_url": browsing_history_url,
        "home_banner": banner,
    }
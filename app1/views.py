from django.views.generic import TemplateView,ListView,DetailView
from app1.templatetags.indian_formatting import format_indian_currency
from django.db.models import Case, When, Value, IntegerField
from django.db.models import Case, Q, Value, When
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models.functions import TruncMonth
from django.db.models import Sum, Value, Prefetch
from django.db.models.functions import Coalesce
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Case, When
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Count
from django.db import transaction
from django.db.models import Value
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum
from datetime import timedelta
from django.db.models import Q
from django.http import Http404
from django.urls import reverse
from django.contrib import auth
from .utils import apply_rating, send_async_login_email, send_async_email
from django.contrib.auth.decorators import login_required
from urllib.parse import quote
from django.views import View
from user_agents import parse
from datetime import date
from django.utils import timezone
from datetime import date, datetime
from django.http import HttpResponse
from xhtml2pdf import pisa
from decimal import Decimal
from .models import *
import urllib.parse
import threading
import traceback
import requests
import random
import os
import re
import base64
import resend
from django.contrib.staticfiles import finders
from django.utils.safestring import mark_safe
# Create your views here.
def send_email_thread(email):
    try:
        email.send(fail_silently=False)
    except Exception:
        traceback.print_exc()
def get_featured_brands():
    brand_configs = [
        {"name": "Majestic Man Stylish Slim Fit Cotton Spread Collar Checked Casual Shirt", "cat_id": 1, "query": "Majestic Man Stylish Slim Fit Cotton Spread Collar Checked Casual Shirt", "type": "shirt", "search_term": None, "id": 63},
        {"name": "Majestic Man Men Classic Slim Fit Pure Cotton Casual Shirt", "cat_id": 1, "query": "Majestic Man Men Classic Slim Fit Pure Cotton Casual Shirt", "type": "shirt", "search_term": "Classic Slim"},
        {"name": "Pinkmint Mens Cotton Blend Regular Fit Long Sleeve Button Down White Shirt for Men Collared Casual Formal Soild Shirt", "cat_id": 1, "query": "Pinkmint Mens Cotton Blend Regular Fit Long Sleeve Button Down White Shirt for Men Collared Casual Formal Soild Shirt", "type": "shirt", "search_term": "Pinkmint"},
        {"name": "Combo of Men’s Casual Cotton Blend Shirt Long Sleeve Button Down with Spread Collar", "cat_id": 1, "query": "Combo of Men’s Casual Cotton Blend Shirt Long Sleeve Button Down with Spread Collar", "type": "shirt", "search_term": "MADHAVISTA"},
        {"name": "NexaFlair Men's Shirt Regular Fit Solid Pattern Linen Cotton with Long Sleeve Collared Neck Standard Length and Button Down Closure Type Mens Casual Shirts Man's Formal Shirts", "cat_id": 1, "query": "NexaFlair Men's Shirt Regular Fit Solid Pattern Linen Cotton with Long Sleeve Collared Neck Standard Length and Button Down Closure Type Mens Casual Shirts Man's Formal Shirts", "type": "shirt", "search_term": "NexaFlair"},
        {"name": "Allen Solly Men’s Solid Polo T‑Shirt Regular Fit Premium Cotton Contrast Tipping Collar Smart Casual Wear", "cat_id": 6, "query": "Allen Solly Men’s Solid Polo T‑Shirt Regular Fit Premium Cotton Contrast Tipping Collar Smart Casual Wear", "type": "tshirt", "search_term": "Allen Solly"},
        {"name": "Lux Cozi Men's Half Sleeve Soild Casual Regular Fit T-Shirt with Chest Pocket Polo Tshirt for Men", "cat_id": 6, "query": "Lux Cozi Men's Half Sleeve Soild Casual Regular Fit T-Shirt with Chest Pocket Polo Tshirt for Men", "type": "tshirt", "search_term": "Lux Cozi"},
        {"name": "WildHorn Genuine Leather Wallet for Men Slim Bifold Wallet with RFID Blocking Multiple Card Slots & Coin Pocket Premium Leather Mens Wallet", "cat_id": 11, "query": "WildHorn Genuine Leather Wallet for Men Slim Bifold Wallet with RFID Blocking Multiple Card Slots & Coin Pocket Premium Leather Mens Wallet", "type": "wallet", "search_term": "WildHorn"},
        {"name": "NAPA HIDE Leather Wallet for Men Handcrafted Credit/Debit Card Slots 2 Currency Compartments 2 Secret Compartments", "cat_id": 11, "query": "NAPA HIDE Leather Wallet for Men Handcrafted Credit/Debit Card Slots 2 Currency Compartments 2 Secret Compartments", "type": "wallet", "search_term": "NAPA HIDE"},
        {"name": "Mehrang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric", "cat_id": 13, "query": "Mehrang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric", "type": "trouser", "search_term": "Mehrang"},
        {"name": "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear", "cat_id": 13, "query": "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear", "type": "trouser", "search_term": "Vogaan"}, 
        {"name": "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4", "cat_id": 19, "query": "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4", "type": "earBuds", "search_term": "pTron"},  
        {"name": "Safari Cabin Genius Alley rolley Bag Hard Case Polypropylene, 4 Spinner Wheels, 360 Degree Wheeling Carry on Luggage, Travel Bag, Suitcase for Travel, Trolley Bags for Travel", "cat_id": 10, "query": "Safari Cabin Genius Alley rolley Bag Hard Case Polypropylene, 4 Spinner Wheels, 360 Degree Wheeling Carry on Luggage, Travel Bag, Suitcase for Travel, Trolley Bags for Travel", "type": "Suitcase", "search_term": "Safari"},
        {"name": "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel", "cat_id": 10, "query": "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel", "type": "Suitcase", "search_term": "Teakwood"},
        {"name": "URBAN FOREST Zeus Vintage Leather Bi-Fold Wallet for Men", "cat_id": 11, "query": "URBAN FOREST Zeus Vintage Leather Bi-Fold Wallet for Men", "type": "Wallet", "search_term": "URBAN FOREST"},
        {"name": "Boldfit Sneakers for Man Lightweight Shoes for Men Comfortable Sneakers for Men Air Mesh Casual Shoes Mens Soft Cushion Insole Lace Up Casual Boys Shoe Sneaker DripWave", "cat_id": 8, "query": "Boldfit Sneakers for Man Lightweight Shoes for Men Comfortable Sneakers for Men Air Mesh Casual Shoes Mens Soft Cushion Insole Lace Up Casual Boys Shoe Sneaker DripWave", "type": "Shoes", "search_term": "Boldfit"},
        {"name": "Nasher Miles Pondicherry Hard-Sided Polypropylene Check-in Luggage 28 inch 8 Wheels Large Trolley Bag for Travel Suitcase", "cat_id": 10, "query": "Nasher Miles Pondicherry Hard-Sided Polypropylene Check-in Luggage 28 inch 8 Wheels Large Trolley Bag for Travel Suitcase", "type": "Suitcase", "search_term": "Nasher Miles"},
        {"name": "DEELMO Men's Regular Fit Button Down Dress Shirts Textured Long Sleeve Casual Hawaiian Shirt", "cat_id": 1, "query": "DEELMO Men's Regular Fit Button Down Dress Shirts Textured Long Sleeve Casual Hawaiian Shirt", "type": "shirt", "search_term": "DEELMO"},
        {"name": "IndoPrimo Men's Cotton Shirt with Stylish Full Sleeves Spread Collared Neck Solid Pattern Western Style Classic Fit and Standard Length Casual Shirt for Man", "cat_id": 1, "query": "IndoPrimo Men's Cotton Shirt with Stylish Full Sleeves Spread Collared Neck Solid Pattern Western Style Classic Fit and Standard Length Casual Shirt for Man", "type": "shirt", "search_term": "IndoPrimo"},
        {"name": "WOW IMAGINE Shock Proof Flip Cover Back Case Cover for Samsung Galaxy M17e 5G F70e 5G M07 F07 A07 A07 5G Flexible Leather Finish Card Pockets Wallet & Stand", "cat_id": 20, "query": "WOW IMAGINE Shock Proof Flip Cover Back Case Cover for Samsung Galaxy M17e 5G F70e 5G M07 F07 A07 A07 5G Flexible Leather Finish Card Pockets Wallet & Stand", "type": "Mobile Cover", "search_term": "WOW IMAGINE"},
        {"name": "Casotec Flip Cover Back Case for Apple iPhone 13 Pro Premium Leather Finish Inbuilt Pockets & Stand Flip Cover Back Case for Apple iPhone 13 Pro","cat_id": 20,"query": "Casotec Flip Cover Back Case for Apple iPhone 13 Pro Premium Leather Finish Inbuilt Pockets & Stand Flip Cover Back Case for Apple iPhone 13 Pro","type": "Mobile Cover","search_term": "Casotec",}
    ]
    def fetch_product(config):
        if config.get("id"):
            return Productview.objects.filter(productviewid=config["id"]).first()
        term = config["search_term"]
        product = Productview.objects.filter(productname__icontains=term, in_stock=True).first()
        if not product:
            product = Productview.objects.filter(producttitle__icontains=term, in_stock=True).first()
        return product
    featured_brands = []
    for item in brand_configs:
        product = fetch_product(item)
        featured_brands.append({
            "name": item["name"],
            "category_id": item["cat_id"],
            "product_id": product.productviewid if product else None,
            "search_query": item["query"],
            "image": product.get_main_image() if product else None,
            "type": item["type"],
        })
    return featured_brands
def attach_variants_and_rating(product):
    if not product:
        return product
    apply_rating(product)
    variants = Productview.objects.filter(category_id=product.category_id,producttitle=product.producttitle,in_stock=True).order_by("productviewid")
    ordered_variants = [product] + [v for v in variants if v.productviewid != product.productviewid]
    variants_list = []
    used_colors = set()
    for variant in ordered_variants:
        color = (variant.productcolor1 or "").strip()
        if not color or color.lower() in used_colors:
            continue
        used_colors.add(color.lower())
        color_code = (
            get_clean_color_code(color) 
            if callable(globals().get("get_clean_color_code")) 
            else ""
        )
        variants_list.append({
            "id": variant.productviewid,
            "name": color,
            "image": variant.productimage1,
            "color_code": color_code,
        })
    product.color_variants = variants_list
    return product
class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_brands"] = get_featured_brands()
        # Search History
        if self.request.user.is_authenticated:
            context["search_history"] = SearchHistory.objects.filter(userid=self.request.user).order_by("-searched_at")[:20]
        else:
            context["search_history"] = self.request.session.get("search_history", [])
        # Coupons
        context["coupons"] = Coupon.objects.filter(active=True).order_by("-couponid")
        # Top Rated Products (Shirts, T-Shirts)
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=3)
        top_rated_products = []
        category_filter = Q(category_id__categoryname__icontains="shirt") | Q(category_id__categoryname__icontains="tshirt")
        titles = Productview.objects.filter(category_filter, in_stock=True).values_list("producttitle", flat=True).distinct()
        for title in titles:
            product = Productview.objects.filter(category_filter, producttitle=title, in_stock=True).first()
            if product:
                top_rated_products.append(attach_variants_and_rating(product))
        top_rated_products.sort(key=lambda x: getattr(x, "rating", 0), reverse=True)
        top_product_ids = [p.productviewid for p in top_rated_products]
        context["top_rated_products"] = top_rated_products
        context["top_product_ids"] = top_product_ids
        # Deals Of The Day
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=3)
        deals_of_the_day = []
        deal_titles = list(Productview.objects.filter(in_stock=True, category_id__categoryname__in=["Shirt", "Tshirt"]).values_list("producttitle", flat=True).distinct())
        random.shuffle(deal_titles)
        for title in deal_titles:
            product = Productview.objects.filter(producttitle=title, in_stock=True, category_id__categoryname__in=["Shirt", "Tshirt"]).order_by("-productviewid").first()
            if product:
                deals_of_the_day.append(attach_variants_and_rating(product))
        random.shuffle(deals_of_the_day)
        deal_product_ids = [p.productviewid for p in deals_of_the_day]
        context["deals_of_the_day"] = deals_of_the_day
        # New Arrivals
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=3)
        new_arrivals = []
        target_arrival_titles = [
            "Bacca Bucci Men Lace Up Basketball Shoe",
            "Bacca Bucci Men Lace Up Running Shoes",
            "Bacca Bucci Men Lace Up Athletic Shoes",
            "Reebok Men's Running Shoes EVA Cushioned Breathable Mesh Sports Shoes for Men",
            "Safari Pentagon Pro 8 Wheels Spinner Checkin Trolley Bag, Hard Case Polypropylene 360º Wheeling Luggage for Men & Women, Suitcase Bag",
            "Safari Cabin Genius Alley rolley Bag Hard Case Polypropylene, 4 Spinner Wheels, 360 Degree Wheeling Carry on Luggage, Travel Bag, Suitcase for Travel, Trolley Bags for Travel",
            "Provogue Spectrum Hard-Sided PP Trolley Bags for Travel Medium Size Expandable Luggage Suitcase with 8 Wheels Combination Lock",
            "Boldfit Sneakers for Man Lightweight Shoes for Men Comfortable Sneakers for Men Air Mesh Casual Shoes Mens Soft Cushion Insole Lace Up Casual Boys Shoe Sneaker DripWave",
            "Campus Men Oxyfit (N) Walking Shoes",
            "WildHorn Genuine Leather Wallet for Men Slim Bifold Wallet with RFID Blocking Multiple Card Slots & Coin Pocket Premium Leather Mens Wallet",
            "URBAN FOREST Zeus Vintage Leather Bi-Fold Wallet for Men",
            "Tommy Hilfiger Men's Cuiaba Slimfold Wallet Leather with Liner Texture Ultra-Slim Minimalist Design Stylish Purse for Men",
            "NAPA HIDE Leather Wallet for Men Handcrafted Credit/Debit Card Slots 2 Currency Compartments 2 Secret Compartments",
            "TALED Genuine Leather Wallet - RFID Blocking Wallet for Men,12 Card Holder with Coin Pocket for Men with Gift Box, Nature Anthracite",
            "Spiffy Genuine Leather Wallet for Men RFID Men Wallet, Slim Bifold Card Holder Wallet for Man with 12 Card Slots",
            "Mehrang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric",
            "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear",
            "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4",
            "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel",
            "Bacca Bucci Men Lace Up Sneaker Shoes",
            "Bacca Bucci Mens Ironman Running Shoes",
            "Reebok Men's Running Shoes Lightweight Durable Sports Shoes for Men Lightweight Gym Shoe for Men Running, Jogging, Walking & Gym Flylite Lss Voyager",
            "WOW IMAGINE Shock Proof Flip Cover Back Case Cover for Samsung Galaxy M17e 5G F70e 5G M07 F07 A07 A07 5G Flexible Leather Finish Card Pockets Wallet & Stand",
            "Pikkme Samsung Galaxy M32 4G M32 Prime F22 4G Flip Cover Leather Finish Inside TPU with Card Pockets Wallet Stand and Shock Proof Magnetic Closing Complete Protection Flip Case",
            "Solimo Mobile Cover for Apple iPhone 15 Plus Full Camera Protection Liquid Silicon Case  Flexible Bumper Case for Apple iPhone 15 Plus",
            "LIRAMARK Silicone Soft Back Cover Case for Apple iPhone 12 Mini",
            "Casotec Flip Cover Back Case for Apple iPhone 13 Pro Premium Leather Finish Inbuilt Pockets & Stand  Flip Cover Back Case for Apple iPhone 13 Pro",
        ]
        arrival_titles = Productview.objects.filter(in_stock=True, producttitle__in=target_arrival_titles).values_list("producttitle", flat=True).distinct()
        for title in arrival_titles:
            product = Productview.objects.filter(producttitle=title, in_stock=True).order_by("-productviewid").first()
            if product:
                new_arrivals.append(attach_variants_and_rating(product))
        context["new_arrivals"] = new_arrivals
        context["new_arrival_product_ids"] = [p.productviewid for p in new_arrivals]
        # Recommended For You
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=3)
        recommended_products = []
        base_queryset = Productview.objects.filter(in_stock=True, category_id__categoryname__in=["Shirt", "Tshirt"]).exclude(productviewid__in=deal_product_ids + top_product_ids)
        rec_titles = list(base_queryset.values_list("producttitle", flat=True).distinct())
        random.shuffle(rec_titles)
        seen_titles = set()
        for title in rec_titles:
            title_clean = title.strip() if title else ""
            if title_clean and title_clean not in seen_titles:
                product = base_queryset.filter(producttitle=title).order_by("-productviewid").first()
                if product:
                    seen_titles.add(title_clean)
                    recommended_products.append(attach_variants_and_rating(product))
        random.shuffle(recommended_products)
        context["recommended_products"] = recommended_products
        # Color Variants 
        all_product_lists = [top_rated_products, deals_of_the_day, new_arrivals, recommended_products]
        for product_list in all_product_lists:
            if product_list:
                titles = [p.producttitle for p in product_list if p and p.producttitle]
                all_variants = Productview.objects.filter(producttitle__in=titles).only("productviewid", "category_id", "producttitle", "productcolor1", "productimage1")
                variant_dict = {}
                for v in all_variants:
                    if v.producttitle:
                        variant_dict.setdefault(v.producttitle, []).append(v)
                for product in product_list:
                    related_variants = variant_dict.get(product.producttitle, [])
                    variants_list = []
                    used_colors = set()
                    current_color = str(getattr(product, "productcolor1", "") or "").strip()
                    if current_color:
                        used_colors.add(current_color.lower())
                        variants_list.append({
                            "id": product.productviewid,
                            "name": current_color,
                            "image": product.productimage1,
                            "color_code": get_clean_color_code(current_color)
                            if callable(globals().get("get_clean_color_code"))
                            else "",
                        })
                    for variant in related_variants:
                        color = str(getattr(variant, "productcolor1", "") or "").strip()
                        if not color or color.lower() in used_colors:
                            continue
                        used_colors.add(color.lower())
                        variants_list.append({
                            "id": variant.productviewid,
                            "name": color,
                            "image": variant.productimage1,
                            "color_code": get_clean_color_code(color)
                            if callable(globals().get("get_clean_color_code"))
                            else "",
                        })
                    product.color_variants = variants_list
        return context
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            SearchHistory.objects.filter(userid=request.user).delete()
        else:
            request.session["search_history"] = []
        return redirect("home")
class RegisterView(View):
    template_name = "register.html"
    def get(self, request):
        context = {
            "category": Category.objects.all(),
            "username": request.GET.get("username", ""),
        }
        return render(request, self.template_name, context)
    def post(self, request):
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        mobile = request.POST.get("mobile", "").strip()
        password = request.POST.get("password", "")
        conformpassword = request.POST.get("conformpassword", "")
        image = request.FILES.get("image")
        if password != conformpassword:
            messages.error(request, "Passwords do not match")
            return redirect("register")
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already taken")
            return redirect("register")
        if not mobile.isdigit() or len(mobile) != 10:
            messages.error(request, "Please enter a valid 10-digit mobile number")
            return redirect("register")
        if Profile.objects.filter(mobile=mobile).exists():
            messages.warning(request, "Mobile number already registered")
            return redirect("register")
        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password,
        )
        Profile.objects.create(user=user, image=image, mobile=mobile)
        messages.success(request, f"Hello {username}! Your account has been created successfully.")
        return redirect(f"/login/?username={username}")
resend.api_key = os.environ.get("RESEND_API_KEY")
class LoginView(View):
    template_name = "login.html"
    def get(self, request):
        context = {
            "category": Category.objects.all(),
            "username": request.GET.get("username", ""),
        }
        return render(request, self.template_name, context)
    def post(self, request):
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = auth.authenticate(
            request,
            username=username,
            password=password
        )
        if user is None:
            messages.error(request,"Invalid username or password")
            return render(
                request,
                self.template_name,
                {
                    "category": Category.objects.all(),
                    "username": username,
                },
            )
        auth.login(request, user)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(",")[0].strip()
        else:
            ip_address = request.META.get("REMOTE_ADDR", "127.0.0.1")
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        device = "Unknown Device"
        try:
            ua = parse(user_agent)
            browser = f"{ua.browser.family} {ua.browser.version_string}"
            operating_system = f"{ua.os.family} {ua.os.version_string}"
            device = f"{browser} on {operating_system}"
        except Exception:
            device = "Unknown Device"
        location = "Unknown Location"
        if ip_address not in ["127.0.0.1", "::1"]:
            try:
                response = requests.get(
                    f"http://ip-api.com/json/{ip_address}",
                    timeout=4,
                    headers={"User-Agent": "EiserShop"}
                )
                data = response.json()
                if data.get("status") == "success":
                    city = data.get("city", "")
                    region = data.get("regionName", "")
                    country = data.get("country", "")
                    location = f"{city}, {region}, {country}"
            except Exception as e:
                print("Location lookup error:", str(e))
        if user.email:
            try:
                # EMAIL 
                email_context = {
                    "user": user,
                    "login_time": timezone.localtime().strftime("%d-%m-%Y %I:%M %p"),
                    "device": device,
                    "location": location,
                    "ip_address": ip_address,
                    "logo_url": "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string("emails/login_success.html",email_context)
                email_thread = threading.Thread(target=send_async_login_email,args=(user,html_content,),daemon=True,)
                email_thread.start()
            except Exception as e:
                print("Login email setup error:", str(e))
                traceback.print_exc()
        messages.success(request,f"Welcome back, {user.username}! You have successfully logged in.")
        return redirect("home")
class LogoutView(View):
    def get(self,request):
        username = getattr(request.user,"username","User")
        auth.logout(request)
        messages.success(request,f"Thank you for visiting EiserShop, {username}! You have successfully logged out.")
        return redirect("home")
class ForgetPasswordView(View):
    template_name = "forgetpassword.html"
    def get(self, request):
        return render(request, self.template_name, {"category": Category.objects.all()})
    def post(self, request):
        context = {
            "category": Category.objects.all(),
            "identifier": request.POST.get("identifier", "").strip(),
            "show_password": True,
        }
        identifier = context["identifier"]
        otp = request.POST.get("otp", "").strip()
        newpassword = request.POST.get("newpassword", "")
        confirmpassword = request.POST.get("confirmpassword", "")
        user = User.objects.filter(Q(email__iexact=identifier) | Q(username__iexact=identifier)).first()
        if not user:
            messages.error(request, "No account found with this Email or Username.")
            return render(request, self.template_name, context)
        if "send_otp" in request.POST:
            generated_otp = str(random.randint(100000, 999999))
            request.session["reset_email"] = user.email
            request.session["reset_otp"] = generated_otp
            try:
                otp_html_content = f"""
                <div style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <div style="background-color: #131921; padding: 22px; text-align: center;">
                            <img src="https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png" alt="EiserShop Logo" style="max-height: 50px; display: block; margin: 0 auto;">
                            <p style="color: #ffffff; margin-top: 10px; font-size: 15px;">Password Reset Request</p>
                        </div>
                        <div style="padding: 30px; color: #333333;">
                            <h2 style="color: #131921;">Hello {user.username},</h2>
                            <p>We received a request to reset your password for your <strong>EiserShop</strong> account.</p>
                            <p>Your Password Reset OTP is:</p>
                            <div style="background-color: #f8f9fa; padding: 15px; text-align: center; font-size: 24px; font-weight: bold; letter-spacing: 2px; color: #7fad39; margin: 20px 0; border-radius: 4px;">
                                {generated_otp}
                            </div>
                            <p style="color: #777777; font-size: 13px;">Do not share this OTP with anyone. If you didn't request this, please ignore this email.</p>
                            <p style="margin-top: 30px;">Regards,<br><strong>EiserShop Team</strong></p>
                        </div>
                    </div>
                </div>
                """
                threading.Thread(
                    target=send_async_email,
                    args=(user.email, "Password Reset OTP - EiserShop", otp_html_content),
                    daemon=True
                ).start()
                messages.success(request, "OTP sent successfully to your registered email.")
            except Exception:
                traceback.print_exc()
                messages.error(request, "Unable to send OTP email.")
            return render(request, self.template_name, context)
        if request.session.get("reset_email") != user.email:
            messages.error(request, "Please generate OTP first.")
            return render(request, self.template_name, context)
        if otp != request.session.get("reset_otp"):
            messages.error(request, "Invalid OTP.")
            return render(request, self.template_name, context)
        if newpassword != confirmpassword:
            messages.error(request, "Passwords do not match.")
            return render(request, self.template_name, context)
        if len(newpassword) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return render(request, self.template_name, context)
        user.set_password(newpassword)
        user.save()
        request.session.pop("reset_email", None)
        request.session.pop("reset_otp", None)
        try:
            html_content = render_to_string(
                "emails/password_reset_success.html",
                {
                    "user": user,
                    "change_time": timezone.localtime().strftime("%d-%m-%Y %I:%M %p"),
                    "logo_url": "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                },
            )
            threading.Thread(
                target=send_async_email,
                args=(user.email, "Password Changed Successfully - EiserShop", html_content),
                daemon=True
            ).start()
        except Exception:
            traceback.print_exc()  
        messages.success(request, "Password reset successfully.")
        return redirect(f"/login/?username={user.username}")
class EditProfileView(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "editprofile.html"
    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        last_order = Order.objects.filter(user_id=request.user).order_by("-date").first()
        if last_order and hasattr(last_order, 'address') and last_order.address:
            profile.delivery_address = last_order.address
        else:
            profile.delivery_address = ""
        context = {"category": Category.objects.all(), "profile": profile}
        return render(request, self.template_name, context)
    def post(self, request):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        user.first_name = request.POST.get("firstname", "").strip()
        user.last_name = request.POST.get("lastname", "").strip()
        user.username = request.POST.get("username", "").strip()
        user.email = request.POST.get("email", "").strip()
        profile.delivery_address = request.POST.get("delivery_address", "").strip()
        profile.mobile = request.POST.get("mobile", "").strip()
        uploaded_image = request.FILES.get("profile_image")
        if User.objects.exclude(pk=user.pk).filter(username=user.username).exists():
            messages.error(request, "Username already exists.")
            return redirect("editprofile")
        if User.objects.exclude(pk=user.pk).filter(email=user.email).exists():
            messages.error(request, "Email already exists.")
            return redirect("editprofile")
        try:
            user.save()
            if uploaded_image:
                profile.image = uploaded_image
            profile.save()  
            success_msg = f'<div class="d-flex align-items-center"><img src="/static/IMAGES/favicon.png" style="width: 40px; height: 40px; object-fit: contain;" class="me-2"> Hello {user.username}, your profile has been updated successfully.</div>'
            messages.success(request, mark_safe(success_msg))
            return redirect("home")
        except IntegrityError:
            messages.error(request, "Username or Email already exists.")
            return redirect("editprofile")
color_map = {
    "white": "#FFFFFF",
    "black": "#000000",
    "red": "#FF0000",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "green": "#008000",
    "grey": "#808080",
    "brown": "#8B4513",
    "cream": "#FFFDD0",
    "peach": "#FFDAB9",
    "beige": "#F5F5DC",
    "maroon": "#800000",
    "purple": "#800080",
    "pink": "#FFC0CB",
    "orange": "#FFA500",
    "olive": "#808000",
    "cyan": "#00FFFF",
    "teal": "#008080",
    "rust": "#B7410E",
    "mustard": "#FFDB58",
    "wine": "#722F37",
    "khaki": "#C3B091",
    "charcoal": "#36454F",
    "emerald": "#50C878",
    "pista": "#93C572",
    "rama": "#00A896",
    "blaze blue": "#005BFF",
    "rogue red": "#A61212",
    "sapphire black": "#0B132B",
    "moonlight silver": "#D6DBDF",
    "serene green": "#9CAF88",
    "velvet black": "#121212",
    "orange haze": "#FF7F3E",
    "vibe violet": "#8A2BE2",
    "blitz blue": "#00A3FF",
    "seaport teal": "#007C83",
    "tan crunch": "#B35A2B",
    "black mio": "#1C1C1C",
    "brown crackle": "#6B4226",
    "grey hunter": "#666A6D",
    "hunter blue": "#355C7D",
    "nature anthracite": "#4A4A4A",
    "english green": "#1B4D3E",
    "dark green": "#013220",
    "medium grey": "#808080",
    "sky blue": "#87CEEB",
    "cadet blue": "#5F9EA0",
    "royal blue": "#4169E1",
    "navy blue": "#000080",
    "navy": "#000080",
    "dark blue": "#00008B",
    "light blue": "#ADD8E6",
    "lightblue": "#ADD8E6",
    "ink blue": "#000F55",
    "oxford blue": "#002147",
    "aqua": "#00FFFF",
    "aqua blue": "#00FFFF",
    "sea angel": "#48D1CC",
    "scuba blue": "#00C4E6",
    "frost fade blue": "#A0C4DF",
    "aqua hush blue": "#70A9C1",
    "batik blue": "#1C39BB",
    "medium blue": "#0000CD",
    "olive green": "#556B2F",
    "light green": "#90EE90",
    "mint green": "#98FF98",
    "mintgreen": "#98FF98",
    "sea green": "#2E8B57",
    "midnight fern green": "#1A3323",
    "teal green": "#00827F",
    "deep forrest": "#1B3B2B",
    "deep brown": "#4A2E2B",
    "clay": "#B66A50",
    "white grey": "#E0E0E0",
    "navy grey": "#354052",
    "black grey": "#333333",
    "dark grey": "#A9A9A9",
    "light grey": "#D3D3D3",
    "dusty grey": "#8D8D8D",
    "grey melange": "#BEBEBE",
    "flintstone": "#6C7A89",
    "dusty pink": "#DCAE96",
    "mauve pink": "#C8A2C8",
    "pale yellow": "#FFF8DC",
    "sundrip yellow": "#F9D71C",
    "mineral yellow": "#E3A857",
    "dusty copper": "#B87333",
    "dusty oak": "#B8860B",
    "milky white": "#FDFFF5",
    "light beige": "#F5F5DC",
    "coffee": "#6F4E37",
    "apricat": "#FBCEB1",
    "white-blue": "#87CEEB",
    "tan": "#D2B48C",
    "vintage brown": "#593319",
    "vintage cognac": "#9A461E",
    "vintage green": "#3E5336",
    "vintage grey": "#62615D",
    "vintage tobacco": "#724A2D",
    "caramel brown": "#A8652A",
    "vintage black": "#252525",
    "vintage blue": "#384B5F",
    "vintage red": "#8B2626",
    "fresh blue": "#00A2E8",
    "lunar pearl": "#E5E4E2",
    "pitch black": "#0B0B0B",
    "light gold": "#E6CA65",
    "cloud white": "#F5F5F7",
    "space black": "#1B1B1D",
    "deep blue": "#00008B",
    "silver": "#C0C0C0",
    "cosmic orange": "#E85D04",
    "titanium whitesilver": "#E8E8E8",
    "titanium gray": "#6C7072",
    "titanium silverblue": "#B0C4DE",
    "cobalt violet": "#8A2BE2",
    "coralred": "#FF4040",
    "dune glow": "#E6C280",
    "sage mist": "#9AB09E",
    "storm blue": "#496076",
    "frosted silver": "#D9E1E8",
    "white sabre": "#F0F4F8",
    "black sabre": "#181818",
    "active black": "#111111",
    "bold blue": "#0047AB",
    "jet black": "#0A0A0A",
    "taupe": "#483C32",
    "lime green": "#32CD32",
    "lavender": "#E6E6FA",
    "sage green": "#9CAF88",
    "lime yellow": "#DFFF00",
    "rose gold": "#B76E79",
    "ivory mist": "#F3F0E6",
    "carbon black": "#1C1C1C",
    "forest sage": "#4F6F52",
    "vibrant black": "#000000",
    "monet purple": "#7B68A6",
    "agile white": "#F8F8F5",
    "lilac": "#C8A2C8",
    "light brown": "#B5651D",
    "true purple": "#6A0DAD",
    "snow white": "#FFFAFA",
    "space blue": "#1D2951",
    "true blue": "#0073CF",
    "dark cyan": "#008B8B",
    "swedish white": "#FBFBF9",
    "chocolate": "#D2691E",
    "orange mint": "#FF9F74",
    "lemon cola": "#D4AC0D",
    "gold": "#FFD700",
    "gold purple": "#7E57C2",
    "powder blue": "#B0E0E6",
    "raven black": "#1B1B1B",
    "spring green": "#00FF7F",
    "chiku": "#8B5A2B",
    "blazing black": "#050505",
    "mist blue": "#6488EA",
    "sunset orange": "#FD5E53",
    "hyper black": "#0F0F0F",
    "vivid mint": "#00FFCC",
    "lavender drift": "#DCD0FF",
    "shadow black": "#121212",
    "graphite grey": "#4B4E53",
    "quick silver": "#A6A6A6",
    "mirage purple": "#5E4B8B",
    "space gray": "#535150",
    "starlight": "#F0EAD6",
    "marigold yellow": "#EAA221",
    "cayenne red": "#901111",
    "dawn grey": "#A3A8B0",
    "sky": "#87CEEB",
    "dark green": "#006400",
    "choco": "#5C3A21",
    "chiku": "#A75533",
    "alder brown": "#7A431D",
    "aquamarine": "#35A79C",      
    "forest green": "#2C4C3E",
    "haze black": "#2C2D30",
    "stone grey": "#8E8E93",
    "silicone black": "#1C1C1E",
    "silicone blue": "#3B6E8C",
    "silicone green": "#4A7C59",
    "silicone pink": "#D17A91",   
    "camel blue": "#345976",
    "camel black": "#222222",
}
def get_clean_color_code(color_name):
    if not color_name:
        return "#CCCCCC"
    clean_name = color_name.strip().lower()
    if clean_name in color_map:
        return color_map[clean_name]
    sorted_keys = sorted(color_map.keys(), key=len, reverse=True)
    for key in sorted_keys:
        if key in clean_name:
            return color_map[key]      
    return "#888888"
class CollectionView(ListView):
    model = Productview
    template_name = "collection.html"
    context_object_name = "products"
    paginate_by = 20
    def paginate_queryset(self, queryset, page_size):
        try:
            return super().paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs[self.page_kwarg] = 1
            return super().paginate_queryset(queryset, page_size)
    def get_filtered_queryset(self):
        if not hasattr(self, "category"):
            self.category = get_object_or_404(Category, categoryid=self.kwargs["categoryid"])
        queryset = Productview.objects.filter(category_id=self.category).order_by("-productviewid")
        # Search Query
        raw_search = (self.request.GET.get("q") or "").strip()
        if raw_search:
            queryset = queryset.filter(Q(producttitle__icontains=raw_search) | Q(productname__icontains=raw_search))
        # Narrow Filter 
        narrow_filter = (self.request.GET.get("narrow_filter") or "").strip()
        if narrow_filter:
            queryset = queryset.filter(Q(producttitle__iexact=narrow_filter) | Q(producttitle__icontains=narrow_filter) | Q(productname__icontains=narrow_filter))
        # Brand Filter 
        selected_brands = self.request.GET.getlist("brand")
        if selected_brands:
            brand_query = Q()
            for brand in selected_brands:
                brand = brand.strip()
                if not brand:
                    continue
                brand_query |= Q(producttitle__iexact=brand) | Q(producttitle__icontains=brand) | Q(productname__icontains=brand)
            if brand_query:
                queryset = queryset.filter(brand_query)
        # Size Filter
        selected_sizes = self.request.GET.getlist("size")
        if selected_sizes:
            size_query = Q()
            for size in selected_sizes:
                size_query |= (Q(productsize__iexact=size) | Q(productsize1__iexact=size) | Q(productsize2__iexact=size) | Q(productsize3__iexact=size))
            queryset = queryset.filter(size_query)
        # Price Filter
        price = self.request.GET.get("price")
        if price == "0-500":
            queryset = queryset.filter(productprice__lte=500)
        elif price == "500-1000":
            queryset = queryset.filter(productprice__gte=500, productprice__lte=1000)
        elif price == "1000-2000":
            queryset = queryset.filter(productprice__gte=1000, productprice__lte=2000)
        elif price == "2000-5000":
            queryset = queryset.filter(productprice__gte=2000, productprice__lte=5000)
        elif price == "5000-above":
            queryset = queryset.filter(productprice__gte=5000)
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        if min_price:
            queryset = queryset.filter(productprice__gte=min_price)
        if max_price:
            queryset = queryset.filter(productprice__lte=max_price)
        # Color Filter
        selected_colors = self.request.GET.getlist("color")
        if selected_colors:
            color_query = Q()
            for color in selected_colors:
                color = color.strip()
                if color.lower() == "blue":
                    color_query |= Q(productcolor1__iexact="Blue") | (
                        Q(productcolor1__icontains="Oxford Blue") 
                        & ~Q(productcolor1__icontains="Sky Blue") 
                        & ~Q(productcolor1__icontains="Navy Blue") 
                        & ~Q(productcolor1__icontains="Dark Blue")
                    )
                else:
                    color_query |= Q(productcolor1__icontains=color)
            queryset = queryset.filter(color_query)
        return queryset
    def get_queryset(self):
        raw_search = (self.request.GET.get("q") or "").strip()
        save_search = (self.request.GET.get("save_search") == "1")
        if save_search and raw_search and self.request.user.is_authenticated:
            history, created = SearchHistory.objects.get_or_create(userid=self.request.user,keyword__iexact=raw_search,defaults={"keyword": raw_search},)
            if not created:
                history.search_count += 1
                history.save()
        queryset = self.get_filtered_queryset()
        today = timezone.localdate()
        ratings_map = {
            "Majestic Man Men Classic Slim Fit Pure Cotton Casual Shirt": 4.0,
            "U TURN Men's Casual Printed Striped Stylish Latest Formal Shirt for Men": 3.6,
            "Pinkmint Mens Cotton Blend Regular Fit Long Sleeve Button Down White Shirt for Men Collared Casual Formal Soild Shirt": 3.7,
            "Majestic Man Stylish Slim Fit Cotton Spread Collar Checked Casual Shirt": 4.0,
            "Combo of Men’s Casual Cotton Blend Shirt Long Sleeve Button Down with Spread Collar": 3.9,
            "NexaFlair Men's Shirt Regular Fit Solid Pattern Linen Cotton with Long Sleeve Collared Neck Standard Length and Button Down Closure Type Mens Casual Shirts Man's Formal Shirts": 3.2,
            "Lux Cozi Men's Half Sleeve Soild Casual Regular Fit T-Shirt with Chest Pocket Polo Tshirt for Men": 4.0,
            "Peter England Men's Snug Fit Solid Polo T-Shirt with Coloured Collar Tipping Cotton Rich Premium Pique Weave": 4.1,
            "U.S. Polo ASSN. Men's I688 Crew Neck Striped Lounge T-Shirt": 4.0,
            "Allen Solly Men’s Solid Polo T‑Shirt Regular Fit Premium Cotton Contrast Tipping Collar Smart Casual Wear": 4.1,
            "Jockey 2726 Men Super Combed Cotton Rich Solid V Neck Half Sleeve T-Shirt": 4.2,
            "Bacca Bucci Men Lace Up Basketball Shoe": 4.2,
            "Bacca Bucci Men Lace Up Running Shoes": 4.1,
            "Bacca Bucci Men Lace Up Athletic Shoes": 4.2,
            "Reebok Men's Running Shoes EVA Cushioned Breathable Mesh Sports Shoes for Men": 3.8,
            "Safari Pentagon Pro 8 Wheels Spinner Checkin Trolley Bag, Hard Case Polypropylene 360º Wheeling Luggage for Men & Women, Suitcase Bag": 4.1,
            "Safari Cabin Genius Alley rolley Bag Hard Case Polypropylene, 4 Spinner Wheels, 360 Degree Wheeling Carry on Luggage, Travel Bag, Suitcase for Travel, Trolley Bags for Travel": 4.1,
            "Provogue Spectrum Hard-Sided PP Trolley Bags for Travel Medium Size Expandable Luggage Suitcase with 8 Wheels Combination Lock": 4.0,
            "Boldfit Sneakers for Man Lightweight Shoes for Men Comfortable Sneakers for Men Air Mesh Casual Shoes Mens Soft Cushion Insole Lace Up Casual Boys Shoe Sneaker DripWave": 3.9,
            "Campus Men Oxyfit (N) Walking Shoes": 4.2,
            "WildHorn Genuine Leather Wallet for Men Slim Bifold Wallet with RFID Blocking Multiple Card Slots & Coin Pocket Premium Leather Mens Wallet": 4.2,
            "URBAN FOREST Zeus Vintage Leather Bi-Fold Wallet for Men": 4.1,
            "Tommy Hilfiger Men's Cuiaba Slimfold Wallet Leather with Liner Texture Ultra-Slim Minimalist Design Stylish Purse for Men": 3.0,
            "NAPA HIDE Leather Wallet for Men Handcrafted Credit/Debit Card Slots 2 Currency Compartments 2 Secret Compartments": 4.0,
            "TALED Genuine Leather Wallet - RFID Blocking Wallet for Men,12 Card Holder with Coin Pocket for Men with Gift Box, Nature Anthracite": 4.6,
            "Spiffy Genuine Leather Wallet for Men RFID Men Wallet, Slim Bifold Card Holder Wallet for Man with 12 Card Slots": 4.1,
            "Prang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric": 3.6,
            "SaintX eter England Men's Super Slim Fit Casual Trouser Chinos": 3.8,
            "MehMen's Regular Fit Formal Trousers Wrinkle Resistant Easy Care Stretchable Triple Blend Fabric Everyday Office & Business Wear Comfortable & Breathable Work Wear": 4.0,
            "Allen Solly Men s Formal Trousers,Premium Cotton Fabric,Comfy Fit for Office & Business Wear, Regular Fit": 3.7,
            "Samsung Galaxy M47 5G Powerful Snapdragon Processor Fast LPDDR5x RAM,UFS 3.1 Storage Gorilla Glass Victus+IP64 Super AMOLED Display 50MP OIS AI Gemini Live": 3.5,
            "Samsung Galaxy M17 5G Mobile 50MP OIS Triple Camera Gorilla Glass Victus IP54 6 Gen OS Upgrades AI Gemini Live Lag-Free Gaming Without Charger": 3.8,
            "Samsung Galaxy M36 5G Mobile Google Gemini Gorilla Glass Victus+ 7.7mm AI Enhanced 50MP OIS Triple Camera Nightography Lag-free Gaming Without Charger": 4.1,
            "Samsung Galaxy M17e 5G Mobile Smoothest 120 Hz Refresh Rate Monster 6000 mAh Battery IP54 6 Gen OS Upgrades AI Gemini Live Without Charger": 3.8,
            "OnePlus Nord CE6 Snapdragon 7s Gen 4 Segment's Fastest Touch Response 8000mAh Battery 144Hz 1.5K AMOLED Display 50MP Main + 32MP Selfie 4K Cameras IP66,68,69,69K": 4.3,
            "Bacca Bucci Men Lace Up Sneaker Shoes": 3.9,
            "Apple iPhone Air Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life": 4.5,
            "Apple iPhone 17 Pro Max 17.42 cm (6.9″) Display with Promotion, A19 Pro Chip, Best Battery Life in Any iPhone Ever, Pro Fusion Camera System, Center Stage Front Camera": 4.6,
            "Samsung Galaxy S25 Ultra 5G AI Smartphone 200MP Camera, S Pen Included, Long Battery Life": 4.4,
            "Samsung Galaxy S26 5G AI Phone, Photo Assist, Creative Studio, 50MP Camera with ProVisual Engine, Powerful Customized Processor and 4300mAh Battery": 4.4,
            "Samsung Galaxy Tab A11+ 27.82 cm (11 inch) Display 90Hz Refresh Rate, AI with Google Gemini, Dolby Atmos, Quad Speakers, Wi-Fi Tablet": 4.5,
            "Samsung Galaxy Tab S10 Lite with AI S Pen in-Box, 27.7 cm (10.9 Inch) Display, Object Eraser, 90Hz Refresh Rate, IP42 Rating, Wi-Fi Tablet": 4.6,
            "OnePlus Pad 4, Snapdragon® 8 Elite Gen 5 Platform, 33.53cm 13.2 3.4K Screen, 144Hz Adaptive, 8 Speakers, AI Powered, PC-Level Productivity, 13,380 mAh Battery,WiFi": 4.4,
            "OnePlus Pad 3 World's Fastest Snapdragon 8 Elite Processor, 13.2 3.4k Screen, 144Hz Adaptive Refresh Rate, 8 Speakers, AI, 12140 mAh Battery WiFi": 4.4,
            "Samsung Galaxy Tab S10 Plus S Pen in-Box, 31.5 cm (12.4 inch) Dynamic AMOLED 2X Display, Wi-Fi Tablet": 4.5,
            "ZEBRONICS Thunder Neo Wireless Headphone, BT v6.0, True 50hrs Playback, 40mm Driver, ENC, Rapid Charge, Gaming Mode, Dual Pairing, 3 EQ Modes, AUX, Voice Assistant": 3.9,
            "boAt Rockerz 480, RGB LEDs,6 Light Modes, 40mm Drivers,Beast Mode, 60H Battery, ENx Tech, Stream Ad Free Music via App Support, Bluetooth Headphones, Wireless Over Ear Headphone with Mic": 4.1,
            "boAt Rockerz 411, 40Ms Low Latency, 40Hrs Battery, 40Mm Drivers, ENx Tech, Stream Ad Free Music via App Support, Bluetooth Headphones, Wireless Over Ear Headphone with Mic": 4.2,
            "pTron Studio Pro w/ 65Hrs Playtime, Wireless Over Ear Headphones w/HD Mic, Dual Device Pairing, TruTalk AI-ENC Calls, Low-Latency Game & Music, 40mm Drivers, BT5.4, Type-C Fast Charging": 3.6,
            "Sony WH-CH520 Wireless Bluetooth Headphones On Ear with Mic, Up to 50Hrs Battery, Quick Charge, DSEE Upscale, Multipoint Connectivity, Voice Assistant": 4.2,
            "Portronics Muffs M2 Bluetooth Headphones Over Ear with Upto 40 Hrs Playtime, 40mm Dynamic Drivers, AUX 3.5mm, Powerful Bass, Laptop & PC Support,Type C Charging Port, Foldable Design": 4.0,
            "Noise Airwave Max 4 Wireless Over Ear Headphones with 70H Playtime, ENC, 40mm Driver, Low Latency(up to 40ms), Dual Pairing, BT v5.4": 3.7,
            "JBL Tune 770NC Wireless Over Ear Headphones with Adaptive Noise Cancellation, Upto 70H Battery, Smart Ambient, Speed Charge, Customized EQ, Google Fast Pair, Multipoint Connect, BT 5.3  Bluetooth, Adaptive Noise Cancellation, Detachable Sound Cable, Pure Bass Audio": 4.1,
            "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel": 4.1,
            "DELSEY PARIS Juliette Polycarbonate Hard Sided 8 Wheels and Expandable Spinner Suitcase Trolley Bag for Travel with TSA Lock": 3.6,
            "Nasher Miles Pondicherry Hard-Sided Polypropylene Check-in Luggage 28 inch 8 Wheels Large Trolley Bag for Travel Suitcase": 3.9,
            "boAt Airdopes 219, 4Mics ENx, 40H Battery, Best in Segment for Calling, Stream Ad Free Music via App Support, Bluetooth Earbuds, TWS Ear Buds Wireless Earphones with mic": 3.8,
            "realme Buds T310 True Wireless in-Ear Earbuds with 46dB Hybrid ANC, 360° Spatial Audio, 12.4mm Dynamic Bass Driver, Upto 40Hrs Battery and Fast Charging": 4.2,
            "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4": 4.0,
            "Noise Buds Trance in-Ear Truly Wireless Earbuds with 45H of Playtime, Voice Control, Low Latency(up to 40 ms), Instacharge(10 min=200 min), BT v5.3": 3.9,
            "boAt Airdopes Joy, 35Hrs Battery, Fast Charge, IWP Tech, Low Latency, 2Mic ENx, Type-C Port, v5.3 Bluetooth Earbuds, TWS Ear Buds Wireless Earphones with mic": 3.7,
            "realme Buds T500 Pro TWS Earbuds with 12.4mm Drivers, Upto 50dB ANC,3D Spatial Audio, 56H Playtime, AI ENC, IP55 Rating, and 45ms Low Latency BT 6.1": 4.1,
            "realme Buds Air 8,11mm+6mm Dual Dynamic Bass Drivers,58Hrs Playtime, 55dB ANC,6 Mic ENC, 45ms Low Latency, 360° Spatial Audio, Hi-Res LHDC, IP55 Dust & Water Resistant, BT v5.4": 4.2,
            "GOBOULT Z60 Made in India Ear Buds Wireless 60H Playtime, 4 ENC Mics Clear Calling, 50ms Low Latency Gaming, 13mm Bass Driver Earbuds Bluetooth Wireless Earphones": 3.8,
            "Peter England Men's Super Slim Fit Casual Trouser Chinos": 3.8,
            "Mehrang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric": 3.6,
            "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear": 4.0,
            "Samsung Galaxy M06 5G Mobile MediaTek Dimensity 6300 AnTuTu 623K+12 5G Bands 25W Fast Charging 4 Gen OS Upgrades 50MP Camera Without Charger": 3.6,
            "REDMI A7 Pro 5G Segment's Fastest Processor Segment's Largest Battery Segment's Largest & Smoothest 6.9in 120Hz Display": 3.4,
            "OnePlus Nord CE6 Lite Segment's Fastest Dimensity 7400 Apex Processor 7000mAh Battery  Segment's Highest 144Hz Refresh Rate 50MP Main Camera, 4K Video Recording": 4.4,
            "Sony WH-CH720N Active Noise Cancellation Wireless Bluetooth Over Ear Headphones with Mic, Adaptive Sound Control, Quick Charge, Up to 35Hrs Battery, Customized": 4.2,
            "Generic Wireless Bluetooth Headphones with Deep Bass, Foldable Design, Built-in Microphone, Adjustable Headband, Noise Isolation": 4.9,
            "OnePlus Pad Go 2, 2.8K 120Hz, WiFi Tablet, AI": 4.2,
            "Samsung Galaxy Tab A9 22.10 cm (8.7 inch) Display,Expandable, Wi-Fi+4G, Tablet": 4.1,
            "Redmi Pad 2 Pro 12000mAh Snapdragon 7s Gen 4 12.1-inch, 2.5K Display 83+ Days Standby HyperOS 2 120Hz Dolby Vision Atmos Wi-Fi 6 AI Powered": 4.0,
            "Redmi Pad 2 , Active Pen Support, 27.94cmModel, 2.5K Sharp & Clear Display,All Day & More 9000mAh Battery, AI-Enabled, Dolby Atmos, HyperOS 2": 3.7,
            "XIAOMI Pad 7 Nano Texture Display Snapdragon 7+ Gen 3 3.2K Display Tablet Wi-Fi Anti-Reflective Anti-Glare Hyperos 2 Dolby Vision Atmos": 4.1,
            "Apple iPad Air 27.59 cm Liquid Retina Display,12MP Front/Back Camera, Wi-Fi 7 with Apple N1, Touch ID, All-Day Battery Life": 4.6,
            "IndoPrimo Men's Cotton Shirt with Stylish Full Sleeves Spread Collared Neck Solid Pattern Western Style Classic Fit and Standard Length Casual Shirt for Man":4.0,
            "DEELMO Men's Regular Fit Button Down Dress Shirts Textured Long Sleeve Casual Hawaiian Shirt":4.0,
            "Lymio Polo T Shirt for Men T Shirt for Man Collar T Shirt Style Men":3.4,
            "London Hills Men's Cotton Regular Fit Printed Round Neck Full Sleeve T-Shirt":3.6,
            "Jump Cuts Mens Cotton Blend Polo Neck Half Sleeve T-Shirt":3.2,
            "Reebok Men's Running Shoes Lightweight Durable Sports Shoes for Men Lightweight Gym Shoe for Men Running, Jogging, Walking & Gym Flylite Lss Voyager":3.9,
            "Bacca Bucci Mens Ironman Running Shoes":3.7,
            "WOW IMAGINE Shock Proof Flip Cover Back Case Cover for Samsung Galaxy M17e 5G F70e 5G M07 F07 A07 A07 5G Flexible Leather Finish Card Pockets Wallet & Stand":3.8,
            "Pikkme Samsung Galaxy M32 4G M32 Prime F22 4G Flip Cover Leather Finish Inside TPU with Card Pockets Wallet Stand and Shock Proof Magnetic Closing Complete Protection Flip Case":4.1,
            "Solimo Mobile Cover for Apple iPhone 15 Plus Full Camera Protection Liquid Silicon Case  Flexible Bumper Case for Apple iPhone 15 Plus":4.1,
            "LIRAMARK Silicone Soft Back Cover Case for Apple iPhone 12 Mini":4.2,
            "Casotec Flip Cover Back Case for Apple iPhone 13 Pro Premium Leather Finish Inbuilt Pockets & Stand Flip Cover Back Case for Apple iPhone 13 Pro":3.9,
            "KACA Silicone Back Case for Apple iPhone 15, Soft-Touch, Shockproof Phone Back Cover for Apple iPhone 15":3.7,
            "AIBEX Back Cover for Apple iPhone 15 MagSafe Compatible with OStand Ring Kickstand Magnetic Metal Alloy Ring Wireless Charging Slim Thin Scratch Resistant Armor Shockproof Protective Case":3.9,
        }
        for product in queryset:
            title_clean = product.producttitle.strip()
            variants = Productview.objects.filter(category_id=product.category_id,producttitle__iexact=title_clean).order_by("productviewid")
            ordered_variants = [product] + [v for v in variants if v.productviewid != product.productviewid]
            variants_list = []
            for variant in ordered_variants:
                color = (variant.productcolor1 or "").strip()
                if not color:
                    continue
                variants_list.append({
                    "id": variant.productviewid,
                    "name": color,
                    "image": variant.productimage1,
                    "color_code": (get_clean_color_code(color) if callable(globals().get("get_clean_color_code"))
                        else ""
                    ),
                })
            product.color_variants = variants_list
            product.color_variant_count = len(variants_list)
            if "NexaFlair" in title_clean:
                raw_rating = 3.2
            elif "Combo of Men" in title_clean:
                raw_rating = 3.9
            else:
                raw_rating = float(ratings_map.get(title_clean, 5.0))
            product.rating = raw_rating
            full_stars = int(raw_rating)
            half_stars = 0 if raw_rating == 5.0 else (1 if (raw_rating - full_stars) > 0 else 0)
            product.full_stars_range = range(full_stars)
            product.half_stars_range = range(half_stars)
            product.empty_stars_range = range(max(0, 5 - full_stars - half_stars))
            if (
                product.productmrpprice
                and product.productprice
                and product.productmrpprice > product.productprice
            ):
                discount = ((product.productmrpprice - product.productprice) / product.productmrpprice) * 100
                product.productdiscountrate = str(int(discount))
            else:
                product.productdiscountrate = "0"
            days_to_add = 2 + (product.productviewid % 4)
            start_date = today + timedelta(days=days_to_add)
            if product.productviewid % 2 == 0:
                product.delivery_type = 'single'
                product.delivery_date = start_date
            else:
                product.delivery_type = 'range'
                end_date = start_date + timedelta(days=2)
                product.delivery_range = f"{start_date.strftime('%d')} - {end_date.strftime('%d %b')}"
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["categories"] = self.category
        page_title = getattr(self.category, 'categoryname', str(self.category))
        selected_brands = self.request.GET.getlist("brand")
        if selected_brands:
            if len(selected_brands) == 1:
                page_title = selected_brands[0]
            else:
                page_title = ", ".join(selected_brands)
        context["page_title"] = page_title
        base_category_qs = Productview.objects.filter(category_id=self.category)
        active_brand_qs = self.get_filtered_queryset()
        brands = [
            "Majestic Man",
            "U TURN",
            "Pinkmint",
            "MADHAVISTA",
            "NexaFlair",
            "Lux Cozi",
            "Peter England",
            "U.S. Polo ASSN",
            "Allen Solly",
            "Jockey",
            "Bacca Bucci",
            "Reebok",
            "Safari",
            "Provogue",
            "Boldfit",
            "Campus",
            "WildHorn",
            "URBAN FOREST",
            "Tommy Hilfiger",
            "NAPA HIDE",
            "TALED",
            "Spiffy",
            "Mehrang",
            "SaintX",
            "Samsung Galaxy M47 5G Powerful Snapdragon Processor Fast LPDDR5x RAM,UFS 3.1 Storage Gorilla Glass Victus+IP64 Super AMOLED Display 50MP OIS AI Gemini Live",
            "Samsung Galaxy M17 5G Mobile 50MP OIS Triple Camera Gorilla Glass Victus IP54 6 Gen OS Upgrades AI  Gemini Live Lag-Free Gaming Without Charger",
            "Samsung Galaxy M36 5G Mobile Google Gemini Gorilla Glass Victus+ 7.7mm AI Enhanced 50MP OIS Triple Camera Nightography Lag-free Gaming Without Charger",
            "Samsung Galaxy M17e 5G Mobile Smoothest 120 Hz Refresh Rate Monster 6000 mAh Battery IP54 6 Gen OS Upgrades AI Gemini Live Without Charger",
            "OnePlus Nord CE6 Snapdragon 7s Gen 4 Segment's Fastest Touch Response 8000mAh Battery 144Hz 1.5K AMOLED Display 50MP Main + 32MP Selfie 4K Cameras IP66,68,69,69K",
            "Apple iPhone Air Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life",
            "Apple iPhone 17 Pro Max 17.42 cm (6.9″) Display with Promotion, A19 Pro Chip, Best Battery Life in Any iPhone Ever, Pro Fusion Camera System, Center Stage Front Camera",
            "Samsung Galaxy S25 Ultra 5G AI Smartphone 200MP Camera, S Pen Included, Long Battery Life",
            "Samsung Galaxy S26 5G AI Phone, Photo Assist, Creative Studio, 50MP Camera with ProVisual Engine, Powerful Customized Processor and 4300mAh Battery",
            "Samsung Galaxy Tab A11+ 27.82 cm (11 inch) Display 90Hz Refresh Rate, AI with Google Gemini, Dolby Atmos, Quad Speakers, Wi-Fi Tablet",
            "Samsung Galaxy Tab S10 Lite with AI S Pen in-Box, 27.7 cm (10.9 Inch) Display, Object Eraser, 90Hz Refresh Rate, IP42 Rating, Wi-Fi Tablet",
            "OnePlus Pad 4, Snapdragon® 8 Elite Gen 5 Platform, 33.53cm 13.2 3.4K Screen, 144Hz Adaptive, 8 Speakers, AI Powered, PC-Level Productivity, 13,380 mAh Battery,WiFi",
            "OnePlus Pad 3 World's Fastest Snapdragon 8 Elite Processor, 13.2 3.4k Screen, 144Hz Adaptive Refresh Rate, 8 Speakers, AI, 12140 mAh Battery WiFi",
            "Samsung Galaxy Tab S10 Plus S Pen in-Box, 31.5 cm (12.4 inch) Dynamic AMOLED 2X Display, Wi-Fi Tablet",
            "Samsung Galaxy Tab S11 with AI, Hexagonal S-Pen in-Box, 27.8 cm (11 Inch) Dynamic AMOLED 2X Display, 120Hz Refresh Rate, Pre Loaded Pro Apps, Wi-Fi + 5G Tablet",
            "ZEBRONICS Thunder Neo Wireless Headphone, BT v6.0, True 50hrs Playback, 40mm Driver, ENC, Rapid Charge, Gaming Mode, Dual Pairing, 3 EQ Modes, AUX, Voice Assistant",
            "boAt Rockerz 480, RGB LEDs,6 Light Modes, 40mm Drivers,Beast Mode, 60H Battery, ENx Tech, Stream Ad Free Music via App Support, Bluetooth Headphones, Wireless Over Ear Headphone with Mic",
            "boAt Rockerz 411, 40Ms Low Latency, 40Hrs Battery, 40Mm Drivers, ENx Tech, Stream Ad Free Music via App Support, Bluetooth Headphones, Wireless Over Ear Headphone with Mic",
            "pTron Studio Pro w/ 65Hrs Playtime, Wireless Over Ear Headphones w/HD Mic, Dual Device Pairing, TruTalk AI-ENC Calls, Low-Latency Game & Music, 40mm Drivers, BT5.4, Type-C Fast Charging",
            "Sony WH-CH520 Wireless Bluetooth Headphones On Ear with Mic, Up to 50Hrs Battery, Quick Charge, DSEE Upscale, Multipoint Connectivity, Voice Assistant",
            "Portronics Muffs M2 Bluetooth Headphones Over Ear with Upto 40 Hrs Playtime, 40mm Dynamic Drivers, AUX 3.5mm, Powerful Bass, Laptop & PC Support,Type C Charging Port, Foldable Design",
            "Noise Airwave Max 4 Wireless Over Ear Headphones with 70H Playtime, ENC, 40mm Driver, Low Latency(up to 40ms), Dual Pairing, BT v5.4",
            "JBL Tune 770NC Wireless Over Ear Headphones with Adaptive Noise Cancellation, Upto 70H Battery, Smart Ambient, Speed Charge, Customized EQ, Google Fast Pair, Multipoint Connect, BT 5.3  Bluetooth, Adaptive Noise Cancellation, Detachable Sound Cable, Pure Bass Audio",
            "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel",
            "DELSEY PARIS Juliette Polycarbonate Hard Sided 8 Wheels and Expandable Spinner Suitcase Trolley Bag for Travel with TSA Lock",
            "Nasher Miles Pondicherry Hard-Sided Polypropylene Check-in Luggage 28 inch 8 Wheels Large Trolley Bag for Travel Suitcase",
            "boAt Airdopes 219, 4Mics ENx, 40H Battery, Best in Segment for Calling, Stream Ad Free Music via App Support, Bluetooth Earbuds, TWS Ear Buds Wireless Earphones with mic",
            "realme Buds T310 True Wireless in-Ear Earbuds with 46dB Hybrid ANC, 360° Spatial Audio, 12.4mm Dynamic Bass Driver, Upto 40Hrs Battery and Fast Charging",
            "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4",
            "Noise Buds Trance in-Ear Truly Wireless Earbuds with 45H of Playtime, Voice Control, Low Latency(up to 40 ms), Instacharge(10 min=200 min), BT v5.3",
            "boAt Airdopes Joy, 35Hrs Battery, Fast Charge, IWP Tech, Low Latency, 2Mic ENx, Type-C Port, v5.3 Bluetooth Earbuds, TWS Ear Buds Wireless Earphones with mic",
            "realme Buds T500 Pro TWS Earbuds with 12.4mm Drivers, Upto 50dB ANC,3D Spatial Audio, 56H Playtime, AI ENC, IP55 Rating, and 45ms Low Latency BT 6.1",
            "realme Buds Air 8,11mm+6mm Dual Dynamic Bass Drivers,58Hrs Playtime, 55dB ANC,6 Mic ENC, 45ms Low Latency, 360° Spatial Audio, Hi-Res LHDC, IP55 Dust & Water Resistant, BT v5.4",
            "GOBOULT Z60 Made in India Ear Buds Wireless 60H Playtime, 4 ENC Mics Clear Calling, 50ms Low Latency Gaming, 13mm Bass Driver Earbuds Bluetooth Wireless Earphones",
            "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear",
            "Samsung Galaxy M06 5G Mobile MediaTek Dimensity 6300 AnTuTu 623K+12 5G Bands 25W Fast Charging 4 Gen OS Upgrades 50MP Camera Without Charger",
            "REDMI A7 Pro 5G Segment's Fastest Processor Segment's Largest Battery Segment's Largest & Smoothest 6.9in 120Hz Display",
            "OnePlus Nord CE6 Lite Segment's Fastest Dimensity 7400 Apex Processor 7000mAh Battery  Segment's Highest 144Hz Refresh Rate 50MP Main Camera, 4K Video Recording",
            "Sony WH-CH720N Active Noise Cancellation Wireless Bluetooth Over Ear Headphones with Mic, Adaptive Sound Control, Quick Charge, Up to 35Hrs Battery, Customized",
            "Generic Wireless Bluetooth Headphones with Deep Bass, Foldable Design, Built-in Microphone, Adjustable Headband, Noise Isolation",
            "OnePlus Pad Go 2, 2.8K 120Hz, WiFi Tablet, AI",
            "Samsung Galaxy Tab A9 22.10 cm (8.7 inch) Display,Expandable, Wi-Fi+4G, Tablet",
            "Redmi Pad 2 Pro 12000mAh Snapdragon 7s Gen 4 12.1-inch, 2.5K Display 83+ Days Standby HyperOS 2 120Hz Dolby Vision Atmos Wi-Fi 6 AI Powered",
            "Redmi Pad 2 , Active Pen Support, 27.94cmModel, 2.5K Sharp & Clear Display,All Day & More 9000mAh Battery, AI-Enabled, Dolby Atmos, HyperOS 2",
            "XIAOMI Pad 7 Nano Texture Display Snapdragon 7+ Gen 3 3.2K Display Tablet Wi-Fi Anti-Reflective Anti-Glare Hyperos 2 Dolby Vision Atmos",
            "Apple iPad Air 27.59 cm Liquid Retina Display,12MP Front/Back Camera, Wi-Fi 7 with Apple N1, Touch ID, All-Day Battery Life",
            "IndoPrimo Men's Cotton Shirt with Stylish Full Sleeves Spread Collared Neck Solid Pattern Western Style Classic Fit and Standard Length Casual Shirt for Man",
            "DEELMO Men's Regular Fit Button Down Dress Shirts Textured Long Sleeve Casual Hawaiian Shirt",
            "Lymio Polo T Shirt for Men T Shirt for Man Collar T Shirt Style Men",
            "London Hills Men's Cotton Regular Fit Printed Round Neck Full Sleeve T-Shirt",
            "Jump Cuts Mens Cotton Blend Polo Neck Half Sleeve T-Shirt",
            "Reebok Men's Running Shoes Lightweight Durable Sports Shoes for Men Lightweight Gym Shoe for Men Running, Jogging, Walking & Gym Flylite Lss Voyager",
            "Bacca Bucci Mens Ironman Running Shoes",
            "WOW IMAGINE Shock Proof Flip Cover Back Case Cover for Samsung Galaxy M17e 5G F70e 5G M07 F07 A07 A07 5G Flexible Leather Finish Card Pockets Wallet & Stand",
            "Pikkme Samsung Galaxy M32 4G M32 Prime F22 4G Flip Cover Leather Finish Inside TPU with Card Pockets Wallet Stand and Shock Proof Magnetic Closing Complete Protection Flip Case",
            "Solimo Mobile Cover for Apple iPhone 15 Plus Full Camera Protection Liquid Silicon Case  Flexible Bumper Case for Apple iPhone 15 Plus",
            "LIRAMARK Silicone Soft Back Cover Case for Apple iPhone 12 Mini",
            "Casotec Flip Cover Back Case for Apple iPhone 13 Pro Premium Leather Finish Inbuilt Pockets & Stand Flip Cover Back Case for Apple iPhone 13 Pro",
            "KACA Silicone Back Case for Apple iPhone 15, Soft-Touch, Shockproof Phone Back Cover for Apple iPhone 15",
            "AIBEX Back Cover for Apple iPhone 15 MagSafe Compatible with OStand Ring Kickstand Magnetic Metal Alloy Ring Wireless Charging Slim Thin Scratch Resistant Armor Shockproof Protective Case",
        ]
        # brand_list 
        brand_list = []
        for brand in brands:
            titles = (base_category_qs.filter(Q(producttitle__icontains=brand) | Q(productname__icontains=brand)).values("producttitle").annotate(count=Count("productviewid")).order_by("producttitle"))
            for item in titles:
                brand_list.append({"name": item["producttitle"],"label": item["producttitle"],"count": item["count"],})
        context["brand_list"] = brand_list
        context["selected_brands"] = selected_brands
        # Narrow your search
        narrow_search_list = []
        for item in brand_list:
            title_name = item["label"]
            first_prod = base_category_qs.filter(producttitle=title_name).exclude(productimage1__isnull=True).exclude(productimage1="").first()
            img_url = first_prod.productimage1.url if (first_prod and hasattr(first_prod.productimage1, 'url')) else (first_prod.productimage1 if first_prod else None)
            narrow_search_list.append({"title": title_name,"image": img_url,"filter_val": title_name,})
        # Active filter
        narrow_filter = self.request.GET.get("narrow_filter")
        active_brand = None
        if selected_brands and selected_brands[0]:
            active_brand = selected_brands[0].strip().lower()
        elif narrow_filter:
            active_brand = narrow_filter.strip().lower()
        if active_brand:
            primary = []
            secondary = []
            for entry in narrow_search_list:
                t_lower = entry["title"].strip().lower()
                if active_brand in t_lower or t_lower in active_brand:
                    primary.append(entry)
                else:
                    secondary.append(entry)
            narrow_search_list = primary + secondary
        context["narrow_search_list"] = narrow_search_list
        # Size 
        size_list = []
        sizes = set()
        for product in active_brand_qs:
            for size in [product.productsize, product.productsize1, product.productsize2, product.productsize3]:
                if size:
                    sizes.add(size.strip())
        for size in sorted(sizes):
            count = active_brand_qs.filter(Q(productsize__iexact=size) | Q(productsize1__iexact=size) | Q(productsize2__iexact=size) | Q(productsize3__iexact=size)).count()
            size_list.append({"name": size, "count": count})
        context["size_list"] = size_list
        selected_sizes = self.request.GET.getlist("size")
        context["selected_sizes"] = selected_sizes
        context["selected_sizes_text"] = ", ".join(selected_sizes) if selected_sizes else ""
        # Price
        selected_price = self.request.GET.get("price", "")
        min_price = self.request.GET.get("min_price", "")
        max_price = self.request.GET.get("max_price", "")
        context["selected_price"] = selected_price
        context["min_price"] = min_price
        context["max_price"] = max_price
        if selected_price:
            context["selected_price_text"] = f"₹{selected_price}"
        elif min_price or max_price:
            context["selected_price_text"] = f"₹{min_price or '0'} - ₹{max_price or 'Max'}"
        else:
            context["selected_price_text"] = ""
        # Color
        color_values = (active_brand_qs.exclude(productcolor1__isnull=True).exclude(productcolor1="").values_list("productcolor1", flat=True).distinct())
        color_list = []
        for color in sorted(color_values):
            color_clean = color.strip()
            color_count = active_brand_qs.filter(productcolor1__iexact=color_clean).count()
            if color_count > 0:
                color_list.append({
                    "name": color_clean,
                    "count": color_count,
                    "color_code": get_clean_color_code(color_clean) if callable(globals().get("get_clean_color_code")) else "",
                })
        context["color_list"] = color_list
        selected_colors = self.request.GET.getlist("color")
        context["selected_colors"] = selected_colors
        context["selected_colors_text"] = ", ".join(selected_colors) if selected_colors else ""
        context["excluded_categories"] = ['wallet', 'headphone', 'earbuds', 'mobile cover']
        return context
def get_styling_ideas(product, limit=9):
    current_category = (product.category_id.categoryname or "").strip().lower()
    category_rules = {
        "shirt": [["pant", "trouser", "jeans"],["shoe", "footwear", "sneaker"],["wallet", "belt"],],
        "tshirt": [["pant", "trouser", "jeans"],["shoe", "footwear", "sneaker"],["wallet", "belt"],],
        "trouser": [["shirt", "tshirt", "t-shirt"],["shoe", "footwear", "sneaker"],["wallet", "belt"],],
        "shoes": [["shirt", "tshirt", "t-shirt"],["pant", "trouser", "jeans"],["wallet", "belt"],],
        "wallet": [["pant", "trouser", "jeans"],["shirt", "tshirt", "t-shirt"],["shoe", "footwear", "sneaker"],],
    }
    selected_rule = category_rules.get(current_category,[["shirt", "tshirt", "t-shirt"],["pant", "trouser", "jeans"],["shoe", "footwear", "sneaker"],],)
    outfits = [] 
    used_product_ids = {product.productviewid}
    for outfit_idx in range(4):
        current_outfit = []
        for category_keywords in selected_rule:
            category_q = Q()
            for keyword in category_keywords:
                category_q |= Q(categoryname__icontains=keyword)
            candidates = (Productview.objects.filter(category_id__in=Category.objects.filter(category_q),in_stock=True,).exclude(productviewid__in=used_product_ids).exclude(productimage1__isnull=True).exclude(productimage1="").select_related("category_id").order_by("?"))
            selected_item = candidates.first()
            if selected_item:
                apply_rating(selected_item)
                variant_count = (Productview.objects.filter(producttitle=selected_item.producttitle, in_stock=True).exclude(productviewid=selected_item.productviewid).count())
                current_outfit.append(
                    {
                        "product_id": selected_item.productviewid,
                        "category_id": selected_item.category_id.categoryid,
                        "title": selected_item.producttitle,
                        "brand": selected_item.productname,
                        "image": selected_item.productimage1,
                        "price": selected_item.productprice,
                        "mrp": selected_item.productmrpprice,
                        "discount": selected_item.productdiscountrate,
                        "rating": selected_item.rating,
                        "full_stars_range": list(selected_item.full_stars_range),
                        "half_stars_range": list(selected_item.half_stars_range),
                        "empty_stars_range": list(selected_item.empty_stars_range),
                        "color_count": variant_count + 1,
                    }
                )
                used_product_ids.add(selected_item.productviewid)
        if len(current_outfit) == 3:
            outfits.append({"look_name": f"Look {outfit_idx + 1}","products": current_outfit,})
    return outfits
class ProductDetailView(DetailView):
    model = Productview
    template_name = "productview.html"
    context_object_name = "productview"
    pk_url_kwarg = "productviewid"
    def get_object(self, queryset=None):
        return get_object_or_404(Productview.objects.select_related("category_id"),productviewid=self.kwargs["productviewid"],category_id=self.kwargs["categoryid"],)
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # recently viewed
        product = self.object
        recently_viewed = request.session.get("recently_viewed", [])
        p_id = product.productviewid
        if p_id in recently_viewed:
            recently_viewed.remove(p_id)
        recently_viewed.insert(0, p_id)
        request.session["recently_viewed"] = recently_viewed[:10]  
        request.session.modified = True
        return response
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        product = self.object
        if not request.user.is_authenticated:
            return redirect("login")
        rating = request.POST.get("rating") or request.POST.get("rate")
        review_text = request.POST.get("review") or request.POST.get("comment") or request.POST.get("description")
        country = request.POST.get("country")  
        size = request.POST.get("size")
        color = request.POST.get("color")
        image = request.FILES.get("image") or request.FILES.get("review_image")
        if rating and review_text:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                country=country,
                review=review_text,
                size=size,
                color=color,
                image=image if image else None
            )
            messages.success(request, "Your review has been submitted successfully.")
        else:
            messages.error(request, "Please provide both rating and review text.")
        return redirect(request.path)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        # HELPER FUNCTIONS
        def clean_str(val):
            if not val:
                return ""
            s = str(val).replace("+", " ").strip().lower()
            return " ".join(s.split())
        def is_variant_unavailable(variant_obj, selected_size):
            title = clean_str(variant_obj.producttitle)
            color = clean_str(variant_obj.productcolor1)
            size = clean_str(selected_size)
            if "samsung galaxy tab a9" in title and color == "silver":
                return True
            if "redmi pad 2" in title and size in ["8gb 128gb", "8gb + 128gb"]:
                return True
            if "apple ipad air" in title and size in ["512gb","1tb","512 gb","1 tb",]:
                return True
            if hasattr(variant_obj, "stock") and variant_obj.stock <= 0:
                return True
            return False
        def get_variant_price_details(variant_obj, target_size_clean):
            size_slots = [
                (variant_obj.productsize, variant_obj.productprice, variant_obj.productmrpprice),
                (variant_obj.productsize1, variant_obj.productprice1, variant_obj.productmrpprice1),
                (variant_obj.productsize2, variant_obj.productprice2, variant_obj.productmrpprice2),
                (variant_obj.productsize3, variant_obj.productprice3, variant_obj.productmrpprice3),
            ]
            if target_size_clean:
                for raw_size, price, mrp in size_slots:
                    if raw_size and clean_str(raw_size) == target_size_clean:
                        final_price = (price if price is not None else variant_obj.productprice)
                        final_mrp = (mrp if mrp is not None else variant_obj.productmrpprice)
                        return (
                            final_price,
                            final_mrp,
                            str(raw_size).strip(),
                        )
            return (variant_obj.productprice, variant_obj.productmrpprice, (variant_obj.productsize or "").strip())
        def calculate_discount_rate(price, mrp):
            if mrp and price and mrp > price and mrp > 0:
                return str(int(((mrp - price) / mrp) * 100))
            return "0"
        # PRICE 
        raw_size = self.request.GET.get("size", "")
        selected_size = (
            urllib.parse.unquote(raw_size).strip()
            if raw_size
            else (product.productsize or "").strip()
        )
        sel_size_clean = clean_str(selected_size)
        (
            current_price,
            current_mrp,
            active_selected_size,
        ) = get_variant_price_details(product, sel_size_clean)
        context["selected_size"] = active_selected_size
        context["current_price"] = current_price
        context["current_mrp"] = current_mrp
        context["current_discount"] = calculate_discount_rate(current_price, current_mrp)
        raw_sizes = [product.productsize, product.productsize1, product.productsize2, product.productsize3]
        excluded_sizes = ["85 cm", "none", "", None]
        context["sizes_list"] = [
            s.strip()
            for s in raw_sizes
            if s and str(s).strip().lower() not in excluded_sizes
        ]
        variant_unavailable = is_variant_unavailable(product, selected_size)
        context["variant_unavailable"] = variant_unavailable
        # COLOR 
        all_color_variants = (Productview.objects.filter(producttitle__iexact=product.producttitle).select_related("category_id").order_by("productviewid"))
        color_variants_list = []
        added_colors = set()
        for variant in all_color_variants:
            color = str(variant.productcolor1 or "").strip()
            if not color:
                continue
            color_key = clean_str(color)
            if color_key in added_colors:
                continue
            added_colors.add(color_key)
            var_price, var_mrp, active_size_label = get_variant_price_details(variant, sel_size_clean)
            color_variant_unavailable = is_variant_unavailable(variant, selected_size)
            disc_rate = calculate_discount_rate(var_price, var_mrp)
            color_code = (
                get_clean_color_code(color)
                if "get_clean_color_code" in globals()
                else ""
            )
            color_variants_list.append(
                {
                    "id": variant.productviewid,
                    "name": color,
                    "image": variant.productimage1,
                    "display_price": var_price,
                    "display_mrp": var_mrp,
                    "display_size": active_size_label,
                    "display_discount": disc_rate,
                    "discount_rate": disc_rate,
                    "category_id": (
                        variant.category_id.categoryid
                        if variant.category_id
                        else variant.category_id_id
                    ),
                    "color_code": color_code,
                    "unavailable": color_variant_unavailable,
                }
            )
        context["color_variants"] = color_variants_list
        context["ref_page"] = self.request.GET.get("ref_page", 1)
        context["stock_quantity"] = product.stock
        context["stock_available"] = product.stock > 0 and not variant_unavailable
        if "apply_rating" in globals():
            apply_rating(product)
        # FEATURED PRODUCT
        featured_prod = (Productview.objects.filter(category_id=product.category_id, in_stock=True).exclude(productimage1__isnull=True).exclude(productimage1="").exclude(productviewid=product.productviewid).order_by("?").first())
        if featured_prod:
            var_price, var_mrp, active_size_label = get_variant_price_details(featured_prod, sel_size_clean)
            featured_prod.display_price = var_price
            featured_prod.display_mrp = var_mrp
            featured_prod.display_discount = calculate_discount_rate(var_price, var_mrp)
        context["category_featured_product"] = featured_prod
        # BANNERS
        home_banner = (Productview.objects.filter(in_stock=True).exclude(productimage1__isnull=True).exclude(productimage1="").order_by("?").first())
        if not home_banner:
            home_banner = product
        if "apply_rating" in globals():
            apply_rating(home_banner)
        context["home_banner"] = home_banner
        # SIMILAR PRODUCTS
        similar_products = list(Productview.objects.filter(category_id=product.category_id,producttitle__iexact=product.producttitle,in_stock=True,).exclude(productviewid=product.productviewid).order_by("-productviewid")[:22])
        for p in similar_products:
            if "apply_rating" in globals():
                apply_rating(p)
            var_price, var_mrp, active_size_label = get_variant_price_details(p, sel_size_clean)
            p.display_price = var_price
            p.display_mrp = var_mrp
            p.display_size = active_size_label
            p.display_discount = calculate_discount_rate(var_price, var_mrp)
            p.is_unavailable = is_variant_unavailable(p, selected_size)
            sim_variants = Productview.objects.filter(category_id=p.category_id,producttitle__iexact=p.producttitle,in_stock=True,).order_by("productviewid")
            ordered_sim_variants = [p] + [v for v in sim_variants if v.productviewid != p.productviewid]
            variants_list = []
            used_colors = set()
            for variant in ordered_sim_variants:
                color = (variant.productcolor1 or "").strip()
                if not color or color.lower() in used_colors:
                    continue
                used_colors.add(color.lower())
                color_code = (get_clean_color_code(color) if callable(globals().get("get_clean_color_code")) else "")
                var_unavail = is_variant_unavailable(variant, selected_size)
                img_url = (variant.productimage1.url if hasattr(variant.productimage1, "url") else variant.productimage1)
                v_price, v_mrp, _ = get_variant_price_details(variant, sel_size_clean)
                variants_list.append(
                    {
                        "id": variant.productviewid,
                        "name": color,
                        "image": img_url,
                        "price": v_price,
                        "mrp": v_mrp,
                        "color_code": color_code,
                        "unavailable": var_unavail,
                        "is_selected": variant.productviewid == p.productviewid,
                    }
                )
            p.color_variants = variants_list
        context["similar_products"] = similar_products
        if "get_styling_ideas" in globals():
            context["styling_ideas"] = get_styling_ideas(product, limit=3)
        context["category"] = Category.objects.all()
        context["categories"] = get_object_or_404(Category, categoryid=self.kwargs["categoryid"])
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=5)
        context["last_order"] = None
        if self.request.user.is_authenticated:
            context["last_order"] = (Order.objects.filter(user_id=self.request.user).order_by("-date").first())
        # COLOR PAGINATOR
        variants_qs = (
            Productview.objects.filter(producttitle__iexact=product.producttitle)
            .annotate(
                is_current=Case(
                    When(productviewid=product.productviewid, then=Value(0)),
                    default=Value(1),
                    output_field=IntegerField(),
                )
            )
            .order_by("is_current", "productviewid")
        )
        paginator = Paginator(variants_qs, 10)
        page_number = self.request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)
        
        for item in page_obj:
            var_price, var_mrp, active_size_label = get_variant_price_details(item, sel_size_clean)
            item.display_price = var_price
            item.display_mrp = var_mrp
            item.display_size = active_size_label
            item.display_discount = calculate_discount_rate(var_price, var_mrp)
            item.variant_unavailable = is_variant_unavailable(item, selected_size)
        context["page_obj"] = page_obj
        context["same_product_count"] = variants_qs.count()
        similar_variant_ids = Productview.objects.filter(producttitle__iexact=product.producttitle).values_list('productviewid', flat=True)
        reviews = list(Review.objects.filter(product_id__in=similar_variant_ids).select_related("user").order_by("-created_at")[:7])
        verified_user_ids = set()
        if reviews:
            review_user_ids = [r.user.id for r in reviews if r.user_id]
            if review_user_ids:
                try:
                    verified_user_ids = set(Orderitem.objects.filter(order_id__orderstatus="Delivered",productview_id__in=similar_variant_ids,order_id__user_id__in=review_user_ids).values_list("order_id__user_id", flat=True))
                except Exception:
                    try:
                        verified_user_ids = set(Orderitem.objects.filter(order__orderstatus="Delivered",productview_id__in=similar_variant_ids,order__user__in=review_user_ids).values_list("order__user_id", flat=True))
                    except Exception:
                        pass
        for review in reviews:
            review.verified_purchase = (review.user_id in verified_user_ids if review.user else False)
        context["reviews"] = reviews
        context["all_reviews_count"] = Review.objects.filter(product_id__in=similar_variant_ids).count()
        return context
@login_required
def add_review_view(request, productviewid):
    product = get_object_or_404(Productview, productviewid=productviewid)
    if request.method == 'POST':
        rating = request.POST.get("rating")
        review_text = request.POST.get("review")
        size = request.POST.get("size")
        color = request.POST.get("color")
        country = request.POST.get("country")
        image = request.FILES.get("image")
        if rating and review_text:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                review=review_text,
                size=size,
                color=color,
                country=country,
                image=image if image else None
            )
            messages.success(request, "Your review has been submitted successfully.")
            return redirect('productview', categoryid=product.category_id.categoryid, productviewid=product.productviewid)
        else:
            messages.error(request, "Please provide both rating and review text.")
    context = {'productview': product}
    return render(request, 'add_review.html', context)
class DeleteReviewView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, reviewid):
        review = get_object_or_404(Review, reviewid=reviewid)
        if review.user == request.user:
            review.delete()
            messages.success(request, "Your review has been deleted successfully.")
        else:
            messages.error(request, "You can only delete your own review.")
        return redirect(request.META.get("HTTP_REFERER", "/"))
class ProfileView(DetailView):
    model = User
    template_name = "profile.html"
    context_object_name = "profile_user"
    pk_url_kwarg = "user_id"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["productview"] = get_object_or_404(Productview,productviewid=self.kwargs["productviewid"])
        context["categories"] = context["productview"].category_id
        context["reviews"] = (Review.objects.filter(user=self.object).select_related("user", "product").order_by("-created_at"))
        return context
class CustomerReviewView(DetailView):
    model = Productview
    template_name = "customer_review.html"
    context_object_name = "productview"
    pk_url_kwarg = "productviewid"
    def get_object(self):
        return get_object_or_404(Productview,productviewid=self.kwargs["productviewid"])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["categories"] = get_object_or_404(Category,categoryid=self.kwargs["categoryid"])
        context["reviews"] = (
            Review.objects.filter(product=self.object).select_related("user").order_by("-created_at"))
        return context
class ApplyCouponView(View):
    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, "Please login first.")
            return redirect("login")
        cart_items = Cart.objects.filter(userid=request.user)
        if not cart_items.exists():
            messages.error(request,"Please add items to cart first.")
            return redirect("cart")
        code = request.POST.get("coupon", "").strip().upper()
        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            messages.error(request,"Invalid coupon code.")
            return redirect("cart")
        if not coupon.is_valid():
            messages.error(request,"Coupon has expired.")
            return redirect("cart")
        if CouponUsage.objects.filter(coupon=coupon,user=request.user).exists():
            messages.error(request,"You have already used this coupon.")
            return redirect("cart")
        subtotal = 0
        for item in cart_items:
            subtotal += item.subtotal()
        if subtotal < coupon.minimum_amount:
            messages.error(request,f"Minimum order should be ₹{coupon.minimum_amount}")
            return redirect("cart")
        discount = subtotal * coupon.discount // 100
        request.session["coupon_code"] = coupon.code
        request.session["coupon_discount"] = discount
        messages.success(request,f"Coupon '{coupon.code}' applied successfully.")
        return redirect("cart")
class RemoveCouponView(View):
    def get(self, request):
        request.session.pop("coupon_code", None)
        request.session.pop("coupon_discount", None)
        messages.success(request, "Coupon removed successfully.")
        return redirect("cart")
class CartView(TemplateView):
    template_name = "cart.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        subtotal = 0
        discount = 0
        deliverycharge = 0
        if self.request.user.is_authenticated:
            cartdata = Cart.objects.filter(userid=self.request.user).select_related("product_id").order_by("-cartid")
        else:
            cartdata = Cart.objects.none()
        for item in cartdata:
            product = item.product_id
            if product:
                selected_size = str(getattr(item, "selected_size", "") or "").strip().lower()
                unit_price = product.productprice
                mrp_price = product.productmrpprice
                if hasattr(item, "product_price") and item.product_price:
                    unit_price = item.product_price
                elif selected_size:
                    s0 = str(product.productsize or "").strip().lower()
                    s1 = str(product.productsize1 or "").strip().lower()
                    s2 = str(product.productsize2 or "").strip().lower()
                    s3 = str(product.productsize3 or "").strip().lower()
                    if selected_size == s1:
                        unit_price = product.productprice1 or product.productprice
                        mrp_price = product.productmrpprice1 or product.productmrpprice
                    elif selected_size == s2:
                        unit_price = product.productprice2 or product.productprice
                        mrp_price = product.productmrpprice2 or product.productmrpprice
                    elif selected_size == s3:
                        unit_price = product.productprice3 or product.productprice
                        mrp_price = product.productmrpprice3 or product.productmrpprice
                    elif selected_size == s0:
                        unit_price = product.productprice
                        mrp_price = product.productmrpprice
                item.calculated_price = unit_price
                item.calculated_mrp = mrp_price
                item.calculated_subtotal = unit_price * item.quantity
                subtotal += item.calculated_subtotal
            else:
                subtotal += item.subtotal() if hasattr(item, "subtotal") else 0
        deliverycharge = 30 if 0 < subtotal < 300 else 0
        if self.request.user.is_authenticated:
            coupon_code = self.request.session.get("coupon_code", "")
            discount = self.request.session.get("coupon_discount", 0)
        else:
            coupon_code = ""
        total = subtotal - discount + deliverycharge
        if cartdata.exists() and cartdata[0].product_id:
            first_product = cartdata[0].product_id
            context["producttitle"] = first_product.producttitle
            if first_product.category_id:
                context["category_name"] = first_product.category_id.categoryname
                context["category_id"] = first_product.category_id.categoryid
        context["cartdata"] = cartdata
        context["subtotal"] = subtotal
        context["discount"] = discount
        context["deliverycharge"] = deliverycharge
        context["total"] = total
        context["coupon_code"] = coupon_code
        context["coupons"] = Coupon.objects.filter(active=True)
        return context
class AddToCartView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, productviewid):
        product = get_object_or_404(Productview, productviewid=productviewid)
        raw_size = (
            request.POST.get("selected_size")
            or request.GET.get("size")
            or ""
        )
        selected_size = raw_size.strip()
        sizes = [
            product.productsize,
            product.productsize1,
            product.productsize2,
            product.productsize3,
        ]
        valid_sizes = [
            size.strip()
            for size in sizes
            if size
            and size.strip()
            and size.strip().lower() not in ["none", "85 cm", "standard"]
        ]
        if valid_sizes:
            if (
                not selected_size
                or selected_size.lower() in ["none", "85 cm", "standard"]
            ):
                selected_size = valid_sizes[0]
        else:
            selected_size = ""
        if not product.in_stock or product.stock < 1:
            messages.error(request, f"Sorry, '{product.productname}' is currently out of stock!")
            return redirect(request.META.get("HTTP_REFERER", "/"))
        selected_price = product.productprice
        if selected_size:
            s_clean = selected_size.lower().strip()
            if product.productsize and product.productsize.lower().strip() == s_clean:
                selected_price = product.productprice
            elif product.productsize1 and product.productsize1.lower().strip() == s_clean:
                selected_price = getattr(product, "productprice1", product.productprice) or product.productprice
            elif product.productsize2 and product.productsize2.lower().strip() == s_clean:
                selected_price = getattr(product, "productprice2", product.productprice) or product.productprice
            elif product.productsize3 and product.productsize3.lower().strip() == s_clean:
                selected_price = getattr(product, "productprice3", product.productprice) or product.productprice
        cart_item = Cart.objects.filter(userid=request.user,product_id=product,selected_size=selected_size).first()
        if cart_item:
            cart_item.quantity += 1
            if hasattr(cart_item, "product_price"):
                cart_item.product_price = selected_price
                cart_item.save(update_fields=["quantity", "product_price"])
            else:
                cart_item.save(update_fields=["quantity"])
            if selected_size:
                messages.success(request, f"'{product.producttitle}' ({selected_size}) in your cart.")
            else:
                messages.success(request, f"'{product.producttitle}' in your cart.")
        else:
            cart_kwargs = {
                "userid": request.user,
                "product_id": product,
                "quantity": 1,
                "selected_size": selected_size
            }
            if hasattr(Cart, "product_price"):
                cart_kwargs["product_price"] = selected_price 
            Cart.objects.create(**cart_kwargs)
            if selected_size:
                messages.success(request, f"'{product.producttitle}' ({selected_size}) added to your cart.")
            else:
                messages.success(request, f"'{product.producttitle}' added to your cart.")
        return redirect("cart")
class RemoveCartView(LoginRequiredMixin,View):
    login_url = "login"
    def post(self, request, cartid):
        cart_item = get_object_or_404(Cart, cartid=cartid)
        if cart_item.userid == request.user:
            cart_item.delete()
            messages.success(request, f"item has been removed from your cart.")
        else:
            messages.error(request, "Sorry, you don't have permission to remove this item.")
        return redirect("cart")
    def get(self, request, cartid):
        return redirect("cart")
class PlusCartView(LoginRequiredMixin,View):
    login_url = "login"
    def post(self, request, cartid):
        cart_item = get_object_or_404(Cart,cartid=cartid,userid=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect("cart")
    def get(self, request, cartid):
        return redirect("cart")
class MinusCartView(LoginRequiredMixin,View):
    login_url = "login"
    def post(self, request, cartid):
        cart_item = get_object_or_404(Cart,cartid=cartid,userid=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            messages.warning(request,"Quantity cannot be less than 1.")
        return redirect("cart")
    def get(self, request, cartid):
        return redirect("cart")
class CheckoutView(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "checkout.html"
    def get(self, request):
        category = Category.objects.all()
        cartdata = Cart.objects.filter(userid=request.user).select_related("product_id").order_by("-cartid")
        if not cartdata.exists():
            messages.warning(request, "Your cart is empty! Please add products first.")
            return redirect("cart")
        subtotal = 0
        for item in cartdata:
            product = item.product_id
            if product:
                selected_size = str(getattr(item, "selected_size", "") or "").strip().lower()
                unit_price = product.productprice
                mrp_price = product.productmrpprice
                if hasattr(item, "product_price") and item.product_price:
                    unit_price = item.product_price
                elif selected_size:
                    s0 = str(product.productsize or "").strip().lower()
                    s1 = str(product.productsize1 or "").strip().lower()
                    s2 = str(product.productsize2 or "").strip().lower()
                    s3 = str(product.productsize3 or "").strip().lower()
                    if selected_size == s1:
                        unit_price = product.productprice1 or product.productprice
                        mrp_price = product.productmrpprice1 or product.productmrpprice
                    elif selected_size == s2:
                        unit_price = product.productprice2 or product.productprice
                        mrp_price = product.productmrpprice2 or product.productmrpprice
                    elif selected_size == s3:
                        unit_price = product.productprice3 or product.productprice
                        mrp_price = product.productmrpprice3 or product.productmrpprice
                    elif selected_size == s0:
                        unit_price = product.productprice
                        mrp_price = product.productmrpprice
                item.calculated_price = unit_price
                item.calculated_mrp = mrp_price
                item.calculated_subtotal = unit_price * item.quantity
                subtotal += item.calculated_subtotal
            else:
                subtotal += item.subtotal() if hasattr(item, "subtotal") else 0
        deliverycharge = 30 if 0 < subtotal < 300 else 0
        coupon_code = request.session.get("coupon_code", "")
        discount = request.session.get("coupon_discount", 0)
        total = subtotal - discount + deliverycharge
        if total < 0:
            total = 0
        category_name = None
        producttitle = None
        category_id = None
        first_item = cartdata.first()
        if first_item and first_item.product_id:
            producttitle = first_item.product_id.producttitle
            if first_item.product_id.category_id:
                category_name = first_item.product_id.category_id.categoryname
                category_id = first_item.product_id.category_id.categoryid
        last_order = Order.objects.filter(user_id=request.user).order_by("-orderid").first()
        context = {
            "category": category,
            "cartdata": cartdata,
            "subtotal": subtotal,
            "deliverycharge": deliverycharge,
            "discount": discount,
            "coupon_code": coupon_code,
            "total": total,
            "last_order": last_order,
            "category_name": category_name,
            "producttitle": producttitle,
            "category_id": category_id,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        cartdata = Cart.objects.filter(userid=request.user).select_related("product_id").order_by("-cartid")
        if not cartdata.exists():
            messages.warning(request, "Your cart is empty!")
            return redirect("cart")
        subtotal = 0
        for item in cartdata:
            product = item.product_id
            if product:
                selected_size = str(getattr(item, "selected_size", "") or "").strip().lower()
                unit_price = product.productprice
                if hasattr(item, "product_price") and item.product_price:
                    unit_price = item.product_price
                elif selected_size:
                    s0 = str(product.productsize or "").strip().lower()
                    s1 = str(product.productsize1 or "").strip().lower()
                    s2 = str(product.productsize2 or "").strip().lower()
                    s3 = str(product.productsize3 or "").strip().lower()
                    if selected_size == s1:
                        unit_price = product.productprice1 or product.productprice
                    elif selected_size == s2:
                        unit_price = product.productprice2 or product.productprice
                    elif selected_size == s3:
                        unit_price = product.productprice3 or product.productprice
                    elif selected_size == s0:
                        unit_price = product.productprice
                subtotal += unit_price * item.quantity
            else:
                subtotal += item.subtotal() if hasattr(item, "subtotal") else 0    
        deliverycharge = 30 if 0 < subtotal < 300 else 0
        coupon_code = request.session.get("coupon_code", "")
        discount = request.session.get("coupon_discount", 0)
        coupon = None
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
            except Coupon.DoesNotExist:
                coupon = None
        total = subtotal - discount + deliverycharge
        if total < 0:
            total = 0
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        number = request.POST.get("number")
        address = request.POST.get("address")
        paymentmethod = request.POST.get("paymentmethod")
        tracker_status = Otracker.objects.filter(status="conformorder", myuser=request.user).first()
        if not tracker_status:
            tracker_status = Otracker.objects.create(status="conformorder", myuser=request.user)
        try:
            order = Order.objects.create(
                orderstatus="Pending",
                otracker_id=tracker_status,
                user_id=request.user,
                firstname=firstname,
                lastname=lastname,
                email=email,
                number=number,
                username=request.user.username,
                address=address,
                subtotal=subtotal,
                deliverycharges=deliverycharge,
                total=total,
                paymentmethod=paymentmethod,
                coupon=coupon,
                coupon_discount=discount,
            )
            for item in cartdata:
                Orderitem.objects.create(
                    status="Pending",
                    productview_id=item.product_id,
                    order_id=order,
                    quantity=item.quantity,
                    selected_size=item.selected_size,
                )
                product = item.product_id
                if product:
                    product.sold_count += item.quantity  
                    product.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            if address:
                profile.delivery_address = address
            if number:
                profile.mobile = number
            profile.save()
            cartdata.delete()
            request.session["order_just_placed_id"] = order.orderid
            messages.info(request, "Please review your order details before placing the order.")
            return redirect("conformorder", order.orderid)
        except Exception as e:
            import traceback
            traceback.print_exc()
            messages.error(request, str(e))
            return redirect("checkout")
class ConfirmOrderView(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "conformorder.html"
    def get(self, request, orderid):
        order = get_object_or_404(Order, orderid=orderid, user_id=request.user)
        pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
        if order.orderstatus == "Cancelled":
            order.payment_status_display = "Cancelled"
        elif "COD" in pm or "CASH" in pm:
            order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
        else:
            order.payment_status_display = order.paymentstatus or "Paid"  
        order_items = Orderitem.objects.filter(order_id=order)
        running_total = 0
        for item in order_items:
            unit_price = item.productview_id.productprice  
            if hasattr(item, 'selected_size') and item.selected_size:
                size_clean = str(item.selected_size).strip().lower()
                prod = item.productview_id
                if prod.productsize and prod.productsize.strip().lower() == size_clean:
                    unit_price = prod.productprice
                elif prod.productsize1 and prod.productsize1.strip().lower() == size_clean:
                    unit_price = prod.productprice1 or prod.productprice
                elif prod.productsize2 and prod.productsize2.strip().lower() == size_clean:
                    unit_price = prod.productprice2 or prod.productprice
                elif prod.productsize3 and prod.productsize3.strip().lower() == size_clean:
                    unit_price = prod.productprice3 or prod.productprice 
            item.calculated_unit_price = unit_price
            item.calculated_subtotal = unit_price * item.quantity
            running_total += item.calculated_subtotal 
        if order.coupon:
            coupon_code = order.coupon.code
            discount = order.coupon_discount
            final_total = running_total - discount
        else:
            coupon_code = ""
            discount = 0
            final_total = running_total
        order.calculated_total = final_total
        user_order_no = Order.objects.filter(user_id=request.user, orderid__lte=order.orderid).count()
        order.amazon_order_id = f"{user_order_no:05d}"
        expected_delivery = order.date + timedelta(days=5)
        first_item = order_items.first()
        context = {
            "order": order,
            "cart_items": order_items,
            "is_checkout": request.session.get("order_just_placed_id") == order.orderid,
            "expected_delivery": expected_delivery,
            "productview": first_item.productview_id if first_item else None,
            "categories": first_item.productview_id.category_id if first_item else None,
            "coupon_code": coupon_code,
            "discount": discount,
            "subtotal": running_total,
        }
        return render(request, self.template_name, context)
class PlaceOrderView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request):
        order_id = request.session.get("order_just_placed_id")
        if not order_id:
            messages.error(request, "No order found.")
            return redirect("cart")
        order = get_object_or_404(Order, orderid=order_id, user_id=request.user)
        if order.orderstatus and order.orderstatus != "Pending":
            Cart.objects.filter(userid_id=request.user.id).delete()
            request.session.pop("coupon_code", None)
            request.session.pop("coupon_discount", None)
            request.session.pop("order_just_placed_id", None)
            return redirect("thankyou", order.orderid)
        is_pending = (order.orderstatus == "Pending" or not order.orderstatus)
        order.orderstatus = "Processing"
        coupon_code = request.session.get("coupon_code", "")
        discount = request.session.get("coupon_discount", 0)
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
                CouponUsage.objects.get_or_create(coupon=coupon, user=request.user)
                order.coupon = coupon
                order.coupon_discount = discount
            except Coupon.DoesNotExist:
                pass
        order.save()
        # Stock update logic
        if is_pending:
            for item in order.orderitem_set.all():
                product = item.productview_id
                if product:
                    if product.stock is not None:
                        if product.stock >= item.quantity:
                            product.stock -= item.quantity
                            product.sold_count += item.quantity
                        else:
                            product.stock = 0
                            product.sold_count += item.quantity
                        product.save()
                    else:
                        product.sold_count = (product.sold_count or 0) + item.quantity
                        product.save()
        # Cart cleanup
        try:
            Cart.objects.filter(userid=request.user).delete()
        except Exception:
            print("CART DELETE ERROR:")
            traceback.print_exc()
        # Session cleanup
        request.session.pop("coupon_code", None)
        request.session.pop("coupon_discount", None)
        request.session.pop("order_just_placed_id", None)
        return redirect("thankyou", order.orderid)
class CancelProductView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, orderitemid):
        order_item = get_object_or_404(
            Orderitem,
            orderitemid=orderitemid,
            order_id__user_id=request.user,
        )
        order = order_item.order_id
        if request.session.get("order_just_placed_id") == order.orderid:
            messages.error(request,"Please place your order first. You cannot cancel products during checkout.",)
            return redirect("conformorder", order.orderid)
        cancelled_product_name = order_item.productview_id.producttitle
        cancelled_quantity = order_item.quantity
        cancelled_price = order_item.productview_id.productprice * order_item.quantity
        product_image_url = order_item.productview_id.productimage1
        order_item.delete()
        remaining_items = Orderitem.objects.filter(order_id=order)
        subtotal = 0
        for item in remaining_items:
            subtotal += item.productview_id.productprice * item.quantity
        order.subtotal = subtotal
        order.deliverycharges = 0
        if order.coupon:
            if subtotal >= order.coupon.minimum_amount:
                order.coupon_discount = int(
                    subtotal * order.coupon.discount / 100
                )
            else:
                order.coupon = None
                order.coupon_discount = 0
        else:
            order.coupon_discount = 0
        order.total = (order.subtotal - order.coupon_discount + order.deliverycharges)
        if not remaining_items.exists():
            order.orderstatus = "Cancelled"
            order.cancelled_at = timezone.now()
        order.save()
        # Email Sending
        if order.email:
            try:
                context = {
                    "user": request.user,
                    "order": order,
                    "product_name": cancelled_product_name,
                    "quantity": cancelled_quantity,
                    "price": cancelled_price,
                    "cancel_date": timezone.localtime().strftime(
                        "%d-%m-%Y %I:%M %p"
                    ),
                    "remaining_total": order.total,
                    "refund_amount": cancelled_price,
                    "logo_url": "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
                }
                html_content = render_to_string(
                    "emails/order_cancelled.html",
                    context,
                )
                subject = f"Order Cancellation - {order.amazon_order_id}"
                # Background thread call
                threading.Thread(
                    target=send_cancellation_email_with_image,
                    args=(order.email, subject, html_content, product_image_url),
                    daemon=True
                ).start()
            except Exception:
                print("❌ Cancellation email error occurred")
                traceback.print_exc()
        messages.success(request, "Order cancelled successfully.")
        return redirect("conformorder", order.orderid)
class ThankYouView(LoginRequiredMixin,View):
    login_url = "login"
    template_name = "thankyou.html"
    def get(self, request, orderid):
        order = get_object_or_404(Order,orderid=orderid,user_id=request.user)
        context = {"order": order}
        return render(request, self.template_name, context)
class ViewBillView(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "viewbill.html"
    def get(self, request, orderid):
        order = get_object_or_404(Order, orderid=orderid, user_id=request.user)
        pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
        if order.orderstatus == "Cancelled":
            order.payment_status_display = "Cancelled"
        elif "COD" in pm or "CASH" in pm:
            order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
        else:
            order.payment_status_display = order.paymentstatus or "Paid"
        orderitems = Orderitem.objects.filter(order_id=order)
        running_total = 0
        for item in orderitems:
            prod = item.productview_id
            unit_price = prod.productprice
            if hasattr(item, "selected_size") and item.selected_size:
                size_clean = str(item.selected_size).replace(" ", "").lower()
                s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                if s1 and s1 == size_clean:
                    unit_price = prod.productprice1 or prod.productprice
                elif s2 and s2 == size_clean:
                    unit_price = prod.productprice2 or prod.productprice
                elif s3 and s3 == size_clean:
                    unit_price = prod.productprice3 or prod.productprice
                elif s0 and s0 == size_clean:
                    unit_price = prod.productprice
            item.calculated_unit_price = unit_price
            item.calculated_subtotal = unit_price * item.quantity
            running_total += item.calculated_subtotal
        if order.coupon:
            coupon_code = order.coupon.code
            discount = order.coupon_discount
            final_total = running_total - discount
        else:
            coupon_code = ""
            discount = 0
            final_total = running_total
        order.calculated_total = final_total
        user_order_no = Order.objects.filter(user_id=request.user, orderid__lte=order.orderid).count()
        order.amazon_order_id = f"{user_order_no:05d}"
        if order.orderstatus == "Delivered":
            order.display_status_date = order.delivered_at or order.date
        elif order.orderstatus == "Shipped":
            order.display_status_date = order.shipped_at or order.date
        elif order.orderstatus == "Processing":
            order.display_status_date = order.processing_at or order.date
        elif order.orderstatus == "Cancelled":
            order.display_status_date = order.cancelled_at or order.date
        else:
            order.display_status_date = order.date

        context = {"order": order, "orderitems": orderitems}
        return render(request, self.template_name, context)
class MyOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    template_name = "myorders.html"
    def get(self, request):
        orders = Order.objects.filter(user_id=request.user).order_by("-date")
        category = Category.objects.all()
        for order in orders:
            if order.user_id:
                user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
                order.amazon_order_id = f"{user_order_no:05d}"
            else:
                order.amazon_order_id = "00001"
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = order.paymentstatus or "Paid"
            if order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            if order.date:
                order.return_last_date = order.date + timedelta(days=7)
            else:
                order.return_last_date = None
            order_items = Orderitem.objects.filter(order_id=order)
            running_total = 0
            for item in order_items:
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                running_total += item.calculated_subtotal
                item.has_reviewed = Review.objects.filter(user=request.user, product=prod).exists()
                existing_return = ReturnRequest.objects.filter(orderitem=item).first()
                if existing_return:
                    item.has_return_request = True
                    item.return_status = existing_return.status
                    item.return_date = (
                        getattr(existing_return, "updated_at", None)
                        or getattr(existing_return, "created_at", None)
                        or getattr(existing_return, "date", None)
                    )
                else:
                    item.has_return_request = False
                    item.return_status = None
                    item.return_date = None
            discount = getattr(order, "coupon_discount", 0) if order.coupon else 0
            order.calculated_subtotal = running_total
            order.calculated_total = running_total - discount
            order.order_items = order_items
        context = {"orders": orders, "category": category}
        return render(request, self.template_name, context)
class UpdateOrderStatusView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, orderid, status):
        if not request.user.is_staff:
            return redirect("login")   
        order = get_object_or_404(Order, orderid=orderid)
        old_status = order.orderstatus
        order.orderstatus = status
        if status == "Processing" and old_status != "Processing":
            order.processing_at = timezone.now()
        elif status == "Order Approved & Processing" and old_status != "Order Approved & Processing":
            order.processing_at = timezone.now()
        elif status == "Shipped" and old_status != "Shipped":
            if not order.processing_at:
                order.processing_at = timezone.now()
            order.shipped_at = timezone.now()
        elif status == "Out for Delivery" and old_status != "Out for Delivery":
            if not order.processing_at:
                order.processing_at = timezone.now()
            if not order.shipped_at:
                order.shipped_at = timezone.now()
        elif status == "Delivered" and old_status != "Delivered":
            if not order.processing_at:
                order.processing_at = timezone.now()
            if not order.shipped_at:
                order.shipped_at = timezone.now()
            order.delivered_at = timezone.now()
        if (
            status == "Delivered"
            and old_status != "Delivered"
            and not order.stock_updated
        ):
            order_items = order.orderitem_set.select_related("productview_id").all()
            with transaction.atomic():
                for item in order_items:
                    product = item.productview_id
                    quantity = item.quantity or 0
                    if quantity <= 0:
                        continue
                    product.stock = max(0, product.stock - quantity)
                    product.sold_count = (product.sold_count or 0) + quantity
                    product.in_stock = (product.stock > 0)
                    product.save(update_fields=["stock", "sold_count", "in_stock"])
                order.stock_updated = True
                order.save() 
        else:
            order.save() 
        return redirect("admin_dashboard")
class ReturnOrderView(LoginRequiredMixin, View):
    login_url = "login"
    NO_SIZE_CATEGORIES = ["wallet", "suitcase", "earbuds", "earbud", "headphone", "headphones"]
    def get_category_name(self, product):
        return product.category_id.categoryname.strip().lower() if product.category_id else ""
    def get(self, request, orderitemid):
        order_item = get_object_or_404(Orderitem.objects.select_related("order_id","productview_id","productview_id__category_id",),orderitemid=orderitemid,order_id__user_id=request.user,)
        order = order_item.order_id
        product = order_item.productview_id
        if order.orderstatus != "Delivered":
            messages.error(request, "Only delivered orders can be returned.")
            return redirect("my_orders")
        if not order.delivered_at:
            messages.error(request, "Delivery date not found.")
            return redirect("my_orders")
        expiry_date = order.delivered_at + timedelta(days=7)
        if timezone.now() > expiry_date:
            messages.error(request, "Return period has expired.")
            return redirect("my_orders")
        category_name = self.get_category_name(product)
        hide_size_issue = category_name in self.NO_SIZE_CATEGORIES
        context = {
            "order_item": order_item,
            "order": order,
            "delivered_date": order.delivered_at,
            "expiry_date": expiry_date,
            "hide_size_issue": hide_size_issue,
        }
        return render(request, "returnorder.html", context)
    def post(self, request, orderitemid):
        order_item = get_object_or_404(
            Orderitem.objects.select_related("order_id","productview_id","productview_id__category_id",),orderitemid=orderitemid,order_id__user_id=request.user,)
        order = order_item.order_id
        if order.orderstatus != "Delivered":
            messages.error(request, "Only delivered orders can be returned.")
            return redirect("my_orders")
        if ReturnRequest.objects.filter(orderitem=order_item).exists():
            messages.warning(request, "Return request already submitted.")
            return redirect("my_orders")
        if not order.delivered_at:
            messages.error(request, "Delivery date not found.")
            return redirect("my_orders")
        expiry_date = order.delivered_at + timedelta(days=7)
        if timezone.now() > expiry_date:
            messages.error(request, "Return period has expired.")
            return redirect("my_orders")
        reason = request.POST.get("reason")
        comments = request.POST.get("comments", "")
        if not reason:
            messages.error(request, "Please select a return reason.")
            return redirect("return_order", orderitemid=orderitemid)
        product = order_item.productview_id
        category_name = self.get_category_name(product)
        if category_name in self.NO_SIZE_CATEGORIES and reason == "Size Issue":
            messages.error(request, "Size Issue is not applicable for this product category.")
            return redirect("return_order", orderitemid=orderitemid)
        final_reason = f"{reason} - {comments}".strip(" -") if comments else reason
        ReturnRequest.objects.create(order=order,orderitem=order_item,reason=final_reason,status="Requested",)
        order_item.status = "Return Requested"
        order_item.save()
        messages.success(request, "Return request submitted successfully.")
        return redirect("my_orders")
def clean_str(val):
    if not val:
        return ""
    return re.sub(r"\s+", "", str(val)).strip().lower()
def get_calculated_price(item):
    if not item or not getattr(item, "productview_id", None):
        return 0, 0
    prod = item.productview_id
    unit_price = prod.productprice  
    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
    if item_size:
        s_clean = clean_str(item_size)
        s0 = clean_str(getattr(prod, "productsize", None))
        s1 = clean_str(getattr(prod, "productsize1", None))
        s2 = clean_str(getattr(prod, "productsize2", None))
        s3 = clean_str(getattr(prod, "productsize3", None))
        if s1 and s1 == s_clean:
            unit_price = (getattr(prod, "productprice1", None) or prod.productprice)
        elif s2 and s2 == s_clean:
            unit_price = (getattr(prod, "productprice2", None) or prod.productprice)
        elif s3 and s3 == s_clean:
            unit_price = (getattr(prod, "productprice3", None) or prod.productprice)
        elif s0 and s0 == s_clean:
            unit_price = prod.productprice
    qty = getattr(item, "quantity", 1) or 1
    subtotal = unit_price * qty
    return unit_price, subtotal
class AdminDashboardView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        total_products = Productview.objects.count()
        total_users = User.objects.count()
        total_stock = Productview.objects.aggregate(total=Coalesce(Sum("stock"), 0))["total"]
        total_orders = Order.objects.exclude(orderstatus="Cancelled").count()
        delivered_orders = Order.objects.filter(orderstatus="Delivered").count()
        pending_orders = Order.objects.filter(orderstatus="Pending").count()
        processing_orders = Order.objects.filter(orderstatus="Processing").count()
        shipped_orders = Order.objects.filter(orderstatus="Shipped").count()
        out_for_delivery_orders = Order.objects.filter(orderstatus="Out for Delivery").count()
        cancelled_orders = Order.objects.filter(orderstatus="Cancelled").count()
        total_revenue = Order.objects.filter(orderstatus="Delivered").aggregate(total=Coalesce(Sum("total"), 0))["total"]
        # Today Sales 
        today = timezone.now().date()
        today_orders = Order.objects.filter(date__date=today).exclude(orderstatus="Cancelled")
        today_sales = sum(order.total for order in today_orders)
        today_orders_count = today_orders.count()
        # Month Sales
        current_month_start = today.replace(day=1)
        monthly_orders_query = Order.objects.filter(date__date__gte=current_month_start).exclude(orderstatus="Cancelled").prefetch_related("orderitem_set__productview_id")
        current_month_orders_count = monthly_orders_query.count()
        current_month_sales = 0
        for order in monthly_orders_query:
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    order_subtotal += (unit_price * item.quantity)
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            # Discount calculation
            discount = 0
            if hasattr(order, "coupon") and order.coupon:
                discount = getattr(order, "coupon_discount", 0) or getattr(order, "discount", 0)
            elif hasattr(order, "coupon_discount") and order.coupon_discount:
                discount = order.coupon_discount
            elif hasattr(order, "discount") and order.discount:
                discount = order.discount
            order_total = (order_subtotal - discount + delivery_charge)
            current_month_sales += order_total
        # monthly sales data
        monthly_sales = (Order.objects.filter(orderstatus="Delivered").annotate(month=TruncMonth("date")).values("month").annotate(total=Sum("total")).order_by("month"))
        sales_labels = [sale["month"].strftime("%b") for sale in monthly_sales]
        sales_data = [sale["total"] for sale in monthly_sales]
        # monthly orders data
        monthly_orders_chart = (Order.objects.all().annotate(month=TruncMonth("date")).values("month").annotate(total_orders=Count("orderid")).order_by("month"))
        orders_data = [item["total_orders"] for item in monthly_orders_chart]
        return_orders = ReturnRequest.objects.count()
        refunded_orders = ReturnRequest.objects.filter(status="Refunded").count()
        recent_returns = ReturnRequest.objects.select_related("order", "orderitem", "orderitem__productview_id", "order__user_id", "delivery_agent").order_by("-created_at")
        for r in recent_returns:
            if r.order and r.order.user_id:
                user_order_no = Order.objects.filter(user_id=r.order.user_id, orderid__lte=r.order.orderid).count()
                r.amazon_order_id = f"{user_order_no:05d}"
            else:
                r.amazon_order_id = "00001"
            if r.orderitem:
                unit_price, refund_total = get_calculated_price(r.orderitem)
                r.calculated_unit_price = unit_price
                r.calculated_refund = refund_total    
        try:
            total_coupons = Coupon.objects.count()
            active_coupons = Coupon.objects.filter(active=True).count()
        except NameError:
            total_coupons = 0
            active_coupons = 0
        if hasattr(Order, "coupon"):
            used_coupons_count = Order.objects.filter(coupon__isnull=False).count()
        elif hasattr(Order, "discount"):
            used_coupons_count = Order.objects.filter(discount__gt=0).count()
        else:
            used_coupons_count = 0
        if hasattr(Order, "discount"):
            total_discount_given = Order.objects.aggregate(total=Coalesce(Sum("discount"), 0))["total"]
        else:
            total_discount_given = 0 
        total_reviews = Review.objects.count()
        review_products = Review.objects.values("product").distinct().count()
        pickup_agents = PickupAgent.objects.filter(is_active=True)
        recent_orders = (Order.objects.select_related("user_id").prefetch_related("orderitem_set__productview_id", "orderitem_set__returnrequest").order_by("-orderid")[:10])
        for order in recent_orders:
            if order.user_id:
                user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
                order.amazon_order_id = f"{user_order_no:05d}"
            else:
                order.amazon_order_id = "00001"
            order.status_label = order.orderstatus
            if order.orderstatus == "Delivered":
                order.display_status_date = order.delivered_at or order.date
            elif order.orderstatus == "Shipped":
                order.display_status_date = order.shipped_at or order.date
            elif order.orderstatus == "Out for Delivery":
                order.display_status_date = getattr(order, "out_for_delivery_at", None) or order.date
            elif order.orderstatus == "Processing":
                order.display_status_date = getattr(order, "processing_at", None) or order.date
            else:
                order.display_status_date = order.date
            order.display_delivery_date = order.display_status_date if order.orderstatus == "Delivered" else None
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid" 
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "discount", getattr(order, "coupon_discount", 0))
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "discount", getattr(order, "coupon_discount", 0))
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = getattr(order, "discount", 0)  
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    item.calculated_unit_price = unit_price
                    item.calculated_subtotal = unit_price * item.quantity
                    order_subtotal += item.calculated_subtotal
                item.item_status = order.orderstatus
                item.delivered_date = getattr(order, "delivered_date", getattr(order, "updated_at", None))
                item.refund_date = None
                try:
                    return_request = item.returnrequest
                    status_map = {
                        "Requested": "Return Requested",
                        "Approved": "Approved",
                        "Agent Assigned": "Agent Assigned",
                        "Accepted by Pickup Agent": "Accepted by Pickup Agent",
                        "Out for Pickup": "Out for Pickup",
                        "Pickup Completed": "Pickup Completed",
                        "Refund Initiated": "Refund Initiated",
                        "Refunded": "Refunded",
                        "Rejected": "Delivered",
                    }
                    item.item_status = status_map.get(return_request.status, order.orderstatus)
                    item.refund_date = getattr(
                        return_request,
                        "updated_at",
                        getattr(return_request, "created_at", None),
                    )
                except ReturnRequest.DoesNotExist:
                    pass
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = (order_subtotal - discount + delivery_charge)
        low_stock_products = Productview.objects.filter(stock__lte=5)[:10] 
        out_of_stock_count = Productview.objects.filter(in_stock=False).count()
        low_stock_count = Productview.objects.filter(stock__lte=5).count()
        coupons = Coupon.objects.all().order_by('-couponid')
        context = {
            "total_products": total_products,
            "total_orders": total_orders,
            "total_users": total_users,
            "total_stock": total_stock,
            "delivered_orders": delivered_orders,
            "pending_orders": pending_orders,
            "processing_orders": processing_orders,
            "shipped_orders": shipped_orders,
            "out_for_delivery_orders": out_for_delivery_orders,
            "cancelled_orders": cancelled_orders,
            "total_revenue": total_revenue,
            "sales_labels": sales_labels,
            "sales_data": sales_data,
            "orders_data": orders_data,
            "return_orders": return_orders,
            "refunded_orders": refunded_orders,
            "recent_returns": recent_returns,
            "total_coupons": total_coupons,
            "active_coupons": active_coupons,
            "used_coupons_count": used_coupons_count,
            "total_discount_given": total_discount_given,
            "total_reviews": total_reviews,
            "review_products": review_products,
            "pickup_agents": pickup_agents,
            "recent_orders": recent_orders,
            "low_stock_products": low_stock_products,
            "out_of_stock_count": out_of_stock_count,
            "low_stock_count": low_stock_count,
            "coupons": coupons,
            "today_sales": today_sales,
            "today_orders_count": today_orders_count,
            "current_month_sales": current_month_sales,
            "current_month_orders_count": current_month_orders_count,
        }
        return render(request, "admin_dashboard.html", context)
class AdminUsersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders_queryset = Order.objects.prefetch_related("orderitem_set__productview_id").order_by("-date")
        users = (User.objects.select_related("profile").prefetch_related(Prefetch("order_set", queryset=orders_queryset)).annotate(total_spent=Coalesce(Sum("order__total"), Value(0))).order_by("-date_joined"))
        for user in users:
            user.custom_user_id = f"{user.id:05d}"
            for order in user.order_set.all():
                if not getattr(order, "amazon_order_id", None):
                    user_order_no = Order.objects.filter(user_id=order.user_id,orderid__lte=order.orderid).count()
                    order.amazon_order_id = f"{user_order_no:05d}"
                else:
                    order.coupon_code_display = None
                    order.coupon_discount_display = 0
        paginator = Paginator(users, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request, "admin_users.html", {"users": page_obj})
class AdminCustomerDetailView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, user_id):
        if not request.user.is_staff:
            return redirect("login")
        users = User.objects.select_related("profile").order_by("-date_joined")
        customer = get_object_or_404(User, id=user_id)
        orders = (Order.objects.filter(user_id=customer).prefetch_related("orderitem_set__productview_id", "orderitem_set__returnrequest").order_by("-date"))
        total_orders = orders.count()
        delivered_orders = orders.filter(orderstatus="Delivered").count()
        processing_orders = orders.filter(orderstatus="Processing").count()
        cancelled_orders = orders.filter(orderstatus="Cancelled").count()
        return_orders = ReturnRequest.objects.filter(order__user_id=customer).count()
        total_spent = orders.aggregate(total=Sum("total"))["total"] or 0
        for order in orders:
            user_order_no = Order.objects.filter(user_id=customer, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            status = str(order.orderstatus).lower()
            if status == "delivered":
                order.display_status_date = order.delivered_at or order.date
                order.status_label = "Delivered"
            elif status == "shipped":
                order.display_status_date = order.shipped_at or order.date
                order.status_label = "Shipped"
            elif status == "processing":
                order.display_status_date = order.processing_at or order.date
                order.status_label = "Processing"
            else:
                order.display_status_date = order.date
                order.status_label = order.orderstatus
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    item.calculated_unit_price = unit_price
                    item.calculated_subtotal = unit_price * item.quantity
                    order_subtotal += item.calculated_subtotal 
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = (order_subtotal - discount + delivery_charge)
            
        products = []
        context = {
            "customer": customer,
            "orders": orders,
            "products": products,  
            "total_orders": total_orders,
            "delivered_orders": delivered_orders,
            "processing_orders": processing_orders,
            "cancelled_orders": cancelled_orders,
            "return_orders": return_orders,
            "total_revenue": total_spent, 
            "total_spent": total_spent,
            "users": users,
        }
        return render(request, "admin_customer_detail.html", context)
class AdminProductsView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        products = (Productview.objects.select_related("category_id").order_by("-productviewid"))
        paginator = Paginator(products, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"products": page_obj,}
        return render(request, "admin_products.html", context)
class AdminStockView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        products = Productview.objects.select_related("category_id").order_by("productname")
        paginator = Paginator(products, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"products": page_obj,}
        return render(request,"admin_stock.html",context,) 
class AdminOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders = (Order.objects.filter().exclude(orderstatus="Cancelled").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-orderid"))
        for order in orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            status = str(order.orderstatus).lower()
            if status == "delivered":
                order.display_status_date = order.delivered_at or order.date
                order.status_label = "Delivered"
            elif status == "shipped":
                order.display_status_date = order.shipped_at or order.date
                order.status_label = "Shipped"
            elif status == "processing":
                order.display_status_date = order.processing_at or order.date
                order.status_label = "Processing"
            else:
                order.display_status_date = order.date
                order.status_label = order.orderstatus
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    item.calculated_unit_price = unit_price
                    item.calculated_subtotal = unit_price * item.quantity
                    order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = (order_subtotal - discount + delivery_charge)
        context = {"orders": orders}
        return render(request, "admin_orders.html", context)
class ProcessingOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders = (Order.objects.filter(orderstatus="Processing").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            if order.orderstatus == "Processing":
                order.display_status_date = order.processing_at or order.date
                order.status_label = "Processing"
            else:
                order.display_status_date = None
                order.status_label = order.orderstatus
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = str(prod.productsize).replace(" ", "").lower() if prod.productsize else ""
                    s1 = str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else ""
                    s2 = str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else ""
                    s3 = str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else ""
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = order_subtotal - discount + delivery_charge
        return render(request, "processing_orders.html", {"orders": orders})
class ShippedOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders = (Order.objects.filter(orderstatus="Shipped").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            if order.orderstatus == "Shipped":
                order.display_status_date = order.shipped_at or order.date
                order.status_label = "Shipped"
            else:
                order.display_status_date = None
                order.status_label = order.orderstatus
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = order_subtotal - discount + delivery_charge
        return render(request, "shipped_orders.html", {"orders": orders})
class AdminOutForDeliveryOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login") 
        orders = (Order.objects.filter(orderstatus="Out for Delivery").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            if order.orderstatus == "Out for Delivery":
                order.display_status_date = getattr(order, "out_for_delivery_at", None) or order.date
                order.status_label = "Out for Delivery"
            else:
                order.display_status_date = None
                order.status_label = order.orderstatus
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    item.calculated_unit_price = unit_price
                    item.calculated_subtotal = unit_price * item.quantity
                    order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = order_subtotal - discount + delivery_charge
        return render(request, "admin_out_for_delivery_orders.html", {"orders": orders})
class AdminDeliveredOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders = (Order.objects.filter(orderstatus="Delivered").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            if order.orderstatus == "Delivered":
                order.display_status_date = order.delivered_at or order.date
                order.status_label = "Delivered"
            else:
                order.display_status_date = None
                order.status_label = order.orderstatus
            order.display_delivery_date = order.display_status_date
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                if prod:
                    unit_price = prod.productprice
                    item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                    if item_size:
                        s_clean = str(item_size).replace(" ", "").lower()
                        s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                        s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                        s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                        s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                        if s1 and s1 == s_clean:
                            unit_price = prod.productprice1 or prod.productprice
                        elif s2 and s2 == s_clean:
                            unit_price = prod.productprice2 or prod.productprice
                        elif s3 and s3 == s_clean:
                            unit_price = prod.productprice3 or prod.productprice
                        elif s0 and s0 == s_clean:
                            unit_price = prod.productprice
                    item.calculated_unit_price = unit_price
                    item.calculated_subtotal = unit_price * item.quantity
                    order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = order_subtotal - discount + delivery_charge
        return render(request, "admin_delivered_orders.html", {"delivered_orders": orders})
class CancelledOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        orders = (Order.objects.filter(orderstatus="Cancelled").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in orders:
            if order.user_id:
                user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
                order.amazon_order_id = f"{user_order_no:05d}"
            else:
                order.amazon_order_id = "00001"
            order.status_label = order.orderstatus
            order.display_status_date = getattr(order, "cancelled_at", None) or getattr(order, "updated_at", None) or order.date
            order.display_delivery_date = None
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid" 
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "discount", getattr(order, "coupon_discount", 0))
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "discount", getattr(order, "coupon_discount", 0))
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = getattr(order, "discount", 0)  
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
                item.item_status = order.orderstatus
                item.delivered_date = None
                item.refund_date = None
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = (order_subtotal - discount + delivery_charge)
        return render(request, "cancelled_orders.html", {"orders": orders})
class AdminRevenueView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        delivered_orders = (Order.objects.filter(orderstatus="Delivered").select_related("user_id").prefetch_related("orderitem_set__productview_id").order_by("-date"))
        for order in delivered_orders:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
            if order.orderstatus == "Delivered":
                order.display_status_date = order.delivered_at or order.date
                order.status_label = "Delivered"
            else:
                order.display_status_date = None
                order.status_label = order.orderstatus
            order.display_delivery_date = order.display_status_date
            pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
            if order.orderstatus == "Cancelled":
                order.payment_status_display = "Cancelled"
            elif "COD" in pm or "CASH" in pm:
                order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
            else:
                order.payment_status_display = "Paid"
            if hasattr(order, "coupon") and order.coupon:
                order.coupon_code_display = order.coupon.code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            elif hasattr(order, "coupon_code") and order.coupon_code:
                order.coupon_code_display = order.coupon_code
                order.coupon_discount_display = getattr(order, "coupon_discount", 0)
            else:
                order.coupon_code_display = None
                order.coupon_discount_display = 0
            order_subtotal = 0
            for item in order.orderitem_set.all():
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
            order.calculated_subtotal = order_subtotal
            delivery_charge = getattr(order, "delivery_charge", 0) or 0
            order.delivery_charge_display = delivery_charge
            discount = order.coupon_discount_display or 0
            order.calculated_total = order_subtotal - discount + delivery_charge
        total_revenue = sum(order.calculated_total for order in delivered_orders)
        context = {"orders": delivered_orders, "total_revenue": total_revenue}
        return render(request, "admin_revenue.html", context)
class AdminReviewsView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        reviews = Review.objects.all().order_by("-reviewid")
        context = {"reviews": reviews,}
        return render(request, "admin_reviews.html", context)
class AdminReturnOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        return_orders = ReturnRequest.objects.select_related("order","orderitem","orderitem__productview_id","order__user_id",).order_by("-created_at")
        for r in return_orders:
            if r.order and r.order.user_id:
                user_order_no = Order.objects.filter(user_id=r.order.user_id, orderid__lte=r.order.orderid).count()
                r.amazon_order_id = f"{user_order_no:05d}"
            else:
                r.amazon_order_id = "00000"
            if r.order:
                r.order_date = getattr(r.order, "date", None) or getattr(r.order, "created_at", None)
                r.delivered_on = getattr(r.order, "delivered_at", None)
            else:
                r.order_date = None
                r.delivered_on = None
            r.refunded_at = (
                getattr(r, "refunded_at", None)
                or getattr(r, "updated_at", None)
                or getattr(r, "created_at", None)
            )
            item = r.orderitem
            if item and item.productview_id:
                prod = item.productview_id
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = re.sub(r"\s+", "", str(item_size)).lower()
                    s0 = (re.sub(r"\s+", "", str(prod.productsize)).lower() if getattr(prod, "productsize", None) else "")
                    s1 = (re.sub(r"\s+", "", str(prod.productsize1)).lower() if getattr(prod, "productsize1", None) else "")
                    s2 = (re.sub(r"\s+", "", str(prod.productsize2)).lower() if getattr(prod, "productsize2", None) else "")
                    s3 = (re.sub(r"\s+", "", str(prod.productsize3)).lower() if getattr(prod, "productsize3", None) else "")
                    if s1 and s1 == s_clean:
                        unit_price = (getattr(prod, "productprice1", None) or prod.productprice)
                    elif s2 and s2 == s_clean:
                        unit_price = (getattr(prod, "productprice2", None) or prod.productprice)
                    elif s3 and s3 == s_clean:
                        unit_price = (getattr(prod, "productprice3", None) or prod.productprice)
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                r.calculated_unit_price = unit_price
                ret_qty = getattr(item, "quantity", 1) or 1
                r.calculated_refund = unit_price * ret_qty
            else:
                r.calculated_unit_price = 0
                r.calculated_refund = 0
        return render(request, "return_orders.html", {"return_orders": return_orders})
class RejectReturnView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Rejected"
        return_request.save()
        messages.success(request, "Return request rejected.")
        return redirect("admin_dashboard")
class ApproveReturnView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Approved"
        return_request.approved_at = timezone.now()
        return_request.save()
        return redirect("admin_dashboard")
class AssignPickupAgentView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        pickup_agent = get_object_or_404(PickupAgent,agentid=request.POST.get("pickup_agent"),is_active=True)
        return_request.delivery_agent = pickup_agent
        return_request.status = "Agent Assigned"
        return_request.save() 
        messages.success(request, "Pickup Agent Assigned Successfully.")
        return redirect("admin_dashboard")
class PickupDashboardView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        pickup_agent = get_object_or_404(PickupAgent,user=request.user)
        returns = ReturnRequest.objects.filter(delivery_agent=pickup_agent)
        context = {"returns": returns,"agent": pickup_agent,}
        return render(request,"pickup_dashboard.html",context) 
class AcceptPickupRequestView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest, id=pk, delivery_agent=pickup_agent)
        return_request.status = "Accepted by Pickup Agent"
        return_request.save() 
        messages.success(request, "Pickup request accepted successfully.")
        return redirect("pickup_dashboard")
class PickupAgentLoginView(View):
    def get(self, request):
        return render(request, "pickup_login.html")
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if PickupAgent.objects.filter(user=user).exists():
                login(request, user)
                return redirect("pickup_dashboard")
            else:
                messages.error(request,"You are not a Pickup Agent")
        else:
            messages.error(request,"Invalid Login")
        return redirect("pickup_login")
class SendPickupOTPView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest, pk=pk, delivery_agent=pickup_agent)
        return_request.generate_pickup_otp()
        return_request.status = "Out for Pickup"
        return_request.save() 
        messages.success(request, "Pickup OTP sent successfully.")
        return redirect("pickup_dashboard")
class VerifyPickupOTPView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest,pk=pk,delivery_agent=pickup_agent)
        return render(request,"verify_pickup_otp.html",{"return_request": return_request})
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest,pk=pk,delivery_agent=pickup_agent)
        otp = request.POST.get("otp")
        if otp == return_request.pickup_otp:
            return_request.pickup_otp_verified = True
            return_request.status = "Pickup Completed"
            return_request.pickup_completed_at = timezone.now()
            return_request.save()
            messages.success(request, "Pickup Completed Successfully.")
            return redirect("pickup_dashboard")
        messages.error(request, "Invalid OTP")
        return redirect("verify_pickup_otp", pk=pk)
class RefundInitiatedView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Refund Initiated"
        return_request.save()  
        messages.success(request, "Refund Initiated Successfully.")
        return redirect("admin_dashboard")
class AdminRefundedOrdersView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        if not request.user.is_staff:
            return redirect("login")
        refunded_orders = (ReturnRequest.objects.filter(status="Refunded").select_related("order","order__user_id","orderitem","orderitem__productview_id",).order_by("-id"))
        def normalize_size(value):
            if not value:
                return ""
            return str(value).strip().lower().replace(" ", "").replace("-", "")
        for r in refunded_orders:
            if r.order:
                if not getattr(r.order, "amazon_order_id", None):
                    user_order_no = Order.objects.filter(user_id=r.order.user_id, orderid__lte=r.order.orderid).count()
                    r.order.amazon_order_id = f"{user_order_no:05d}"
            amt = getattr(r, "refund_amount", None)
            if r.orderitem and r.orderitem.productview_id:
                product = r.orderitem.productview_id
                selected_size = normalize_size(r.orderitem.selected_size)
                variant_prices = [
                    (getattr(product, "productsize", None),getattr(product, "productprice", None),),
                    (getattr(product, "productsize1", None),getattr(product, "productprice1", None),),
                    (getattr(product, "productsize2", None),getattr(product, "productprice2", None),),
                    (getattr(product, "productsize3", None),getattr(product, "productprice3", None),),
                ]
                matched_price = None
                for sz, pr in variant_prices:
                    if sz and normalize_size(sz) == selected_size:
                        if pr is not None and pr != "":
                            matched_price = pr
                            break
                if matched_price is None or float(matched_price or 0) == 0:
                    matched_price = getattr(product, "productprice", 0) or 0
                qty = getattr(r.orderitem, "quantity", 1) or 1
                amt = Decimal(str(matched_price)) * Decimal(str(qty))
            r.calculated_refund = amt if amt is not None else 0
        return render(request, "refunded_orders.html", {"refunded_orders": refunded_orders})
class RefundCompletedView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(
            ReturnRequest.objects.select_related("order", "order__user_id", "orderitem", "orderitem__productview_id"),pk=pk)
        item = return_request.orderitem
        def normalize_size(value):
            if not value:
                return ""
            return str(value).strip().lower().replace(" ", "").replace("-", "")
        total_refund_amount = Decimal("0.00")
        if item and item.productview_id:
            product = item.productview_id
            unit_price = Decimal(str(product.productprice or 0))
            selected_size = normalize_size(item.selected_size)
            variant_prices = [
                (getattr(product, "productsize", None), getattr(product, "productprice", None)),
                (getattr(product, "productsize1", None), getattr(product, "productprice1", None)),
                (getattr(product, "productsize2", None), getattr(product, "productprice2", None)),
                (getattr(product, "productsize3", None), getattr(product, "productprice3", None)),
            ]
            for size, price in variant_prices:
                if size and normalize_size(size) == selected_size:
                    if price is not None and price != "":
                        unit_price = Decimal(str(price))
                        break
            quantity = Decimal(str(item.quantity or 1))
            total_refund_amount = unit_price * quantity
        return_request.status = "Refunded"
        return_request.refund_completed_at = timezone.now()
        return_request.refund_amount = total_refund_amount
        return_request.save(update_fields=["status", "refund_completed_at", "refund_amount"]) 
        messages.success(request, "Refund completed successfully.")
        return redirect("admin_refunded_orders")
def admin_low_stock_view(request):
    low_stock_products = Productview.objects.filter(stock__lte=5).order_by('stock')
    context = {'low_stock_products': low_stock_products,}
    return render(request, 'admin_low_stock.html', context)
def admin_coupons_view(request):
    coupons = Coupon.objects.all().order_by('-couponid')
    context = {'coupons': coupons,}
    return render(request, 'admin_coupons.html', context)
def admin_today_sales_view(request):
    if not request.user.is_staff:
        return redirect("login")
    today = timezone.now().date()
    today_orders = Order.objects.filter(date__date=today).exclude(orderstatus='Cancelled').prefetch_related("orderitem_set__productview_id").order_by('-date')
    total_sales = 0
    valid_orders_count = 0
    for order in today_orders:
        if order.user_id:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
        else:
            order.amazon_order_id = "00001"
        order.status_label = order.orderstatus
        if order.orderstatus == "Delivered":
            order.display_status_date = order.delivered_at or order.date
        elif order.orderstatus == "Shipped":
            order.display_status_date = order.shipped_at or order.date
        elif order.orderstatus == "Out for Delivery":
            order.display_status_date = getattr(order, "out_for_delivery_at", None) or order.date
        elif order.orderstatus == "Processing":
            order.display_status_date = getattr(order, "processing_at", None) or order.date
        else:
            order.display_status_date = order.date
        order.display_delivery_date = order.display_status_date if order.orderstatus == "Delivered" else None
        pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
        if order.orderstatus == "Cancelled":
            order.payment_status_display = "Cancelled"
        elif "COD" in pm or "CASH" in pm:
            order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
        else:
            order.payment_status_display = "Paid"
        # Coupon 
        if hasattr(order, "coupon") and order.coupon:
            order.coupon_code_display = order.coupon.code
            order.coupon_discount_display = getattr(order, "coupon_discount", 0)
        elif hasattr(order, "coupon_code") and order.coupon_code:
            order.coupon_code_display = order.coupon_code
            order.coupon_discount_display = getattr(order, "coupon_discount", 0)
        else:
            order.coupon_code_display = None
            order.coupon_discount_display = 0
        order_subtotal = 0
        for item in order.orderitem_set.all():
            prod = item.productview_id
            if prod:
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
        order.calculated_subtotal = order_subtotal
        delivery_charge = getattr(order, "delivery_charge", 0) or 0
        order.delivery_charge_display = delivery_charge
        discount = order.coupon_discount_display or 0
        order.calculated_total = (order_subtotal - discount + delivery_charge)
        total_sales += order.calculated_total
        valid_orders_count += 1 
    context = {
        'today_orders': today_orders,
        'today_sales': total_sales,
        'today_orders_count': valid_orders_count,
    }
    return render(request, 'admin_today_sales.html', context)
def admin_monthly_sales_view(request):
    if not request.user.is_staff:
        return redirect("login")
    today = timezone.now().date()
    current_month_start = today.replace(day=1)
    monthly_orders = Order.objects.filter(date__date__gte=current_month_start).exclude(orderstatus='Cancelled').prefetch_related("orderitem_set__productview_id").order_by('-date')

    current_month_sales = 0
    valid_orders_count = 0
    for order in monthly_orders:
        if order.user_id:
            user_order_no = Order.objects.filter(user_id=order.user_id, orderid__lte=order.orderid).count()
            order.amazon_order_id = f"{user_order_no:05d}"
        else:
            order.amazon_order_id = "00001"
        order.status_label = order.orderstatus
        if order.orderstatus == "Delivered":
            order.display_status_date = order.delivered_at or order.date
        elif order.orderstatus == "Shipped":
            order.display_status_date = order.shipped_at or order.date
        elif order.orderstatus == "Out for Delivery":
            order.display_status_date = getattr(order, "out_for_delivery_at", None) or order.date
        elif order.orderstatus == "Processing":
            order.display_status_date = getattr(order, "processing_at", None) or order.date
        else:
            order.display_status_date = order.date
        order.display_delivery_date = order.display_status_date if order.orderstatus == "Delivered" else None
        pm = str(order.paymentmethod).upper() if getattr(order, "paymentmethod", None) else ""
        if order.orderstatus == "Cancelled":
            order.payment_status_display = "Cancelled"
        elif "COD" in pm or "CASH" in pm:
            order.payment_status_display = "Paid" if order.orderstatus == "Delivered" else "Pending"
        else:
            order.payment_status_display = "Paid"
        # Coupon 
        if hasattr(order, "coupon") and order.coupon:
            order.coupon_code_display = order.coupon.code
            order.coupon_discount_display = getattr(order, "coupon_discount", 0)
        elif hasattr(order, "coupon_code") and order.coupon_code:
            order.coupon_code_display = order.coupon_code
            order.coupon_discount_display = getattr(order, "coupon_discount", 0)
        else:
            order.coupon_code_display = None
            order.coupon_discount_display = 0
        order_subtotal = 0
        for item in order.orderitem_set.all():
            prod = item.productview_id
            if prod:
                unit_price = prod.productprice
                item_size = getattr(item, "selected_size", None) or getattr(item, "size", None)
                if item_size:
                    s_clean = str(item_size).replace(" ", "").lower()
                    s0 = (str(prod.productsize).replace(" ", "").lower() if prod.productsize else "")
                    s1 = (str(prod.productsize1).replace(" ", "").lower() if prod.productsize1 else "")
                    s2 = (str(prod.productsize2).replace(" ", "").lower() if prod.productsize2 else "")
                    s3 = (str(prod.productsize3).replace(" ", "").lower() if prod.productsize3 else "")
                    if s1 and s1 == s_clean:
                        unit_price = prod.productprice1 or prod.productprice
                    elif s2 and s2 == s_clean:
                        unit_price = prod.productprice2 or prod.productprice
                    elif s3 and s3 == s_clean:
                        unit_price = prod.productprice3 or prod.productprice
                    elif s0 and s0 == s_clean:
                        unit_price = prod.productprice
                item.calculated_unit_price = unit_price
                item.calculated_subtotal = unit_price * item.quantity
                order_subtotal += item.calculated_subtotal
        order.calculated_subtotal = order_subtotal
        delivery_charge = getattr(order, "delivery_charge", 0) or 0
        order.delivery_charge_display = delivery_charge
        discount = order.coupon_discount_display or 0
        order.calculated_total = (order_subtotal - discount + delivery_charge)
        current_month_sales += order.calculated_total
        valid_orders_count += 1
    context = {
        'monthly_orders': monthly_orders,
        'current_month_sales': current_month_sales,
        'current_month_orders_count': valid_orders_count,
    }
    return render(request, 'admin_monthly_sales.html', context)
class PickupLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Pickup Agent logged out successfully.")
        return redirect("pickup_login")
class WishlistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            guest_wishlist = request.session.get('guest_wishlist', [])
            if guest_wishlist:
                for g_item in guest_wishlist:
                    prod = Productview.objects.filter(productviewid=g_item['productviewid']).first()
                    if prod:
                        wish_item, created = Wishlist.objects.get_or_create(
                            user=request.user,
                            product=prod,
                            size=g_item['size']
                        )
                        if hasattr(wish_item, 'price') and g_item.get('price'):
                            wish_item.price = g_item['price']
                            wish_item.save()
                del request.session['guest_wishlist']
            wishlist_items = list(Wishlist.objects.filter(user=request.user).select_related("product", "product__category_id").order_by("-id"))
        else:
            # Agar user logged-in nahi hai, toh session se items fetch karein
            guest_wishlist = request.session.get('guest_wishlist', [])
            wishlist_items = []
            for idx, g_item in enumerate(guest_wishlist):
                prod = Productview.objects.filter(productviewid=g_item['productviewid']).select_related("category_id").first()
                if prod:
                    class TempWishlistItem:
                        def __init__(self, id, product, size, price):
                            self.id = id
                            self.product = product
                            self.size = size
                            self.price = price
                    temp_item = TempWishlistItem(
                        id=idx, 
                        product=prod, 
                        size=g_item['size'], 
                        price=g_item['price']
                    )
                    wishlist_items.append(temp_item)
        for item in wishlist_items:
            item.quantity = getattr(item, "quantity", 1) or 1
            if hasattr(item, "product") and item.product:
                product = item.product
                selected_size = str(getattr(item, "size", "") or getattr(item, "selected_size", "") or "").strip().lower()
                unit_price = product.productprice
                mrp_price = product.productmrpprice
                if selected_size:
                    s0 = str(product.productsize or "").strip().lower()
                    s1 = str(product.productsize1 or "").strip().lower()
                    s2 = str(product.productsize2 or "").strip().lower()
                    s3 = str(product.productsize3 or "").strip().lower()
                    if selected_size == s1:
                        unit_price = product.productprice1 or product.productprice
                        mrp_price = product.productmrpprice1 or product.productmrpprice
                    elif selected_size == s2:
                        unit_price = product.productprice2 or product.productprice
                        mrp_price = product.productmrpprice2 or product.productmrpprice
                    elif selected_size == s3:
                        unit_price = product.productprice3 or product.productprice
                        mrp_price = product.productmrpprice3 or product.productmrpprice
                    elif selected_size == s0:
                        unit_price = product.productprice
                        mrp_price = product.productmrpprice
                item.calculated_price = unit_price
                item.calculated_mrp = mrp_price
                if callable(globals().get("apply_rating")):
                    apply_rating(product)
                variants = Productview.objects.filter(category_id=product.category_id,producttitle=product.producttitle,in_stock=True,).order_by("productviewid")
                ordered_variants = [product] + [v for v in variants if v.productviewid != product.productviewid]
                variants_list = []
                used_colors = set()
                for variant in ordered_variants:
                    color = (variant.productcolor1 or "").strip()
                    if not color or color.lower() in used_colors:
                        continue
                    used_colors.add(color.lower())
                    color_code = (
                        get_clean_color_code(color)
                        if callable(globals().get("get_clean_color_code"))
                        else ""
                    )
                    variants_list.append(
                        {
                            "id": variant.productviewid,
                            "name": color,
                            "image": variant.productimage1,
                            "color_code": color_code,
                        }
                    )
                product.color_variants = variants_list
        context = {"wishlist_items": wishlist_items,"products": wishlist_items,}
        return render(request, "wishlist.html", context)
class AddWishlistView(View): 
    def post(self, request, productviewid):
        product = get_object_or_404(Productview, productviewid=productviewid)
        selected_color = (request.POST.get("selected_color") or request.GET.get("color")  or getattr(product, "productcolor1", "")).strip()
        if selected_color:
            color_variant = Productview.objects.filter(category_id=product.category_id,producttitle=product.producttitle,productcolor1__iexact=selected_color,in_stock=True,).first()
            if color_variant:
                product = color_variant
        # SIZE 
        raw_size = (
            request.POST.get("selected_size")
            or request.GET.get("selected_size")
            or request.GET.get("size")
            or ""
        )
        selected_size = str(raw_size).strip()
        sizes = [
            product.productsize,
            product.productsize1,
            product.productsize2,
            product.productsize3,
        ]
        valid_sizes = [
            str(s).strip()
            for s in sizes
            if s
            and str(s).strip()
            and str(s).strip().lower()
            not in ["none", "85 cm", "standard", "free size"]
        ]
        if valid_sizes:
            if (
                not selected_size
                or selected_size.lower()
                in ["none", "85 cm", "standard", "free size"]
            ):
                selected_size = valid_sizes[0]
        else:
            selected_size = ""
        unit_price = product.productprice
        if selected_size:
            s_clean = str(selected_size).replace(" ", "").lower()
            s0 = str(product.productsize).replace(" ", "").lower() if product.productsize else ""
            s1 = str(product.productsize1).replace(" ", "").lower() if product.productsize1 else ""
            s2 = str(product.productsize2).replace(" ", "").lower() if product.productsize2 else ""
            s3 = str(product.productsize3).replace(" ", "").lower() if product.productsize3 else ""
            if s1 and s1 == s_clean:
                unit_price = product.productprice1 or product.productprice
            elif s2 and s2 == s_clean:
                unit_price = product.productprice2 or product.productprice
            elif s3 and s3 == s_clean:
                unit_price = product.productprice3 or product.productprice
            elif s0 and s0 == s_clean:
                unit_price = product.productprice
        title_text = str(product.producttitle)
        if " Display" in title_text:
            short_title = title_text.split(" Display")[0]
        elif len(title_text) > 30:
            short_title = title_text[:30] + "..."
        else:
            short_title = title_text
        size_text = f" ({selected_size})" if selected_size else ""
        # CHECK IF USER IS AUTHENTICATED (
        if request.user.is_authenticated:
            wishlist_item = Wishlist.objects.filter(user=request.user,product=product,size=selected_size,).first()
            if wishlist_item:
                if hasattr(wishlist_item, 'price'):
                    wishlist_item.price = unit_price
                    wishlist_item.save()
                messages.info(request, f"'{short_title}'{size_text} is already in your wishlist.")
            else:
                try:
                    kwargs = {
                        "user": request.user,
                        "product": product,
                        "size": selected_size,
                    }
                    if hasattr(Wishlist, 'price'):
                        kwargs["price"] = unit_price
                    Wishlist.objects.create(**kwargs)
                    messages.success(request, f"'{short_title}'{size_text} has been added to your wishlist.")
                except Exception:
                    existing_item = Wishlist.objects.filter(user=request.user, product=product).first()
                    if existing_item:
                        existing_item.size = selected_size
                        if hasattr(existing_item, 'price'):
                            existing_item.price = unit_price
                        existing_item.save()
                        messages.info(request, f"Wishlist updated to size{size_text} for '{short_title}'.")
        else:
            # Guest User ke liye Session mein store karein
            wishlist_session = request.session.get('guest_wishlist', [])
            item_data = {
                'productviewid': product.productviewid,
                'size': selected_size,
                'price': float(unit_price) if unit_price else 0.0
            }
            if item_data not in wishlist_session:
                wishlist_session.append(item_data)
                request.session['guest_wishlist'] = wishlist_session
                messages.success(request, f"'{short_title}'{size_text} has been added to your wishlist.")
            else:
                messages.info(request, f"'{short_title}'{size_text} is already in your wishlist.")
        return redirect("wishlist")
    def get(self, request, productviewid):
        return self.post(request, productviewid)
class RemoveWishlistView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, pk):
        item = get_object_or_404(Wishlist,pk=pk,user=request.user)
        messages.success(request, "Item has been removed from your Wishlist.")
        item.delete()
        return redirect("wishlist")
class ClearWishlistView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request):
        Wishlist.objects.filter(user=request.user).delete()
        return redirect("wishlist")
class SearchView(ListView):
    model = Productview
    template_name = "search.html"
    context_object_name = "products"
    paginate_by = 20
    def get_search_base_queryset(self):
        raw_query = (self.request.GET.get("q") or "").strip()
        selected_brands = self.request.GET.getlist("brand")
        narrow_filter = self.request.GET.get("narrow_filter")
        queryset = Productview.objects.select_related("category_id").all()
        category_name = None
        # Search Query 
        if raw_query:
            if "active_search_category" in self.request.session:
                del self.request.session["active_search_category"]
            clean_query = re.sub(r"[^\w\s]", "", raw_query)
            normalized_query = re.sub(r"[\s\-\.]", "", raw_query.lower())
            category_map = {
                "shirt": "Shirt",
                "shirts": "Shirt",
                "tshirt": "Tshirt",
                "tshirts": "Tshirt",
                "t-shirt": "Tshirt",
                "t shirt": "Tshirt",
                "shoe": "Shoes",
                "shoes": "Shoes",
                "bag": "Suitcase",
                "bags": "Suitcase",
                "suitcase": "Suitcase",
                "trolley": "Suitcase",
                "wallet": "wallet",
                "mobile": "Mobile",
                "mobiles": "Mobile",
                "tablet": "Tablet",
                "headphone": "Headphone",
                "headphones": "Headphone",
            }
            category_name = category_map.get(normalized_query)
            if not category_name:
                words = raw_query.split()
                search_query = Q()
                search_query |= (Q(producttitle__icontains=raw_query) | Q(productname__icontains=raw_query) | Q(category_id__categoryname__icontains=raw_query))
                if clean_query != raw_query:
                    search_query |= Q(producttitle__icontains=clean_query) | Q(productname__icontains=clean_query)
                if len(words) > 0:
                    word_query = Q()
                    for word in words:
                        w_clean = re.sub(r"[^\w]", "", word)
                        w_target = w_clean if w_clean else word
                        word_query &= (Q(producttitle__icontains=w_target) | Q(productname__icontains=w_target) | Q(category_id__categoryname__icontains=w_target))
                    search_query |= word_query
                letters = [re.escape(c) for c in raw_query if c.isalnum()]
                if letters:
                    pattern = r"[\s\.\-]*".join(letters)
                    search_query |= (Q(producttitle__iregex=pattern) | Q(productname__iregex=pattern) | Q(category_id__categoryname__iregex=pattern))
                return queryset.filter(search_query).distinct()
        # Narrow Filter
        elif selected_brands or narrow_filter:
            target_brand = (selected_brands[0] if selected_brands else narrow_filter)
            brand_product = queryset.filter(Q(productname__iexact=target_brand) | Q(producttitle__icontains=target_brand)).first()
            if brand_product and brand_product.category_id:
                category_name = brand_product.category_id.categoryname
        # Session 
        elif self.request.session.get("active_search_category"):
            category_name = self.request.session.get("active_search_category")
        if category_name:
            self.request.session["active_search_category"] = category_name
            initial_qs = queryset.filter(category_id__categoryname__iexact=category_name)
            if category_name.lower() == "shirt":
                initial_qs = initial_qs.exclude(Q(producttitle__iregex=r"t[\s\-]?shirt") | Q(productname__iregex=r"t[\s\-]?shirt"))
            return initial_qs.distinct()
        return queryset
    def get_queryset(self):
        raw_query = (self.request.GET.get("q") or "").strip()
        search_count = 1
        if raw_query and self.request.user.is_authenticated:
            history, created = SearchHistory.objects.get_or_create(userid=self.request.user,keyword__iexact=raw_query,defaults={"keyword": raw_query, "search_count": 1},)
            if not created:
                history.search_count += 1
            history.save()
            search_count = history.search_count
        self.current_search_count = search_count
        base_qs = self.get_search_base_queryset()
        self.base_search_queryset = base_qs
        queryset = base_qs
        # Narrow Filter Apply
        narrow_filter = self.request.GET.get("narrow_filter")
        if narrow_filter:
            queryset = queryset.filter(Q(producttitle__icontains=narrow_filter) | Q(productname__icontains=narrow_filter))
        # Brand 
        selected_brands = self.request.GET.getlist("brand")
        if selected_brands:
            brand_query = Q()
            for brand in selected_brands:
                brand = brand.strip()
                if not brand:
                    continue
                brand_query |= Q(producttitle__iexact=brand) | Q(producttitle__icontains=brand) | Q(productname__icontains=brand)
            queryset = queryset.filter(brand_query)
        self.brand_filtered_qs = queryset
        # Size 
        selected_sizes = self.request.GET.getlist("size")
        active_cat = (self.request.session.get("active_search_category") or "").lower()
        if selected_sizes and active_cat not in ["wallet", "headphone"]:
            size_query = Q()
            for size in selected_sizes:
                if size:
                    s_clean = str(size).strip()
                    size_query |= (Q(productsize__iexact=s_clean) | Q(productsize1__iexact=s_clean) | Q(productsize2__iexact=s_clean) | Q(productsize3__iexact=s_clean))
            queryset = queryset.filter(size_query)
        # Price Filtering Indian Currency
        price = self.request.GET.get("price")
        if price == "0-500":
            queryset = queryset.filter(productprice__lte=500)
        elif price == "500-1000":
            queryset = queryset.filter(productprice__gte=500, productprice__lte=1000)
        elif price == "1000-2000":
            queryset = queryset.filter(productprice__gte=1000, productprice__lte=2000)
        elif price == "2000-5000":
            queryset = queryset.filter(productprice__gte=2000, productprice__lte=5000)
        elif price == "5000-above":
            queryset = queryset.filter(productprice__gte=5000)
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        if min_price and min_price.isdigit():
            queryset = queryset.filter(productprice__gte=int(min_price))
        if max_price and max_price.isdigit():
            queryset = queryset.filter(productprice__lte=int(max_price))
        # Color 
        selected_colors = self.request.GET.getlist("color")
        if selected_colors:
            color_query = Q()
            for color in selected_colors:
                if color:
                    color_clean = str(color).strip()
                    if color_clean.lower() == "blue":
                        color_query |= Q(productcolor1__iexact="Blue") | (
                            Q(productcolor1__icontains="Blue")
                            & ~Q(productcolor1__icontains="Sky Blue")
                            & ~Q(productcolor1__icontains="Navy Blue")
                            & ~Q(productcolor1__icontains="Dark Blue")
                        )
                    else:
                        color_query |= Q(productcolor1__icontains=color_clean)
            queryset = queryset.filter(color_query)
        # Rotation logic
        if raw_query and self.request.user.is_authenticated:
            ids = list(queryset.values_list("pk", flat=True))
            total = len(ids)
            if total > 1:
                offset = (search_count - 1) % total
                ids = ids[offset:] + ids[:offset]
                preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
                queryset = queryset.filter(pk__in=ids).order_by(preserved)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Delivery Date 
        today = timezone.localdate()
        context["delivery_date"] = today + timedelta(days=2)
        # Banner 
        products = context.get("products") or self.get_queryset()
        try:
            reference_product = products[0] if products else None
        except (TypeError, IndexError):
            reference_product = products.first() if hasattr(products, "first") else None
        banner = None
        if reference_product:
            banner = (Productview.objects.filter(category_id=reference_product.category_id, in_stock=True).exclude(productviewid=reference_product.productviewid).order_by("?").first())
        if not banner:
            banner = Productview.objects.filter(in_stock=True).order_by("?").first()
        if not banner:
            banner = reference_product
        if banner:
            apply_rating(banner)
            context["home_banner"] = banner
        raw_query = (self.request.GET.get("q") or "").strip()
        selected_brands = self.request.GET.getlist("brand")
        selected_sizes = self.request.GET.getlist("size")
        selected_colors = self.request.GET.getlist("color")
        price = self.request.GET.get("price", "")
        narrow_filter = self.request.GET.get("narrow_filter")
        context["query"] = raw_query
        # Pagination
        get_copy = self.request.GET.copy()
        if "page" in get_copy:
            get_copy.pop("page")
        context["extra_url_params"] = get_copy.urlencode()
        # Breadcrumb Title
        active_cat = self.request.session.get("active_search_category", "Products")
        base_title = raw_query if raw_query else active_cat
        applied_filters = []
        if narrow_filter:
            applied_filters.append(narrow_filter)
        if selected_brands:
            applied_filters.append(f"Brand: {', '.join(selected_brands)}")
        if selected_sizes:
            applied_filters.append(f"Size: {', '.join(selected_sizes)}")
        if selected_colors:
            applied_filters.append(f"Color: {', '.join(selected_colors)}")
        if price:
            price_map = {
                "0-500": "Under ₹500",
                "500-1000": "₹500 - ₹1,000",
                "1000-2000": "₹1,000 - ₹2,000",
                "2000-5000": "₹2,000 - ₹5,000",
                "5000-above": "Over ₹5,000",
            }
            applied_filters.append(f"Price: {price_map.get(price, price)}")
        context["breadcrumb_title"] = (
            f"{base_title} ({', '.join(applied_filters)})"
            if applied_filters
            else base_title
        )
        base_qs = getattr(self, "base_search_queryset", Productview.objects.none())
        active_qs = getattr(self, "brand_filtered_qs", base_qs)
        # BRAND LIST 
        grouped_brands = list(base_qs.exclude(producttitle__isnull=True).exclude(producttitle="").values("producttitle").annotate(item_count=Count("productviewid")).order_by("-item_count")[:12])
        brand_list = []
        for item in grouped_brands:
            title_name = item["producttitle"].strip()
            brand_list.append({"name": title_name,"value": title_name,"count": item["item_count"],})
        # NARROW SEARCH SLIDER LOGIC 
        narrow_brands_order = list(grouped_brands)
        active_brand = None
        if selected_brands and selected_brands[0]:
            active_brand = selected_brands[0].strip().lower()
        elif narrow_filter:
            active_brand = narrow_filter.strip().lower()
        if active_brand:
            primary = []
            secondary = []
            for item in narrow_brands_order:
                t_lower = item["producttitle"].strip().lower()
                if active_brand in t_lower or t_lower in active_brand:
                    primary.append(item)
                else:
                    secondary.append(item)
            narrow_brands_order = primary + secondary
        narrow_search_list = []
        for item in narrow_brands_order:
            title_name = item["producttitle"].strip()
            first_prod = (base_qs.filter(producttitle=title_name).exclude(productimage1__isnull=True).exclude(productimage1="").first())
            img_url = first_prod.productimage1 if first_prod else None
            narrow_search_list.append({"title": title_name,"image": img_url,"filter_val": title_name,})
        context["brand_list"] = brand_list
        context["narrow_search_list"] = narrow_search_list
        # 3card context
        query_str = raw_query.lower()
        search_context = []
        if query_str:
            if "shoe" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="Shoe").order_by("?")[:3]
            elif "tshirt" in query_str or "t-shirt" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__iexact="Tshirt").order_by("?")[:3]
            elif "shirt" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__iexact="Shirt").order_by("?")[:3]
            elif "suitcase" in query_str or "bag" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="suitcase").order_by("?")[:3]
            elif "wallet" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="wallet").order_by("?")[:3]
            elif "trouser" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="trouser").order_by("?")[:3]
            elif "mobile" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="mobile").order_by("?")[:3]
            elif "tablet" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="tablet").order_by("?")[:3]
            elif "headphone" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="headphone").order_by("?")[:3]
            elif "earbud" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="earbud").order_by("?")[:3]
            elif "mobilecover" in query_str:
                search_context = Productview.objects.filter(category_id__categoryname__icontains="mobilecover").order_by("?")[:3]
        for product in search_context:
            if callable(globals().get("apply_rating")):
                apply_rating(product)
        context["search_context_products"] = search_context
        # Color Variants logic for Product Cards
        product_list = context.get("object_list", [])
        if product_list:
            titles = [p.producttitle for p in product_list if p and p.producttitle]
            all_variants = Productview.objects.filter(producttitle__in=titles).only("productviewid", "category_id", "producttitle", "productcolor1", "productimage1")
            variant_dict = {}
            for v in all_variants:
                if v.producttitle:
                    variant_dict.setdefault(v.producttitle, []).append(v)
            for product in product_list:
                related_variants = variant_dict.get(product.producttitle, [])
                variants_list = []
                used_colors = set()
                current_color = str(getattr(product, "productcolor1", "") or "").strip()
                if current_color:
                    used_colors.add(current_color.lower())
                    variants_list.append({
                        "id": product.productviewid,
                        "name": current_color,
                        "image": product.productimage1,
                        "color_code": get_clean_color_code(current_color)
                        if callable(globals().get("get_clean_color_code"))
                        else "",
                    })
                for variant in related_variants:
                    color = str(getattr(variant, "productcolor1", "") or "").strip()
                    if not color or color.lower() in used_colors:
                        continue
                    used_colors.add(color.lower())
                    variants_list.append({
                        "id": variant.productviewid,
                        "name": color,
                        "image": variant.productimage1,
                        "color_code": get_clean_color_code(color)
                        if callable(globals().get("get_clean_color_code"))
                        else "",
                    })
                product.color_variants = variants_list
                if callable(globals().get("apply_rating")):
                    apply_rating(product)
        # Sizes Context
        excluded_size_categories = ["wallet", "mobile cover", "headphone", "earbuds"]
        active_cat = (self.request.session.get("active_search_category") or "").lower()
        is_no_size_category = active_cat in excluded_size_categories
        if not is_no_size_category and active_qs.exists():
            is_no_size_category = active_qs.filter(Q(category_id__categoryname__icontains="wallet") | Q(category_id__categoryname__icontains="mobile cover") | Q(category_id__categoryname__icontains="headphone") |Q(category_id__categoryname__icontains="earbud")).exists()
        if is_no_size_category:
            context["size_list"] = []
        else:
            size_list = []
            sizes = set()
            for p in active_qs:
                for size in [getattr(p, "productsize", None), getattr(p, "productsize1", None), getattr(p, "productsize2", None), getattr(p, "productsize3", None)]:
                    if size:
                        s_clean = str(size).strip()
                        if s_clean and s_clean.lower() not in ["none", "n"] and "85" not in s_clean:
                            sizes.add(s_clean)
            for size in sorted(sizes):
                count = active_qs.filter(Q(productsize__iexact=size) | Q(productsize1__iexact=size) |  Q(productsize2__iexact=size) |  Q(productsize3__iexact=size)).count()
                size_list.append({"name": size, "count": count})
            context["size_list"] = size_list
        if banner:
            apply_rating(banner)
            context["banner"] = banner  
        # Dynamic Color Context
        color_values = (active_qs.exclude(productcolor1__isnull=True).exclude(productcolor1="").values_list("productcolor1", flat=True).distinct())
        color_list = []
        for color in sorted(color_values):
            color_clean = str(color).strip()
            if color_clean:
                color_count = active_qs.filter(productcolor1__iexact=color_clean).count()
                if color_count > 0:
                    color_list.append({
                        "name": color_clean,
                        "count": color_count,
                        "color_code": get_clean_color_code(color_clean)
                        if callable(globals().get("get_clean_color_code"))
                        else "",
                    })
        context["color_list"] = color_list
        context["selected_brands"] = selected_brands
        context["selected_sizes"] = selected_sizes
        context["selected_colors"] = selected_colors
        context["selected_price"] = price
        return context
class LiveSearchView(View):
    def get(self, request):
        query = request.GET.get("q", "").strip()
        if not query:
            return JsonResponse({"brands": []})
        try:
            clean_query = re.sub(r"[^\w\s-]","",query).strip()
            query_lower = clean_query.lower()
            if not clean_query:
                return JsonResponse({"brands": []})
            base_query = (Q(producttitle__icontains=clean_query)| Q(category_id__categoryname__icontains=clean_query))
            queryset = Productview.objects.filter(base_query,in_stock=True)
            if (
                "shirt" in query_lower
                and "tshirt" not in query_lower
                and "t-shirt" not in query_lower
                and "t shirt" not in query_lower
            ):
                queryset = queryset.exclude(Q(producttitle__icontains="t-shirt")| Q(producttitle__icontains="tshirt")| Q(producttitle__icontains="t shirt")| Q(category_id__categoryname__icontains="t-shirt")| Q(category_id__categoryname__icontains="tshirt")| Q(category_id__categoryname__icontains="t shirt"))
            title_results = (queryset.exclude(producttitle__isnull=True).exclude(producttitle__exact="").values("producttitle","productname","category_id__categoryid","category_id__categoryname",).annotate(total_products=Count("productviewid")).order_by("-total_products"))
            brand_data = []
            seen_titles = set()
            for item in title_results:
                product_title = (item["producttitle"] or "").strip()
                brand_name = (item["productname"] or "").strip()
                category_id = (item["category_id__categoryid"])
                if not category_id:
                    continue
                category_name = (item["category_id__categoryname"] or "").strip()
                if not product_title:
                    continue
                title_key = product_title.lower()
                if title_key in seen_titles:
                    continue
                seen_titles.add(title_key)
                title_count = Productview.objects.filter(producttitle__iexact=product_title,category_id__categoryid=category_id,in_stock=True)
                if (
                    "shirt" in query_lower
                    and "tshirt" not in query_lower
                    and "t-shirt" not in query_lower
                    and "t shirt" not in query_lower
                ):
                    title_count = title_count.exclude(Q(producttitle__icontains="t-shirt")| Q(producttitle__icontains="tshirt")| Q(producttitle__icontains="t shirt"))
                total_count = title_count.count()
                brand_url = (f"/collection/{category_id}/"f"?brand={quote(product_title)}")
                brand_data.append({
                    "brand": brand_name,
                    "title": product_title,
                    "category": category_name,
                    "count": total_count,
                    "url": brand_url,
                })
                if len(brand_data) >= 11:
                    break
            return JsonResponse({"brands": brand_data})
        except Exception as e:
            print("LiveSearchView Error:",e)
            return JsonResponse({"brands": []})
class BrowsingHistoryView(TemplateView):
    template_name = "browsing_history.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ids = self.request.session.get("recently_viewed", [])
        products = []
        for pid in ids:
            try:
                product = Productview.objects.get(productviewid=pid)
                apply_rating(product)
                products.append(product)
            except Productview.DoesNotExist:
                pass
        context["products"] = products
        context["delivery_date"] = timezone.localdate() + timedelta(days=5)
        return context
def remove_recent(request, pk):
    history = request.session.get("recently_viewed", [])
    if pk in history:
        history.remove(pk)
    request.session["recently_viewed"] = history
    return redirect("browsing_history")
def link_callback(uri, rel):
    if not uri:
        return ""
    uri = str(uri).strip()
    if os.path.isabs(uri) and os.path.exists(uri):
        return uri
    if uri.startswith("http://") or uri.startswith("https://"):
        return uri  
    clean_uri = uri.lstrip("/\\")
    if settings.MEDIA_ROOT:
        potential_path = os.path.join(settings.MEDIA_ROOT, clean_uri)
        if os.path.exists(potential_path):
            return potential_path
        if clean_uri.startswith("media/"):
            potential_path = os.path.join(settings.MEDIA_ROOT, clean_uri[6:])
            if os.path.exists(potential_path):
                return potential_path
    if settings.STATIC_ROOT:
        potential_path = os.path.join(settings.STATIC_ROOT, clean_uri)
        if os.path.exists(potential_path):
            return potential_path
        if clean_uri.startswith("static/"):
            potential_path = os.path.join(settings.STATIC_ROOT, clean_uri[7:])
            if os.path.exists(potential_path):
                return potential_path
    if hasattr(settings, 'STATICFILES_DIRS') and settings.STATICFILES_DIRS:
        for d in settings.STATICFILES_DIRS:
            if d:
                potential_path = os.path.join(d, clean_uri)
                if os.path.exists(potential_path):
                    return potential_path
                if clean_uri.startswith("static/"):
                    potential_path = os.path.join(d, clean_uri[7:])
                    if os.path.exists(potential_path):
                        return potential_path
    potential_path = os.path.join(settings.BASE_DIR, clean_uri)
    if os.path.exists(potential_path):
        return potential_path
    return uri
def download_bill(request, order_id):
    order = get_object_or_404(Order, orderid=order_id, user_id=request.user)
    try:
        order_no = f"{int(order.orderid):05d}"
    except ValueError:
        order_no = order.orderid 
    formatted_invoice_id = f"eiser-{order_no}"
    context = {
        'order': order,
        'amazon_order_id': formatted_invoice_id,
        'logo_url': "https://res.cloudinary.com/rccdb6pd/image/upload/v1789276432/logo.png",
    }
    template_path = 'emails/invoice_pdf.html'
    html = render_to_string(template_path, context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Invoice_{formatted_invoice_id}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('Error generating PDF <pre>' + html + '</pre>')
    return response






from .serializers import RegisterSerializer,LoginSerializer,ProfileSerializer,ForgotPasswordSerializer,ResetPasswordSerializer,CategorySerializer,ProductSerializer,ReviewSerializer,WishlistSerializer,CartSerializer,OrderItemSerializer,OrderSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework import status
from django.urls import reverse
from django.db.models import Q
import random
class HomeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        featured_brands = get_featured_brands()
        product_ids = [
            int(pid)
            for pid in request.session.get("recently_viewed", [])
            if str(pid).isdigit()
        ]
        products_data = []
        browsing_list = []
        if product_ids:
            products = list(Productview.objects.filter(productviewid__in=product_ids))
            products.sort(key=lambda x: product_ids.index(int(x.productviewid)))
            for p in products:
                products_data.append({"product_id": p.productviewid,"title": p.producttitle,})
            browsing_products = list(Productview.objects.filter(productviewid__in=product_ids).select_related("category_id"))
            browsing_products.sort(key=lambda x: product_ids.index(int(x.productviewid)))
            for product in browsing_products[:14]:
                if product.productimage1:
                    img_url = (
                        product.productimage1.url
                        if hasattr(product.productimage1, "url")
                        else product.productimage1
                    )
                    browsing_list.append(
                        {
                            "image": img_url,
                            "product_id": product.productviewid,
                            "category_id": (
                                product.category_id.categoryid
                                if product.category_id
                                else None
                            ),
                        }
                    )
        if request.user.is_authenticated:
            search_history = list(SearchHistory.objects.filter(userid=request.user).order_by("-searched_at").values_list("query", flat=True)[:20])
        else:
            search_history = request.session.get("search_history", [])
        coupons = list(
            Coupon.objects.filter(active=True).order_by("-couponid").values("couponid", "code", "discount"))
        top_rated_products = []
        category_filter = Q(category_id__categoryname__icontains="shirt") | Q(category_id__categoryname__icontains="tshirt")
        titles = (Productview.objects.filter(category_filter, in_stock=True).values_list("producttitle", flat=True).distinct())
        for title in titles:
            product = Productview.objects.filter(category_filter, producttitle=title, in_stock=True).first()
            if product:
                top_rated_products.append(attach_variants_and_rating(product))
        top_rated_products.sort(key=lambda x: getattr(x, "rating", 0), reverse=True)
        top_product_ids = [p.productviewid for p in top_rated_products]
        deals_of_the_day = []
        deal_titles = list(Productview.objects.filter(in_stock=True, category_id__categoryname__in=["Shirt", "Tshirt"]).values_list("producttitle", flat=True).distinct())
        random.shuffle(deal_titles)
        for title in deal_titles:
            product = (Productview.objects.filter(producttitle=title,in_stock=True,category_id__categoryname__in=["Shirt", "Tshirt"],).order_by("-productviewid").first())
            if product:
                deals_of_the_day.append(attach_variants_and_rating(product))
        random.shuffle(deals_of_the_day)
        deal_product_ids = [p.productviewid for p in deals_of_the_day]
        new_arrivals = []
        target_arrival_titles = [
            "Bacca Bucci Men Lace Up Basketball Shoe",
            "Bacca Bucci Men Lace Up Running Shoes",
            "Bacca Bucci Men Lace Up Athletic Shoes",
            "Reebok Men's Running Shoes EVA Cushioned Breathable Mesh Sports Shoes for Men",
            "Safari Pentagon Pro 8 Wheels Spinner Checkin Trolley Bag, Hard Case Polypropylene 360º Wheeling Luggage for Men & Women, Suitcase Bag",
            "Safari Cabin Genius Alley rolley Bag Hard Case Polypropylene, 4 Spinner Wheels, 360 Degree Wheeling Carry on Luggage, Travel Bag, Suitcase for Travel, Trolley Bags for Travel",
            "Provogue Spectrum Hard-Sided PP Trolley Bags for Travel Medium Size Expandable Luggage Suitcase with 8 Wheels Combination Lock",
            "Boldfit Sneakers for Man Lightweight Shoes for Men Comfortable Sneakers for Men Air Mesh Casual Shoes Mens Soft Cushion Insole Lace Up Casual Boys Shoe Sneaker DripWave",
            "Campus Men Oxyfit (N) Walking Shoes",
            "WildHorn Genuine Leather Wallet for Men Slim Bifold Wallet with RFID Blocking Multiple Card Slots & Coin Pocket Premium Leather Mens Wallet",
            "URBAN FOREST Zeus Vintage Leather Bi-Fold Wallet for Men",
            "Tommy Hilfiger Men's Cuiaba Slimfold Wallet Leather with Liner Texture Ultra-Slim Minimalist Design Stylish Purse for Men",
            "NAPA HIDE Leather Wallet for Men Handcrafted Credit/Debit Card Slots 2 Currency Compartments 2 Secret Compartments",
            "TALED Genuine Leather Wallet - RFID Blocking Wallet for Men,12 Card Holder with Coin Pocket for Men with Gift Box, Nature Anthracite",
            "Spiffy Genuine Leather Wallet for Men RFID Men Wallet, Slim Bifold Card Holder Wallet for Man with 12 Card Slots",
            "Mehrang Men's Stretchable Stretchable Formal Pant Trousers Stylish Slim Fit Men's Wear Trousers for Office or Party Polycotton Knitted Fabric",
            "Men’s Multi Color Cargo Casual Trousers Men’s Regular Fit Straight Pants Comfortable Stylish Cargo for Men Soft Fabric for Everyday Wear, Travel & Office Linen Cotton Bottom Wear",
            "pTron Bassbuds Astra in-Ear TWS Earbuds w/Stereo Sound, 34Hrs Playtime, Stereo Calls, Custom EQ, BTv5.3 Headphones, Touch Control, Voice Assistant, Type C Charging & IPX4",
            "Teakwood Unisex Trolley Bag, Hard Cabin Trolley Small,Trolley Bag for Travel, Lock System 360 Degree 8 Rotating Wheel",
            "Bacca Bucci Men Lace Up Sneaker Shoes",
        ]
        arrival_titles = (Productview.objects.filter(in_stock=True, producttitle__in=target_arrival_titles).values_list("producttitle", flat=True).distinct())
        for title in arrival_titles:
            product = (Productview.objects.filter(producttitle=title, in_stock=True).order_by("-productviewid").first())
            if product:
                new_arrivals.append(attach_variants_and_rating(product))
        recommended_products = []
        base_queryset = Productview.objects.filter(in_stock=True, category_id__categoryname__in=["Shirt", "Tshirt"]).exclude(productviewid__in=deal_product_ids + top_product_ids)
        rec_titles = list(base_queryset.values_list("producttitle", flat=True).distinct())
        random.shuffle(rec_titles)
        seen_titles = set()
        for title in rec_titles:
            title_clean = title.strip() if title else ""
            if title_clean and title_clean not in seen_titles:
                product = (
                    base_queryset.filter(producttitle=title).order_by("-productviewid").first())
                if product:
                    seen_titles.add(title_clean)
                    recommended_products.append(attach_variants_and_rating(product))
        random.shuffle(recommended_products)
        banner = Productview.objects.filter(in_stock=True).order_by("?").first()
        banner_data = None
        if banner:
            apply_rating(banner)
            banner_data = {
                "product_id": banner.productviewid,
                "title": banner.producttitle,
                "image": banner.productimage1.url
                if hasattr(banner.productimage1, "url")
                else banner.productimage1,
            }
        response_data = {
            "featured_brands": featured_brands,
            "recently_viewed_products": products_data,
            "browsing_list": browsing_list,
            "browsing_history_url": reverse("browsing_history"),
            "search_history": search_history,
            "coupons": coupons,
            "top_product_ids": top_product_ids,
            "deals_product_ids": deal_product_ids,
            "new_arrival_product_ids": [p.productviewid for p in new_arrivals],
            "home_banner": banner_data,
        }
        return Response(response_data)
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            SearchHistory.objects.filter(userid=request.user).delete()
        else:
            request.session["search_history"] = []
        return Response({"message": "Search history cleared successfully."})
class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Account created successfully.",
                    "user": {
                        "id": user.id,
                        "firstname": user.first_name,
                        "lastname": user.last_name,
                        "username": user.username,
                        "email": user.email,
                    }
                },
                status=status.HTTP_201_CREATED
            )
        return Response({"message": "Registration failed.","errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "message": "Login successful.",
                    "token": token.key,
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                    }
                },status=status.HTTP_200_OK)
        return Response({"message": "Login failed.","errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
class LogoutAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        username = getattr(request.user,"username","User")
        if request.auth:
            request.auth.delete()
        return Response(
            {"message": f"Thank you for visiting EiserShop, {username}."},status=200)
class ForgotPasswordSendOTPAPI(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Invalid request.","errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        identifier = serializer.validated_data["identifier"].strip()
        user = User.objects.filter(email__iexact=identifier).first()
        if not user:
            user = User.objects.filter(username__iexact=identifier).first()
        if not user:
            return Response({"message": "No account found with this Email or Username."},status=status.HTTP_404_NOT_FOUND)
        generated_otp = str(random.randint(100000, 999999))
        cache.set(f"password_reset_otp_{user.id}",generated_otp,timeout=600)
        try:
            send_mail(
                subject="Password Reset OTP - EiserShop",
                message=f"""
Hello {user.username},
Your Password Reset OTP is:
{generated_otp}
This OTP is valid for 10 minutes.
Do not share this OTP with anyone.
Regards,
EiserShop Team
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            return Response({"message": "OTP sent successfully to your registered email."},status=status.HTTP_200_OK)
        except Exception:
            traceback.print_exc()
            return Response({"message": "Unable to send OTP email."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ForgotPasswordResetAPI(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Password reset failed.","errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        identifier = serializer.validated_data["identifier"].strip()
        otp = serializer.validated_data["otp"].strip()
        newpassword = serializer.validated_data["newpassword"]
        user = User.objects.filter(email__iexact=identifier).first()
        if not user:
            user = User.objects.filter(username__iexact=identifier).first()
        if not user:
            return Response({"message": "No account found with this Email or Username."},status=status.HTTP_404_NOT_FOUND)
        stored_otp = cache.get(f"password_reset_otp_{user.id}")
        if not stored_otp:
            return Response({"message": "OTP expired. Please generate a new OTP."},status=status.HTTP_400_BAD_REQUEST)
        if otp != stored_otp:
            return Response({"message": "Invalid OTP."},status=status.HTTP_400_BAD_REQUEST)
        user.set_password(newpassword)
        user.save()
        cache.delete(f"password_reset_otp_{user.id}")
        return Response({"message": "Password reset successfully.","username": user.username},status=status.HTTP_200_OK)
class ProfileAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        return Response(
            {
                "message": "Profile fetched successfully.",
                "user": {
                    "id": user.id,
                    "firstname": user.first_name,
                    "lastname": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "profile_image": (
                        request.build_absolute_uri(profile.image.url)
                        if profile.image
                        else None
                    ),
                }
            },
            status=status.HTTP_200_OK
        )
    def put(self, request):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        serializer = ProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"message": "Profile update failed.","errors": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        firstname = serializer.validated_data["firstname"].strip()
        lastname = serializer.validated_data.get("lastname", "").strip()
        username = serializer.validated_data["username"].strip()
        email = serializer.validated_data["email"].strip()
        if User.objects.exclude(pk=user.pk).filter(username=username).exists():
            return Response({"message": "Username already exists."},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.exclude(pk=user.pk).filter(email=email).exists():
            return Response({"message": "Email already exists."},status=status.HTTP_400_BAD_REQUEST)
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        user.email = email
        uploaded_image = request.FILES.get("profile_image")
        try:
            user.save()
            if uploaded_image:
                profile.image = uploaded_image
            profile.save()
            return Response(
                {
                    "message": (
                        f"Hello {user.username}, "
                        "your profile has been updated successfully."
                    ),
                    "user": {
                        "id": user.id,
                        "firstname": user.first_name,
                        "lastname": user.last_name,
                        "username": user.username,
                        "email": user.email,
                        "profile_image": (
                            request.build_absolute_uri(profile.image.url)
                            if profile.image
                            else None
                        ),
                    }
                },status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({"message": "Username or Email already exists."},status=status.HTTP_400_BAD_REQUEST)
class CategoryAPI(APIView):
    def get(self, request):
        categories = Category.objects.all().order_by("categoryid")
        serializer = CategorySerializer(categories,many=True)
        return Response({"message": "Categories fetched successfully.","categories": serializer.data},status=status.HTTP_200_OK)
class ProductAPI(APIView):
    def get(self, request):
        products = Productview.objects.select_related("category_id").filter(in_stock=True).order_by("-productviewid")
        serializer = ProductSerializer(products,many=True)
        return Response({"message": "Products fetched successfully.","count": products.count(),"products": serializer.data},status=status.HTTP_200_OK)
class ProductDetailAPI(APIView):
    def get(self, request, product_id):
        try:
            product = (Productview.objects.select_related("category_id").prefetch_related("review_set__user").get(productviewid=product_id))
        except Productview.DoesNotExist:
            return Response({"message": "Product not found."},status=status.HTTP_404_NOT_FOUND)
        try:
            curr_pid = int(product_id)
            recently_viewed = [int(pid) for pid in request.session.get("recently_viewed", [])]
            if curr_pid in recently_viewed:
                recently_viewed.remove(curr_pid)
            recently_viewed.insert(0, curr_pid)
            request.session["recently_viewed"] = recently_viewed[:20]
            request.session.modified = True
        except ValueError:
            pass
        serializer = ProductSerializer(product, context={"request": request})
        color_variants = Productview.objects.filter(producttitle=product.producttitle, in_stock=True).exclude(productviewid=product.productviewid)
        color_variants_serializer = ProductSerializer(color_variants, many=True, context={"request": request})
        return Response({"message": "Product fetched successfully.","product": serializer.data,"color_variants": color_variants_serializer.data,},status=status.HTTP_200_OK,)
class CreateReviewAPI(APIView):
    permission_classes = [IsAuthenticated]  
    def post(self, request, product_id):
        try:
            product = Productview.objects.get(productviewid=product_id)
        except Productview.DoesNotExist:
            return Response({"message": "Product not found."},status=status.HTTP_404_NOT_FOUND,)
        serializer = ReviewSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response({"message": "Review added successfully.","review": serializer.data,},status=status.HTTP_201_CREATED,)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class DeleteReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, reviewid):
        review = get_object_or_404(Review, reviewid=reviewid)
        if review.user != request.user:
            return Response({"error": "You can only delete your own review."},status=status.HTTP_403_FORBIDDEN,)
        review.delete()
        return Response({"message": "Your review has been deleted successfully."},status=status.HTTP_200_OK,)
class CartAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        cart_items = Cart.objects.filter(userid=request.user).select_related("product_id","product_id__category_id").order_by("-cartid")
        serializer = CartSerializer(cart_items,many=True)
        total = sum(
            item.subtotal()
            for item in cart_items
        )
        return Response({"message": "Cart fetched successfully.","count": cart_items.count(),"total": total,"cart": serializer.data},status=status.HTTP_200_OK)
    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        selected_size = request.data.get("selected_size")
        if not product_id:
            return Response({"message": "product_id is required."},status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Productview.objects.get(productviewid=product_id)
        except Productview.DoesNotExist:
            return Response({"message": "Product not found."},status=status.HTTP_404_NOT_FOUND)
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return Response({"message": "Quantity must be a valid number."},status=status.HTTP_400_BAD_REQUEST)
        if quantity < 1:
            return Response({"message": "Quantity must be at least 1."},status=status.HTTP_400_BAD_REQUEST)
        if product.stock < quantity:
            return Response({"message": "Insufficient stock.","available_stock": product.stock},status=status.HTTP_400_BAD_REQUEST)
        cart_item = Cart.objects.filter(userid=request.user,product_id=product).first()
        if cart_item:
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.stock:
                return Response({"message": "Requested quantity exceeds available stock.","available_stock": product.stock,"current_quantity": cart_item.quantity},status=status.HTTP_400_BAD_REQUEST)
            cart_item.quantity = new_quantity
            if selected_size:
                cart_item.selected_size = selected_size
            cart_item.save()
            message = "Product quantity updated in cart."
        else:
            cart_item = Cart.objects.create(
                userid=request.user,
                product_id=product,
                quantity=quantity,
                selected_size=selected_size
            )
            message = "Product added to cart successfully."
        serializer = CartSerializer(cart_item)
        return Response({"message": message,"cart": serializer.data},status=status.HTTP_200_OK)
class CartUpdateAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, cart_id):
        try:
            cart_item = Cart.objects.select_related("product_id").get(cartid=cart_id,userid=request.user)
        except Cart.DoesNotExist:
            return Response({"message": "Cart item not found."},status=status.HTTP_404_NOT_FOUND)
        quantity = request.data.get("quantity",cart_item.quantity)
        selected_size = request.data.get("selected_size",cart_item.selected_size)
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return Response({"message": "Quantity must be a valid number."},status=status.HTTP_400_BAD_REQUEST)
        if quantity < 1:
            return Response({"message": "Quantity must be at least 1."},status=status.HTTP_400_BAD_REQUEST)
        if quantity > cart_item.product_id.stock:
            return Response({"message": "Requested quantity exceeds available stock.","available_stock": cart_item.product_id.stock},status=status.HTTP_400_BAD_REQUEST)
        cart_item.quantity = quantity
        cart_item.selected_size = selected_size
        cart_item.save()
        serializer = CartSerializer(cart_item)
        return Response({"message": "Cart updated successfully.","cart": serializer.data},status=status.HTTP_200_OK)
class AddToCartAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, productviewid):
        product = get_object_or_404(Productview,productviewid=productviewid)
        raw_size = (
            request.data.get("selected_size")
            or request.query_params.get("size")
            or ""
        )
        selected_size = str(raw_size).strip()
        sizes = [product.productsize,product.productsize1,product.productsize2,product.productsize3]
        valid_sizes = [
            size.strip()
            for size in sizes
            if size
            and size.strip()
            and size.strip().lower() not in [
                "none",
                "85 cm",
                "standard"
            ]
        ]
        # Size
        if valid_sizes:
            if (
                not selected_size
                or selected_size.lower() in [
                    "none",
                    "85 cm",
                    "standard"
                ]
            ):
                selected_size = valid_sizes[0]
        else:
            selected_size = ""
        # Stock
        if not product.in_stock or product.stock < 1:
            return Response({"success": False,"message": f"Sorry, '{product.productname}' is currently out of stock!"},status=status.HTTP_400_BAD_REQUEST)
        # Existing cart item
        cart_item = Cart.objects.filter(userid=request.user,product_id=product,selected_size=selected_size).first()
        if cart_item:
            cart_item.quantity += 1
            if cart_item.quantity > product.stock:
                return Response(
                    {
                        "success": False,
                        "message": f"Only {product.stock} item(s) available in stock.",
                        "stock": product.stock,
                        "quantity": cart_item.quantity - 1
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            cart_item.save(update_fields=["quantity"])
            message = (
                f"'{product.producttitle}' "
                f"({selected_size}) in your cart."
                if selected_size
                else
                f"'{product.producttitle}' in your cart."
            )
            return Response(
                {
                    "success": True,
                    "message": message,
                    "action": "quantity_updated",
                    "cart_item": {
                        "id": cart_item.pk,
                        "productviewid": product.productviewid,
                        "productname": product.productname,
                        "producttitle": product.producttitle,
                        "selected_size": selected_size,
                        "quantity": cart_item.quantity,
                    }
                },status=status.HTTP_200_OK)
        # New cart item
        cart_item = Cart.objects.create(
            userid=request.user,
            product_id=product,
            quantity=1,
            selected_size=selected_size
        )
        message = (
            f"'{product.producttitle}' "
            f"({selected_size}) added to your cart."
            if selected_size
            else
            f"'{product.producttitle}' added to your cart."
        )
        return Response(
            {
                "success": True,
                "message": message,
                "action": "added",
                "cart_item": {
                    "id": cart_item.pk,
                    "productviewid": product.productviewid,
                    "productname": product.productname,
                    "producttitle": product.producttitle,
                    "selected_size": selected_size,
                    "quantity": cart_item.quantity,
                }
            },status=status.HTTP_201_CREATED)
class RemoveCartAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, cartid):
        cart_item = get_object_or_404(Cart,cartid=cartid)
        if cart_item.userid != request.user:
            return Response({"success": False,"message": "Sorry, you don't have permission to remove this item."},status=status.HTTP_403_FORBIDDEN)
        cart_item.delete()
        return Response({"success": True,"message": "Item has been removed from your cart."},status=status.HTTP_200_OK)
class PlusCartAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, cartid):
        cart_item = get_object_or_404(Cart,cartid=cartid,userid=request.user)
        product = cart_item.product_id
        if not product.in_stock or product.stock < 1:
            return Response({"success": False,"message": f"'{product.productname}' is currently out of stock."},status=status.HTTP_400_BAD_REQUEST)
        if cart_item.quantity >= product.stock:
            return Response(
                {
                    "success": False,
                    "message": f"Only {product.stock} item(s) available in stock.",
                    "quantity": cart_item.quantity,
                    "stock": product.stock
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        cart_item.quantity += 1
        cart_item.save(update_fields=["quantity"])
        return Response(
            {
                "success": True,
                "message": "Cart quantity increased.",
                "cart_item": {
                    "cartid": cart_item.cartid,
                    "quantity": cart_item.quantity
                }
            },status=status.HTTP_200_OK)
class MinusCartAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, cartid):
        cart_item = get_object_or_404(Cart,cartid=cartid,userid=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save(update_fields=["quantity"])
            return Response(
                {
                    "success": True,
                    "message": "Cart quantity decreased.",
                    "cart_item": {
                        "cartid": cart_item.cartid,
                        "quantity": cart_item.quantity
                    }
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "success": False,
                "message": "Quantity cannot be less than 1.",
                "cart_item": {
                    "cartid": cart_item.cartid,
                    "quantity": cart_item.quantity
                }
            },status=status.HTTP_400_BAD_REQUEST)
class CartDeleteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, cart_id):
        try:
            cart_item = Cart.objects.get(cartid=cart_id,userid=request.user)
        except Cart.DoesNotExist:
            return Response({"message": "Cart item not found."},status=status.HTTP_404_NOT_FOUND)
        cart_item.delete()
        return Response({"message": "Product removed from cart successfully."},status=status.HTTP_200_OK)
class ApplyCouponAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        code = request.data.get("coupon_code", "").strip()
        if not code:
            return Response({"message": "coupon_code is required."},status=status.HTTP_400_BAD_REQUEST)
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return Response({"message": "Invalid coupon code."},status=status.HTTP_404_NOT_FOUND)
        now = timezone.now()
        if not coupon.active or not (coupon.valid_from <= now <= coupon.valid_to):
            return Response({"message": "Coupon is expired or inactive."},status=status.HTTP_400_BAD_REQUEST)
        already_used = CouponUsage.objects.filter(coupon=coupon,user=request.user).exists()
        if already_used:
            return Response({"message": (f"You have already used coupon "f"'{coupon.code}'. ""This coupon can only be used once per user.")},status=status.HTTP_400_BAD_REQUEST)
        cart_items = Cart.objects.filter(userid=request.user)
        if not cart_items.exists():
            return Response({"message": "Your cart is empty."},status=status.HTTP_400_BAD_REQUEST)
        subtotal = sum(item.subtotal() for item in cart_items)
        if subtotal < coupon.minimum_amount:
            return Response({"message": (f"Minimum cart total required "f"for this coupon is "f"₹{coupon.minimum_amount}.")},status=status.HTTP_400_BAD_REQUEST)
        discount_amount = int((subtotal * coupon.discount) / 100)
        final_total = max(0,subtotal - discount_amount)
        request.session["coupon_code"] = coupon.code
        request.session["coupon_discount"] = discount_amount
        return Response(
            {
                "message": "Coupon applied successfully.",
                "coupon_code": coupon.code,
                "discount_percentage": coupon.discount,
                "subtotal": subtotal,
                "discount_amount": discount_amount,
                "final_total": final_total
            },status=status.HTTP_200_OK)
class RemoveCouponAPIView(APIView):
    def post(self, request, *args, **kwargs):
        request.session.pop("coupon_code", None)
        request.session.pop("coupon_discount", None)
        return Response({"message": "Coupon removed successfully."},status=status.HTTP_200_OK,)
class CheckoutAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cartdata = Cart.objects.filter(userid=request.user).order_by("-cartid")
        if not cartdata.exists():
            return Response({"success": False,"message": "Your cart is empty! Please add products first."},status=status.HTTP_400_BAD_REQUEST)
        subtotal = sum(
            item.subtotal()
            for item in cartdata
        )
        deliverycharge = 30 if 0 < subtotal < 300 else 0
        coupon_code = (
            request.data.get("coupon_code")
            or request.session.get("coupon_code", "")
        )
        coupon_code = str(coupon_code).strip()
        discount = request.session.get("coupon_discount",0)
        coupon = None
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code__iexact=coupon_code)
            except Coupon.DoesNotExist:
                coupon = None
        total = subtotal - discount + deliverycharge
        if total < 0:
            total = 0
        firstname = request.data.get("firstname")
        lastname = request.data.get("lastname")
        email = request.data.get("email")
        number = request.data.get("number")
        address = request.data.get("address")
        paymentmethod = request.data.get("paymentmethod")
        if not firstname:
            return Response({"success": False,"message": "Firstname is required."},status=status.HTTP_400_BAD_REQUEST)
        if not lastname:
            return Response({"success": False,"message": "Lastname is required."},status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({"success": False,"message": "Email is required."},status=status.HTTP_400_BAD_REQUEST)
        if not number:
            return Response({"success": False,"message": "Phone number is required."},status=status.HTTP_400_BAD_REQUEST)
        if not address:
            return Response({"success": False,"message": "Address is required."},status=status.HTTP_400_BAD_REQUEST)
        if not paymentmethod:
            return Response({"success": False,"message": "Payment method is required."},status=status.HTTP_400_BAD_REQUEST)
        tracker_status, created = Otracker.objects.get_or_create(status="conformorder")
        try:
            order = Order.objects.create(
                orderstatus="Pending",
                otracker_id=tracker_status,
                user_id=request.user,
                firstname=firstname,
                lastname=lastname,
                email=email,
                number=number,
                username=request.user.username,
                address=address,
                subtotal=subtotal,
                deliverycharges=deliverycharge,
                total=total,
                paymentmethod=paymentmethod,
                coupon=coupon,
                coupon_discount=discount,
            )
            user_order_no = Order.objects.filter(user_id=request.user,orderid__lte=order.orderid,).count()
            order.amazon_order_id = (f"ORD{user_order_no:05d}")
            order.save(update_fields=["amazon_order_id"])
            order_items = []
            for item in cartdata:
                Orderitem.objects.create(
                    status="Pending",
                    productview_id=item.product_id,
                    order_id=order,
                    quantity=item.quantity,
                    selected_size=item.selected_size,
                )
                product = item.product_id
                product.sold_count += item.quantity
                product.save(update_fields=["sold_count"])
                order_items.append(
                    {
                        "productviewid": product.productviewid,
                        "productname": product.productname,
                        "producttitle": product.producttitle,
                        "quantity": item.quantity,
                        "selected_size": item.selected_size,
                    }
                )
            request.session["order_just_placed_id"] = order.orderid
            return Response(
                {
                    "success": True,
                    "message": "Please review your order details before placing the order.",
                    "order": {
                        "orderid": order.orderid,
                        "amazon_order_id": order.amazon_order_id,
                        "orderstatus": order.orderstatus,
                        "firstname": order.firstname,
                        "lastname": order.lastname,
                        "email": order.email,
                        "number": order.number,
                        "address": order.address,
                        "paymentmethod": order.paymentmethod,
                        "subtotal": subtotal,
                        "deliverycharges": deliverycharge,
                        "coupon_code": coupon_code,
                        "coupon_discount": discount,
                        "total": total,
                        "items": order_items,
                    }
                },status=status.HTTP_201_CREATED)
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"success": False,"message": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ConfirmOrderAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, orderid):
        order = get_object_or_404(Order, orderid=orderid, user_id=request.user)
        order_items = Orderitem.objects.filter(order_id=order).select_related("productview_id")
        user_order_no = Order.objects.filter(user_id=request.user, orderid__lte=order.orderid).count()
        order.amazon_order_id = f"{user_order_no:05d}"
        order.save(update_fields=["amazon_order_id"])
        expected_delivery = order.date + timedelta(days=2)
        if order.coupon:
            coupon_code = order.coupon.code
            discount = order.coupon_discount
        else:
            coupon_code = ""
            discount = 0
        items = []
        for item in order_items:
            product = item.productview_id
            size_value = item.selected_size if item.selected_size else "N/A"
            items.append(
                {
                    "orderitemid": item.pk,
                    "productviewid": product.productviewid,
                    "productname": product.productname,
                    "producttitle": product.producttitle,
                    "quantity": item.quantity,
                    "selected_size": size_value,
                    "status": item.status,
                }
            )
        return Response(
            {
                "success": True,
                "order": {
                    "orderid": order.orderid,
                    "amazon_order_id": order.amazon_order_id,
                    "orderstatus": order.orderstatus,
                    "firstname": order.firstname,
                    "lastname": order.lastname,
                    "email": order.email,
                    "number": order.number,
                    "username": order.username,  # Cleaned duplicate key
                    "address": order.address,
                    "subtotal": order.subtotal,
                    "deliverycharges": order.deliverycharges,
                    "coupon_code": coupon_code,
                    "coupon_discount": discount,
                    "total": order.total,
                    "paymentmethod": order.paymentmethod,
                    "order_date": order.date,
                    "expected_delivery": expected_delivery,
                    "items": items,
                },
            },status=status.HTTP_200_OK,)
class PlaceOrderAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        order_id = request.data.get("orderid") or request.session.get("order_just_placed_id")
        if not order_id:
            return Response({"success": False, "message": "No order found."}, status=status.HTTP_400_BAD_REQUEST)
        order = get_object_or_404(Order, orderid=order_id, user_id=request.user)
        order.orderstatus = "Pending"
        coupon_code = request.data.get("coupon_code") or request.session.get("coupon_code", "")
        discount_amount = 0
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code__iexact=coupon_code)
                now = timezone.now()
                if coupon.active and (coupon.valid_from <= now <= coupon.valid_to) and (order.subtotal >= coupon.minimum_amount):
                    discount_amount = int((order.subtotal * coupon.discount) / 100)
                    order.coupon = coupon
                    order.coupon_discount = discount_amount
                else:
                    coupon_code = ""
                    order.coupon = None
                    order.coupon_discount = 0
            except Coupon.DoesNotExist:
                coupon_code = ""
                order.coupon = None
                order.coupon_discount = 0
        else:
            order.coupon = None
            order.coupon_discount = 0
        order.save()
        email_sent = False
        try:
            context = {
                "user": request.user,
                "order": order,
                "order_items": order.orderitem_set.all(),
                "coupon_code": coupon_code,
                "discount": order.coupon_discount,
            }
            html_content = render_to_string("emails/order_confirmation.html", context)
            email = EmailMultiAlternatives(
                subject=f"Your Order #{order.amazon_order_id} has been placed!",
                body="Your order has been placed successfully.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[order.email],
            )
            email.attach_alternative(html_content, "text/html")
            logo_path = os.path.join(settings.BASE_DIR, "static", "IMAGES", "79e44a35-def7-4146-8642-961f01c9dea4.png")
            if os.path.exists(logo_path):
                with open(logo_path, "rb") as f:
                    logo = MIMEImage(f.read())
                    logo.add_header("Content-ID", "<logo>")
                    logo.add_header("Content-Disposition", "inline", filename="logo.png")
                    email.attach(logo)
            email.send(fail_silently=False)
            email_sent = True
        except Exception as e:
            print("Order email error:", str(e))
        Cart.objects.filter(userid=request.user).delete()
        request.session.pop("coupon_code", None)
        request.session.pop("coupon_discount", None)
        request.session.pop("order_just_placed_id", None)
        return Response(
            {
                "success": True,
                "message": "Your order has been placed successfully.",
                "order": {
                    "orderid": order.orderid,
                    "amazon_order_id": order.amazon_order_id,
                    "orderstatus": order.orderstatus,
                    "subtotal": order.subtotal,
                    "coupon_discount": order.coupon_discount,
                    "deliverycharges": order.deliverycharges,
                    "total": order.total,
                    "paymentmethod": order.paymentmethod,
                    "coupon_code": coupon_code,
                    "email": order.email,
                },
                "email_sent": email_sent
            },status=status.HTTP_200_OK)
class CancelOrderItemAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, orderitemid):
        order_item = get_object_or_404(Orderitem,orderitemid=orderitemid,order_id__user_id=request.user)
        order = order_item.order_id
        if request.session.get("order_just_placed_id") == order.orderid:
            return Response({"success": False,"message": "Please place your order first. You cannot cancel products during checkout."},status=status.HTTP_400_BAD_REQUEST)
        if order.orderstatus in ["Shipped", "Delivered", "Cancelled"]:
            return Response(
                {"success": False,"message": f"Item cannot be cancelled as order status is {order.orderstatus}."},status=status.HTTP_400_BAD_REQUEST)
        cancelled_product = order_item.productview_id
        cancelled_product_name = cancelled_product.producttitle
        cancelled_quantity = order_item.quantity
        cancelled_price = cancelled_product.productprice * cancelled_quantity
        product_image_url = getattr(cancelled_product, "productimage1", None)
        cancelled_product.stock += cancelled_quantity
        cancelled_product.save()
        order_item.delete()
        remaining_items = Orderitem.objects.filter(order_id=order)
        subtotal = sum(item.productview_id.productprice * item.quantity for item in remaining_items)
        order.subtotal = subtotal
        order.deliverycharges = 30 if (0 < subtotal < 300) else 0
        if order.coupon:
            if subtotal >= order.coupon.minimum_amount:
                order.coupon_discount = int((subtotal * order.coupon.discount) / 100)
            else:
                order.coupon = None
                order.coupon_discount = 0
        else:
            order.coupon_discount = 0
        if not remaining_items.exists():
            order.orderstatus = "Cancelled"
            order.cancelled_at = timezone.now()
        order.save()
        if order.email:
            try:
                context = {
                    "user": request.user,
                    "order": order,
                    "product_name": cancelled_product_name,
                    "quantity": cancelled_quantity,
                    "price": cancelled_price,
                    "cancel_date": timezone.localtime().strftime("%d-%m-%Y %I:%M %p"),
                    "remaining_total": order.total,
                    "refund_amount": cancelled_price,
                }
                html_content = render_to_string("emails/order_cancelled.html", context)
                email = EmailMultiAlternatives(
                    subject=f"Order Cancellation - {order.amazon_order_id}",
                    body="Your product has been cancelled successfully.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[order.email],
                )
                email.attach_alternative(html_content, "text/html")
                logo_path = os.path.join(settings.BASE_DIR, "static", "IMAGES", "79e44a35-def7-4146-8642-961f01c9dea4.png")
                if os.path.exists(logo_path):
                    with open(logo_path, "rb") as f:
                        logo = MIMEImage(f.read())
                        logo.add_header("Content-ID", "<logo>")
                        logo.add_header("Content-Disposition", "inline", filename="logo.png")
                        email.attach(logo)
                if product_image_url:
                    try:
                        response = requests.get(product_image_url, timeout=10)
                        if response.status_code == 200:
                            product_img = MIMEImage(response.content)
                            product_img.add_header("Content-ID", "<product>")
                            product_img.add_header("Content-Disposition", "inline", filename="product.jpg")
                            product_img.add_header("X-Attachment-Id", "product")
                            email.attach(product_img)
                    except Exception as img_error:
                        print("❌ Product Image Attachment Error:", img_error)
                email.send(fail_silently=False)
            except Exception as e:
                print("❌ Cancellation email error:", str(e))
                traceback.print_exc()
        return Response(
            {
                "success": True,
                "message": "Item cancelled successfully.",
                "cancelled_item": {
                    "product_name": cancelled_product_name,
                    "quantity": cancelled_quantity,
                    "price": cancelled_price,
                },
                "order_summary": {
                    "orderid": order.orderid,
                    "subtotal": order.subtotal,
                    "coupon_discount": order.coupon_discount,
                    "deliverycharges": order.deliverycharges,
                    "total": order.total,
                    "orderstatus": order.orderstatus,
                },
            },status=status.HTTP_200_OK,)
class ThankYouAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, orderid):
        order = get_object_or_404(Order, orderid=orderid, user_id=request.user)
        return Response(
            {
                "success": True,
                "message": "Thank you for your order!",
                "order": {
                    "orderid": order.orderid,
                    "amazon_order_id": order.amazon_order_id,
                    "orderstatus": order.orderstatus,
                    "paymentstatus": order.paymentstatus,
                    "paymentmethod": order.paymentmethod,
                    "firstname": order.firstname,
                    "username":order.username,
                    "lastname": order.lastname,
                    "email": order.email,
                    "number": order.number,
                    "address": order.address,
                    "subtotal": order.subtotal,
                    "coupon_discount": order.coupon_discount,
                    "deliverycharges": order.deliverycharges,
                    "total": order.total,
                    "date": order.date,
                },
            },status=status.HTTP_200_OK,)
class ViewBillAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, orderid):
        order = get_object_or_404(Order, orderid=orderid, user_id=request.user)
        orderitems = Orderitem.objects.filter(order_id=order)
        user_order_no = Order.objects.filter(user_id=request.user, orderid__lte=order.orderid).count()
        amazon_order_id = f"{user_order_no:05d}"
        items_data = []
        for item in orderitems:
            product = getattr(item, "productview_id", None) or getattr(item, "product_id", None) or getattr(item, "product", None)
            p_title = getattr(product, "producttitle", "") if product else ""
            p_price = getattr(product, "productprice", 0) if product else 0
            p_image = getattr(product, "productimage1", "") if product else ""
            p_id = getattr(product, "productid", None) if product else None
            items_data.append(
                {
                    "orderitemid": item.orderitemid,
                    "product_id": p_id,
                    "product_title": p_title,
                    "product_price": p_price,
                    "product_image": p_image,
                    "quantity": item.quantity,
                    "item_subtotal": p_price * item.quantity,
                }
            )
        return Response(
            {
                "success": True,
                "order": {
                    "orderid": order.orderid,
                    "amazon_order_id": amazon_order_id,
                    "orderstatus": order.orderstatus,
                    "paymentstatus": order.paymentstatus,
                    "paymentmethod": order.paymentmethod,
                    "customer_name": f"{order.firstname} {order.lastname}",
                    "email": order.email,
                    "number": order.number,
                    "address": order.address,
                    "subtotal": order.subtotal,
                    "coupon_code": order.coupon.code if order.coupon else None,
                    "coupon_discount": order.coupon_discount,
                    "deliverycharges": order.deliverycharges,
                    "total": order.total,
                    "date": order.date,
                },
                "orderitems": items_data,
            },status=status.HTTP_200_OK,)
class MyOrdersAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(user_id=request.user).order_by("-date")
        orders_data = []
        for order in orders:
            amazon_order_id = order.amazon_order_id
            if not amazon_order_id:
                seq = getattr(order, "user_order_seq", None) or order.orderid
                amazon_order_id = f"ORD{seq:05d}"
            return_last_date = None
            if order.orderstatus == "Delivered" and order.delivered_at:
                return_last_date = order.delivered_at + timedelta(days=7)
            if order.paymentmethod == "Cash on Delivery" and order.orderstatus == "Delivered":
                payment_status_display = "Paid"
            elif order.paymentstatus == "Paid":
                payment_status_display = "Paid"
            else:
                payment_status_display = "Pending"
            coupon_code_display = None
            coupon_discount_display = 0
            if order.coupon:
                if hasattr(order.coupon, "code"):
                    coupon_code_display = order.coupon.code
                else:
                    coupon_code_display = str(order.coupon)
                coupon_discount_display = order.coupon_discount or 0
            order_items = Orderitem.objects.filter(order_id=order)
            items_list = []
            for item in order_items:
                product = getattr(item, "productview_id", None) or getattr(item, "product_id", None) or getattr(item, "product", None)
                p_id = (
                    getattr(product, "productid", None)
                    or getattr(product, "productviewid", None)
                    or getattr(product, "id", None)
                    if product
                    else None
                )
                p_title = getattr(product, "producttitle", "") if product else ""
                p_price = getattr(product, "productprice", 0) if product else 0
                p_image = getattr(product, "productimage1", "") if product else ""
                items_list.append({
                    "orderitemid": item.orderitemid,
                    "product_id": p_id,
                    "product_title": p_title,
                    "product_price": p_price,
                    "product_image": p_image,
                    "quantity": item.quantity,
                    "item_subtotal": p_price * item.quantity,
                })
            orders_data.append({
                "orderid": order.orderid,
                "amazon_order_id": amazon_order_id,
                "orderstatus": order.orderstatus,
                "paymentstatus": order.paymentstatus,
                "payment_status_display": payment_status_display,
                "paymentmethod": order.paymentmethod,
                "date": order.date,
                "delivered_at": order.delivered_at,
                "return_last_date": return_last_date,
                "subtotal": order.subtotal,
                "deliverycharges": order.deliverycharges,
                "coupon_code": coupon_code_display,
                "coupon_discount": coupon_discount_display,
                "total": order.total,
                "shipping_address": {
                    "firstname": order.firstname,
                    "username":order.username,
                    "lastname": order.lastname,
                    "email": order.email,
                    "number": order.number,
                    "address": order.address,
                },
                "items_count": len(items_list),
                "items": items_list,
            })
        return Response({"success": True,"count": len(orders_data),"orders": orders_data},status=status.HTTP_200_OK)
class UpdateOrderStatusAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]  
    def patch(self, request, orderid):
        new_status = request.data.get("status")
        if not new_status:
            return Response({"error": "'status' is required in request body."},status=status.HTTP_400_BAD_REQUEST,)
        order = get_object_or_404(Order, orderid=orderid)
        old_status = order.orderstatus
        order.orderstatus = new_status
        if (
            new_status == "Delivered"
            and old_status != "Delivered"
            and not order.stock_updated
        ):
            order_items = order.orderitem_set.select_related(
                "productview_id"
            ).all()
            with transaction.atomic():
                for item in order_items:
                    product = item.productview_id
                    quantity = item.quantity or 0
                    if quantity <= 0:
                        continue
                    product.stock = max(0, product.stock - quantity)
                    product.sold_count = (product.sold_count or 0) + quantity
                    product.in_stock = product.stock > 0
                    product.save(update_fields=["stock", "sold_count", "in_stock"])
                order.stock_updated = True
                order.save(update_fields=["orderstatus", "stock_updated"])
        else:
            order.save(update_fields=["orderstatus"])
        Orderitem.objects.filter(order_id=order).update(status=new_status)
        if (
            new_status == "Delivered"
            and old_status != "Delivered"
            and order.user_id
            and order.user_id.email
        ):
            try:
                user = order.user_id
                context = {
                    "user": user,
                    "username": user.username,
                    "order": order,
                    "order_items": order.orderitem_set.all(),
                }
                html_content = render_to_string("emails/order_delivered.html", context)
                email = EmailMultiAlternatives(
                    subject=f"Your Order #{order.amazon_order_id} has been delivered!",
                    body=(
                        f"Hello {user.username},\n\n"
                        f"Your order #{order.amazon_order_id} has been successfully delivered.\n\n"
                        "Thank you for shopping with EiserShop.\n\n"
                        "Regards,\nEiserShop Team"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[order.email],
                )
                email.attach_alternative(html_content, "text/html")
                logo_path = os.path.join(
                    settings.BASE_DIR,
                    "static",
                    "IMAGES",
                    "79e44a35-def7-4146-8642-961f01c9dea4.png",
                )
                if os.path.exists(logo_path):
                    with open(logo_path, "rb") as f:
                        logo = MIMEImage(f.read())
                    logo.add_header("Content-ID", "<logo>")
                    logo.add_header("Content-Disposition", "inline", filename="logo.png")
                    email.attach(logo)
                email.send(fail_silently=False)
            except Exception as e:
                print("Delivered order email error:", str(e))
                traceback.print_exc()
        return Response(
            {
                "success": True,
                "message": f"Order {orderid} status updated to '{new_status}' successfully.",
                "orderid": order.orderid,
                "status": order.orderstatus,
            },status=status.HTTP_200_OK,)
class ReturnOrderAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    NO_SIZE_CATEGORIES = [
        "wallet",
        "suitcase",
        "earbuds",
        "earbud",
        "headphone",
        "headphones",
    ]
    def get_category_name(self, product):
        if product and getattr(product, "category_id", None):
            return product.category_id.categoryname.strip().lower()
        return ""
    def post(self, request, orderitemid):
        order_item = get_object_or_404(
            Orderitem.objects.select_related("order_id","productview_id","productview_id__category_id",),orderitemid=orderitemid,order_id__user_id=request.user,)
        order = order_item.order_id
        product = order_item.productview_id
        if order.orderstatus != "Delivered":
            return Response({"success": False,"message": "Only delivered orders can be returned.",},status=status.HTTP_400_BAD_REQUEST,)
        if ReturnRequest.objects.filter(orderitem=order_item).exists():
            return Response({"success": False,"message": "Return request already submitted.",},status=status.HTTP_400_BAD_REQUEST,)
        delivered_date = (
            getattr(order, "delivered_at", None)
            or getattr(order, "updated_at", None)
            or getattr(order, "created_at", None)
        )
        if not delivered_date and order.orderstatus == "Delivered":
            delivered_date = timezone.now()
        elif not delivered_date:
            return Response({"success": False, "message": "Delivery date not found."},status=status.HTTP_400_BAD_REQUEST,)
        expiry_date = delivered_date + timedelta(days=7)
        if timezone.now() > expiry_date:
            return Response({"success": False,"message": "Return period has expired.","return_expiry": expiry_date,},status=status.HTTP_400_BAD_REQUEST,)
        reason = request.data.get("reason")
        comments = request.data.get("comments", "")
        if not reason:
            return Response({"success": False,"message": "Please select a return reason.",},status=status.HTTP_400_BAD_REQUEST,)
        category_name = self.get_category_name(product)
        if category_name in self.NO_SIZE_CATEGORIES and reason == "Size Issue":
            return Response({"success": False,"message": f"Size Issue is not applicable for {category_name} products.",},status=status.HTTP_400_BAD_REQUEST,)
        final_reason = (f"{reason} - {comments}".strip(" -") if comments else reason)
        return_request = ReturnRequest.objects.create(
            order=order,
            orderitem=order_item,
            reason=final_reason,
            status="Requested",
        )
        order_item.status = "Return Requested"
        order_item.save(update_fields=["status"])
        return Response(
            {
                "success": True,
                "message": "Return request submitted successfully.",
                "data": {
                    "return_request_id": return_request.pk,
                    "order_id": getattr(
                        order, "amazon_order_id", order.orderid
                    ),
                    "orderitemid": order_item.orderitemid,
                    "reason": final_reason,
                    "status": return_request.status,
                    "delivered_date": delivered_date,
                    "return_expiry": expiry_date,
                },
            },status=status.HTTP_201_CREATED,)
class RejectReturnAPIView(APIView):
    permission_classes = [IsAdminUser]  
    def post(self, request, pk):
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Rejected"
        return_request.save()
        return Response(
            {
                "success": True,
                "message": "Return request rejected.",
                "status": return_request.status
            },status=status.HTTP_200_OK)
class ApproveReturnView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request, pk):
        if not request.user.is_staff:
            return redirect("login")
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Approved"
        return_request.approved_at = timezone.now()
        return_request.save()
        messages.success(request, "Return request approved successfully.")
        return redirect("admin_dashboard")
class AssignPickupAgentAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        agent_id = request.data.get("pickup_agent")
        if not agent_id:
            return Response({"error": "pickup_agent field is required in request body."},status=status.HTTP_400_BAD_REQUEST)
        pickup_agent = get_object_or_404(PickupAgent, pk=agent_id, is_active=True)
        return_request.delivery_agent = pickup_agent
        return_request.status = "Agent Assigned"
        return_request.save()
        order_obj = getattr(return_request, 'order', None) or getattr(getattr(return_request, 'orderitem', None), 'order', None)
        customer_name = "Customer"
        address_text = ""
        if order_obj:
            user_field = getattr(order_obj, 'user', None) or getattr(order_obj, 'user_id', None)
            if hasattr(user_field, 'username'):
                customer_name = user_field.username
            elif isinstance(user_field, str):
                customer_name = user_field
            address_text = getattr(order_obj, 'address', '')
        send_mail(
            subject="New Pickup Assigned",
            message=f"""
Hello {pickup_agent.user.first_name or pickup_agent.user.username},
A new return pickup has been assigned to you.
Customer: {customer_name}
Address:
{address_text}
Please login to your Pickup Dashboard:
http://127.0.0.1:8000/pickup-login/
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[pickup_agent.user.email],
            fail_silently=False,
        )
        return Response(
            {
                "success": True,
                "message": "Pickup Agent Assigned Successfully.",
                "agent_assigned": pickup_agent.pk,
                "status": return_request.status
            },status=status.HTTP_200_OK)
class PickupDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        returns = ReturnRequest.objects.filter(delivery_agent=pickup_agent).order_by('-id')
        data = []
        for item in returns:
            order_item = getattr(item, 'orderitem', None) or getattr(item, 'order_item', None)
            product_name = "N/A"
            if order_item:
                product_obj = getattr(order_item, 'productview_id', None) or getattr(order_item, 'productview', None) or getattr(order_item, 'product', None)
                if product_obj:
                    product_name = getattr(product_obj, 'product_name', None) or str(product_obj)
            order_obj = None
            if order_item:
                order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
            if not order_obj:
                order_obj = getattr(item, 'order', None)
            customer_name = "N/A"
            if order_obj:
                user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
                if user_obj:
                    first_name = getattr(user_obj, 'first_name', '').strip()
                    username = getattr(user_obj, 'username', '').strip()
                    last_name = getattr(user_obj, 'last_name', '').strip()
                    name_parts = [part for part in [first_name, f"{username}" if username else "", last_name] if part]
                    customer_name = " ".join(name_parts) if name_parts else "N/A"
            address = "N/A"
            if order_obj:
                address = getattr(order_obj, 'address', 'N/A')
            data.append({
                "return_id": item.id,
                "status": item.status,
                "reason": item.reason,
                "product_name": product_name,
                "customer_name": customer_name,
                "address": str(address),
                "pickup_otp_verified": getattr(item, 'pickup_otp_verified', False)
            })
        return Response({
            "agent_name": pickup_agent.user.username,
            "vehicle_number": getattr(pickup_agent, 'vehicle_number', ''),
            "assigned_returns_count": len(data),
            "returns": data
        }, status=status.HTTP_200_OK)
class AcceptPickupRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest, pk=pk, delivery_agent=pickup_agent)
        return_request.status = "Accepted by Pickup Agent"
        otp = str(random.randint(1000, 9999))
        return_request.pickup_otp = otp
        return_request.save()
        order_item = getattr(return_request, 'orderitem', None) or getattr(return_request, 'order_item', None) 
        order_obj = None
        if order_item:
            order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
        if not order_obj:
            order_obj = getattr(return_request, 'order', None)
        user_obj = None
        if order_obj:
            user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
        customer_email = getattr(user_obj, 'email', None) if user_obj else None
        customer_name = "Customer"
        if user_obj:
            first = getattr(user_obj, 'first_name', '').strip()
            last = getattr(user_obj, 'last_name', '').strip()
            username = getattr(user_obj, 'username', '').strip()
            full_name = " ".join([f for f in [first, last] if f])
            customer_name = full_name if full_name else username or "Customer"
        if customer_email:
            send_mail(
                subject="Pickup Scheduled & OTP for Return",
                message=f"""Hello {customer_name},
Your return request has been accepted by Pickup Agent: {pickup_agent.user.username}.
Your 4-Digit Verification OTP is: {otp}
Please share this OTP with the agent only when they arrive to collect the item.
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer_email],
                fail_silently=False,
            )
        return Response({
            "success": True,
            "message": "Pickup request accepted and OTP sent to customer successfully.",
            "status": return_request.status
        }, status=status.HTTP_200_OK)
class PickupAgentLoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"error": "Username and password both are required."},status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user:
            if PickupAgent.objects.filter(user=user).exists():
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "success": True,
                    "message": "Login successful.",
                    "token": token.key,
                    "username": user.username,
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "You are not registered as a Pickup Agent."},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Invalid login credentials."},status=status.HTTP_401_UNAUTHORIZED)
class SendPickupOTPAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest, pk=pk, delivery_agent=pickup_agent)
        if hasattr(return_request, 'generate_pickup_otp'):
            return_request.generate_pickup_otp()
        else:
            return_request.pickup_otp = str(random.randint(1000, 9999))
        return_request.status = "Out for Pickup"
        return_request.save()
        order_item = getattr(return_request, 'orderitem', None) or getattr(return_request, 'order_item', None)
        order_obj = None
        if order_item:
            order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
        if not order_obj:
            order_obj = getattr(return_request, 'order', None)
        user_obj = None
        if order_obj:
            user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
        customer_email = getattr(user_obj, 'email', None) if user_obj else None
        customer_name = "Customer"
        if user_obj:
            first_name = getattr(user_obj, 'first_name', '').strip()
            username = getattr(user_obj, 'username', '').strip()
            customer_name = first_name or username or "Customer"
        if customer_email:
            send_mail(
                subject="Pickup OTP",
                message=f"""Hello {customer_name},
Your pickup is scheduled.
Pickup OTP: {return_request.pickup_otp}
Please share this OTP with the Pickup Agent after handing over the product.
Thank You.""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer_email],
                fail_silently=False,
            )
        return Response({
            "success": True,
            "message": "Pickup OTP sent successfully.",
            "status": return_request.status,
            "otp": return_request.pickup_otp
        }, status=status.HTTP_200_OK)
class VerifyPickupOTPAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        pickup_agent = get_object_or_404(PickupAgent, user=request.user)
        return_request = get_object_or_404(ReturnRequest, pk=pk, delivery_agent=pickup_agent)
        otp = request.data.get("otp")
        if not otp:
            return Response({"error": "OTP is required."},status=status.HTTP_400_BAD_REQUEST)
        if str(otp) == str(return_request.pickup_otp):
            return_request.pickup_otp_verified = True
            return_request.status = "Pickup Completed"
            if hasattr(return_request, 'pickup_completed_at'):
                return_request.pickup_completed_at = timezone.now()
            return_request.save()
            return Response({
                "success": True,
                "message": "Pickup Completed Successfully.",
                "status": return_request.status
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid OTP. Please enter the correct OTP."},status=status.HTTP_400_BAD_REQUEST)
class RefundInitiatedAPIView(APIView):
    permission_classes = [IsAdminUser]  
    def post(self, request, pk):
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Refund Initiated"
        return_request.save()
        order_item = getattr(return_request, 'orderitem', None) or getattr(return_request, 'order_item', None)
        order_obj = None
        if order_item:
            order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
        if not order_obj:
            order_obj = getattr(return_request, 'order', None)
        user_obj = None
        if order_obj:
            user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
        customer_email = getattr(user_obj, 'email', None) if user_obj else None
        customer_name = getattr(user_obj, 'username', 'Customer') if user_obj else 'Customer'
        if customer_email:
            send_mail(
                subject="Refund Initiated",
                message=f"""Hello {customer_name},
We have successfully received your returned product.
Your refund process has now started.
Thank You.""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer_email],
                fail_silently=False,
            )
        return Response({
            "success": True,
            "message": "Refund Initiated Successfully.",
            "status": return_request.status
        }, status=status.HTTP_200_OK)
class RefundCompletedAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        return_request = get_object_or_404(ReturnRequest, pk=pk)
        return_request.status = "Refunded"
        if hasattr(return_request, 'refund_completed_at'):
            return_request.refund_completed_at = timezone.now()
        return_request.save()
        order_item = getattr(return_request, 'orderitem', None) or getattr(return_request, 'order_item', None)
        order_obj = None
        if order_item:
            order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
        if not order_obj:
            order_obj = getattr(return_request, 'order', None)
        user_obj = None
        if order_obj:
            user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
        customer_email = getattr(user_obj, 'email', None) if user_obj else None
        customer_name = "Customer"
        if user_obj:
            first_name = getattr(user_obj, 'first_name', '').strip()
            username = getattr(user_obj, 'username', '').strip()
            customer_name = first_name or username or "Customer"
        if customer_email:
            send_mail(
                subject="Refund Completed",
                message=f"""Hello {customer_name},
Great News!
Your refund has been successfully completed.
Amount will be credited according to your original payment method.
Thank You for shopping with us.""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer_email],
                fail_silently=False,
            )
        return Response({
            "success": True,
            "message": "Refund Completed Successfully.",
            "status": return_request.status
        }, status=status.HTTP_200_OK)
class AdminRefundedOrdersAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        refunded_requests = ReturnRequest.objects.filter(status="Refunded").order_by("-id")
        data = []
        for r in refunded_requests:
            order_item = getattr(r, 'orderitem', None) or getattr(r, 'order_item', None)
            order_obj = None
            if order_item:
                order_obj = getattr(order_item, 'order_id', None) or getattr(order_item, 'order', None)
            if not order_obj:
                order_obj = getattr(r, 'order', None)
            user_obj = None
            if order_obj:
                user_obj = getattr(order_obj, 'user_id', None) or getattr(order_obj, 'user', None)
            raw_id = 0
            if order_obj:
                raw_id = getattr(order_obj, 'orderid', None) or getattr(order_obj, 'id', 0)
            order_display_id = f"{raw_id:05d}"
            product_name = "N/A"
            if order_item:
                product_obj = getattr(order_item, 'productview_id', None) or getattr(order_item, 'productview', None) or getattr(order_item, 'product', None)
                if product_obj:
                    product_name = getattr(product_obj, 'product_name', None) or str(product_obj)
            customer_name = "Customer"
            customer_email = ""
            if user_obj:
                customer_name = getattr(user_obj, 'username', 'Customer')
                customer_email = getattr(user_obj, 'email', '')
            data.append({
                "return_id": r.id,
                "status": r.status,
                "order_display_id": order_display_id,
                "customer_name": customer_name,
                "customer_email": customer_email,
                "product_name": product_name,
                "refund_completed_at": str(getattr(r, 'refund_completed_at', 'Completed'))
            })
        return Response({
            "success": True,
            "total_refunded": len(data),
            "refunded_orders": data
        }, status=status.HTTP_200_OK)
class PickupLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({
            "success": True,
            "message": "Pickup Agent logged out successfully."
        }, status=status.HTTP_200_OK)
class WishlistAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        wishlist_items = Wishlist.objects.filter(user=request.user).select_related("product","product__category_id").order_by("-created_at")
        serializer = WishlistSerializer(wishlist_items,many=True)
        return Response({"message": "Wishlist fetched successfully.","count": wishlist_items.count(),"wishlist": serializer.data},status=status.HTTP_200_OK)
    def post(self, request):
        product_id = request.data.get("product_id")
        size = request.data.get("size")
        if not product_id:
            return Response({"message": "product_id is required."},status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Productview.objects.get(productviewid=product_id)
        except Productview.DoesNotExist:
            return Response({"message": "Product not found."},status=status.HTTP_404_NOT_FOUND)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user,product=product,defaults={"size": size})
        if not created:
            return Response({"message": "Product already exists in wishlist."},status=status.HTTP_400_BAD_REQUEST)
        serializer = WishlistSerializer(wishlist_item)
        return Response({"message": "Product added to wishlist successfully.","wishlist": serializer.data},status=status.HTTP_201_CREATED)
class WishlistDeleteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, product_id):
        wishlist_item = Wishlist.objects.filter(user=request.user,product__productviewid=product_id).first()
        if not wishlist_item:
            return Response({"message": "Product not found in wishlist."},status=status.HTTP_404_NOT_FOUND)
        wishlist_item.delete()
        return Response({"message": "Product removed from wishlist successfully."},status=status.HTTP_200_OK)
class SearchAPI(APIView):
    def get(self, request, *args, **kwargs):
        raw_query = (request.GET.get("q") or "").strip()
        selected_brands = request.GET.getlist("brand")
        narrow_filter = request.GET.get("narrow_filter")
        queryset = Productview.objects.select_related("category_id").all()
        if raw_query:
            clean_query = re.sub(r"[^\w\s]", "", raw_query)
            normalized_query = re.sub(r"[\s\-\.]", "", raw_query.lower())
            category_map = {
                "shirt": "Shirt",
                "shirts": "Shirt",
                "tshirt": "Tshirt",
                "tshirts": "Tshirt",
                "t-shirt": "Tshirt",
                "t shirt": "Tshirt",
                "shoe": "Shoes",
                "shoes": "Shoes",
                "bag": "Suitcase",
                "bags": "Suitcase",
                "suitcase": "Suitcase",
                "trolley": "Suitcase",
                "wallet": "wallet",
            }
            category_name = category_map.get(normalized_query)
            if category_name:
                # Direct Category Filter + Keyword Search
                queryset = queryset.filter(
                    Q(category_id__categoryname__iexact=category_name)| Q(producttitle__icontains=raw_query)| Q(productname__icontains=raw_query))
                if category_name.lower() == "shirt":
                    queryset = queryset.exclude(Q(producttitle__iregex=r"t[\s\-]?shirt")| Q(productname__iregex=r"t[\s\-]?shirt"))
            else:
                words = raw_query.split()
                search_query = (Q(producttitle__icontains=raw_query)| Q(productname__icontains=raw_query)| Q(category_id__categoryname__icontains=raw_query))
                if clean_query != raw_query:
                    search_query |= Q(producttitle__icontains=clean_query) | Q(productname__icontains=clean_query)
                if words:
                    word_query = Q()
                    for word in words:
                        w_clean = re.sub(r"[^\w]", "", word)
                        w_target = w_clean if w_clean else word
                        word_query &= (Q(producttitle__icontains=w_target)| Q(productname__icontains=w_target)| Q(category_id__categoryname__icontains=w_target))
                    search_query |= word_query
                queryset = queryset.filter(search_query)
            queryset = queryset.distinct()
        if selected_brands:
            brand_query = Q()
            for brand in selected_brands:
                if brand:
                    brand_clean = brand.strip()
                    brand_pattern = r"[\s\-_]*".join([re.escape(c) for c in brand_clean if c.isalnum()])
                    brand_query |= (
                        Q(productname__icontains=brand_clean)| Q(producttitle__icontains=brand_clean)| Q(productname__iregex=brand_pattern)| Q(producttitle__iregex=brand_pattern))
            queryset = queryset.filter(brand_query)
        if narrow_filter:
            queryset = queryset.filter(Q(producttitle__icontains=narrow_filter)| Q(productname__icontains=narrow_filter))
        selected_sizes = request.GET.getlist("size")
        if selected_sizes:
            size_query = Q()
            for size in selected_sizes:
                if size:
                    s_clean = str(size).strip()
                    size_query |= (Q(productsize__iexact=s_clean)| Q(productsize1__iexact=s_clean)| Q(productsize2__iexact=s_clean)| Q(productsize3__iexact=s_clean))
            queryset = queryset.filter(size_query)
        price = request.GET.get("price")
        if price == "0-500":
            queryset = queryset.filter(productprice__lte=500)
        elif price == "500-1000":
            queryset = queryset.filter(productprice__gte=500, productprice__lte=1000)
        elif price == "1000-2000":
            queryset = queryset.filter(productprice__gte=1000, productprice__lte=2000)
        elif price == "2000-5000":
            queryset = queryset.filter(productprice__gte=2000, productprice__lte=5000)
        elif price == "5000-above":
            queryset = queryset.filter(productprice__gte=5000)
        selected_colors = request.GET.getlist("color")
        if selected_colors:
            color_query = Q()
            for color in selected_colors:
                if color:
                    color_clean = str(color).strip()
                    color_query |= Q(productcolor1__icontains=color_clean)
            queryset = queryset.filter(color_query)
        serializer = ProductSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
class LiveSearchAPI(APIView):
    def get(self, request, *args, **kwargs):
        raw_query = (request.GET.get("q") or "").strip()
        selected_brands = request.GET.getlist("brand")
        selected_sizes = request.GET.getlist("size")
        search_filter = Q()
        if raw_query:
            clean_query = re.sub(r"[^\w]", "", raw_query)
            pattern = (
                r"[\s\-_]*".join(
                    [re.escape(c) for c in clean_query if c.isalnum()]
                )
                if clean_query
                else re.escape(raw_query)
            )
            search_filter &= (Q(productname__icontains=raw_query)| Q(producttitle__icontains=raw_query)| Q(productname__iregex=pattern)| Q(producttitle__iregex=pattern)| Q(category_id__categoryname__icontains=raw_query))
        queryset = Productview.objects.filter(search_filter)
        if selected_brands:
            brand_query = Q()
            for brand in selected_brands:
                if brand:
                    b_clean = re.sub(r"[^\w]", "", str(brand)).lower()
                    b_pattern = r"[\s\-_]*".join([re.escape(c) for c in b_clean if c.isalnum()])
                    brand_query |= Q(productname__icontains=brand) | Q(productname__iregex=b_pattern)
            queryset = queryset.filter(brand_query)
        if selected_sizes:
            size_query = Q()
            for size in selected_sizes:
                if size:
                    s_clean = re.sub(r"[^\w]", "", str(size)).lower()
                    s_pattern = r"[\s\-_]*".join(
                        [re.escape(c) for c in s_clean if c.isalnum()]
                    )
                    size_query |= (Q(productsize__iregex=s_pattern)| Q(productsize1__iregex=s_pattern)| Q(productsize2__iregex=s_pattern)| Q(productsize3__iregex=s_pattern))
            queryset = queryset.filter(size_query)
        queryset = queryset.distinct()
        raw_brands = queryset.values_list("productname", flat=True)
        unique_brands = list(
            set(
                [
                    brand.strip()
                    for brand in raw_brands
                    if brand and brand.strip()
                ]
            )
        )
        serializer = ProductSerializer(queryset[:10], many=True, context={"request": request})
        return Response({"products": serializer.data,"brands": unique_brands,},status=status.HTTP_200_OK,)
class BrowsingHistoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        ids = request.session.get("recently_viewed", [])
        products = []
        for pid in ids:
            try:
                product = Productview.objects.get(productviewid=pid)
                apply_rating(product)
                products.append(product)
            except Productview.DoesNotExist:
                pass
        serialized_products = ProductSerializer(products, many=True, context={"request": request}).data
        delivery_date = timezone.localdate() + timedelta(days=8)
        return Response({"products": serialized_products,"delivery_date": delivery_date.strftime("%Y-%m-%d"),},status=status.HTTP_200_OK,)
class RemoveRecentAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        history = request.session.get("recently_viewed", [])
        pk_int = int(pk) if str(pk).isdigit() else pk
        if pk_int in history:
            history.remove(pk_int)
            request.session["recently_viewed"] = history
            request.session.modified = True 
            return Response({"message": f"Product {pk} removed from browsing history successfully.","recently_viewed": history,},status=status.HTTP_200_OK,)
        return Response({"error": "Product not found in browsing history."},status=status.HTTP_404_NOT_FOUND,)

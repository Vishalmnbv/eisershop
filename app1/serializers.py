from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
import urllib.parse
import re
class RegisterSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=150)
    lastname = serializers.CharField(max_length=150, required=False, allow_blank=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    conformpassword = serializers.CharField(write_only=True)
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken")
        return value
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already taken")
        return value
    def validate(self, data):
        if data["password"] != data["conformpassword"]:
            raise serializers.ValidationError({"conformpassword": "Passwords do not match"})
        return data
    def create(self, validated_data):
        validated_data.pop("conformpassword")
        user = User.objects.create_user(
            first_name=validated_data["firstname"],
            last_name=validated_data.get("lastname", ""),
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        Profile.objects.create(user=user)
        return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data
class ProfileSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=150)
    lastname = serializers.CharField(max_length=150,required=False,allow_blank=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    profile_image = serializers.ImageField(required=False,allow_null=True)
class ForgotPasswordSerializer(serializers.Serializer):
    identifier = serializers.CharField()
class ResetPasswordSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    otp = serializers.CharField(max_length=6)
    newpassword = serializers.CharField(write_only=True,min_length=8)
    confirmpassword = serializers.CharField(write_only=True)
    def validate(self, data):
        if data["newpassword"] != data["confirmpassword"]:
            raise serializers.ValidationError({
                "confirmpassword": "Passwords do not match."
            })
        return data
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["categoryid","categoryname",]
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Review
        fields = ["id", "username", "rating", "review", "image", "created_at"]
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category_id.categoryname", read_only=True)
    images = serializers.SerializerMethodField()
    sizes = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    reviews = ReviewSerializer(source="review_set", many=True, read_only=True)
    total_reviews = serializers.SerializerMethodField()
    dynamic_size = serializers.SerializerMethodField()
    dynamic_price = serializers.SerializerMethodField()
    dynamic_mrp = serializers.SerializerMethodField()
    class Meta:
        model = Productview
        fields = [
            "productviewid",
            "category",
            "productname",
            "producttitle",
            "images",
            "productprice",
            "productmrpprice",
            "dynamic_size",
            "dynamic_price",
            "dynamic_mrp",
            "productdiscountrate",
            "sizes",
            "colors",
            "productrating",
            "producttophighlights1",
            "producttophighlights2",
            "producttophighlights3",
            "producttophighlights4",
            "producttophighlights5",
            "producttophighlights6",
            "productaboutitem1",
            "productaboutitem2",
            "productaboutitem3",
            "productaboutitem4",
            "productaboutitem5",
            "productitemdetail1",
            "productitemdetail2",
            "productitemdetail3",
            "productitemdetail4",
            "stock",
            "sold_count",
            "low_stock_alert",
            "in_stock",
            "total_reviews",
            "reviews",
        ]
    def _get_clean_str(self, val):
        if not val:
            return ""
        s = re.sub(r"[^\w]", "", str(val)).lower()
        return " ".join(s.split())
    def _get_matched_price_details(self, obj):
        request = self.context.get("request")
        target_size_clean = ""
        if request:
            raw_sizes = request.GET.getlist("size")
            if raw_sizes:
                target_size_clean = self._get_clean_str(urllib.parse.unquote(raw_sizes[0]))
        size_slots = [
            (obj.productsize, obj.productprice, obj.productmrpprice),
            (obj.productsize1, obj.productprice1, obj.productmrpprice1),
            (obj.productsize2, obj.productprice2, obj.productmrpprice2),
            (obj.productsize3, obj.productprice3, obj.productmrpprice3),
        ]
        if target_size_clean:
            for raw_size, price, mrp in size_slots:
                if raw_size and self._get_clean_str(raw_size) == target_size_clean:
                    final_price = price if price is not None else obj.productprice
                    final_mrp = mrp if mrp is not None else obj.productmrpprice
                    return str(raw_size).strip(), final_price, final_mrp
        return (obj.productsize or "").strip(), obj.productprice, obj.productmrpprice
    def get_dynamic_size(self, obj):
        size_label, _, _ = self._get_matched_price_details(obj)
        return size_label
    def get_dynamic_price(self, obj):
        _, price, _ = self._get_matched_price_details(obj)
        return price
    def get_dynamic_mrp(self, obj):
        _, _, mrp = self._get_matched_price_details(obj)
        return mrp
    def get_total_reviews(self, obj):
        if hasattr(obj, "reviews_count"):
            return obj.reviews_count
        return obj.review_set.count()
    def get_images(self, obj):
        request = self.context.get("request")
        raw_images = [
            obj.productimage1,
            obj.productimage2,
            obj.productimage3,
            obj.productimage4,
            obj.productimage5,
            obj.productimage6,
            obj.productimage7,
            obj.productimage8,
            obj.productimage9,
            obj.productimage10,
        ]
        img_list = []
        for img in raw_images:
            if img:
                url = img.url if hasattr(img, "url") else str(img)
                if request and not url.startswith("http"):
                    url = request.build_absolute_uri(url)
                img_list.append(url)
        return img_list
    def get_sizes(self, obj):
        slots = [
            (obj.productsize, obj.productprice, obj.productmrpprice),
            (obj.productsize1, obj.productprice1 or obj.productprice, obj.productmrpprice1 or obj.productmrpprice),
            (obj.productsize2, obj.productprice2 or obj.productprice, obj.productmrpprice2 or obj.productmrpprice),
            (obj.productsize3, obj.productprice3 or obj.productprice, obj.productmrpprice3 or obj.productmrpprice),
        ]
        size_list = []
        for raw_size, price, mrp in slots:
            if raw_size and str(raw_size).strip().lower() != "none":
                size_list.append({
                    "size": str(raw_size).strip(),
                    "price": price,
                    "mrp": mrp
                })
        return size_list
    def get_colors(self, obj):
        return [
            str(color).strip()
            for color in [
                obj.productcolor1,
                obj.productcolor2,
                obj.productcolor3,
                obj.productcolor4,
                obj.productcolor5,
            ]
            if color and str(color).strip().lower() != "none"
        ]
class WishlistSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.productviewid",read_only=True)
    product_name = serializers.CharField(source="product.productname",read_only=True)
    product_title = serializers.CharField(source="product.producttitle",read_only=True)
    product_price = serializers.IntegerField(source="product.productprice",read_only=True)
    product_mrp_price = serializers.IntegerField(source="product.productmrpprice",read_only=True)
    product_image = serializers.CharField(source="product.productimage1",read_only=True)
    category = serializers.CharField(source="product.category_id.categoryname",read_only=True)
    class Meta:
        model = Wishlist
        fields = [
            "product_id",
            "product_name",
            "product_title",
            "product_price",
            "product_mrp_price",
            "product_image",
            "category",
            "size",
            "created_at",
        ]
class CartSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product_id.productviewid",read_only=True)
    product_name = serializers.CharField(source="product_id.productname",read_only=True)
    product_title = serializers.CharField(source="product_id.producttitle",read_only=True)
    product_image = serializers.CharField(source="product_id.productimage1",read_only=True)
    product_price = serializers.IntegerField(source="product_id.productprice",read_only=True)
    product_mrp_price = serializers.IntegerField(source="product_id.productmrpprice",read_only=True)
    category = serializers.CharField(source="product_id.category_id.categoryname",read_only=True)
    subtotal = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = [
            "cartid",
            "product_id",
            "product_name",
            "product_title",
            "product_image",
            "product_price",
            "product_mrp_price",
            "category",
            "quantity",
            "selected_size",
            "subtotal",
        ]
    def get_subtotal(self, obj):
        return obj.subtotal()
class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="productview_id.productviewid",read_only=True)
    product_name = serializers.CharField(source="productview_id.productname",read_only=True)
    product_title = serializers.CharField(source="productview_id.producttitle",read_only=True)
    product_image = serializers.CharField(source="productview_id.productimage1",read_only=True)
    product_price = serializers.IntegerField(source="productview_id.productprice",read_only=True)
    class Meta:
        model = Orderitem
        fields = [
            "orderitemid",
            "product_id",
            "product_name",
            "product_title",
            "product_image",
            "product_price",
            "quantity",
            "selected_size",
            "status",
        ]
class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            "orderid",
            "amazon_order_id",
            "orderstatus",
            "paymentstatus",
            "firstname",
            "lastname",
            "email",
            "number",
            "username",
            "address",
            "subtotal",
            "deliverycharges",
            "coupon_discount",
            "total",
            "paymentmethod",
            "date",
            "processing_at",
            "shipped_at",
            "delivered_at",
            "cancelled_at",
            "items",
        ]
    def get_items(self, obj):
        items = Orderitem.objects.filter(order_id=obj).select_related("productview_id")
        return OrderItemSerializer(items,many=True).data
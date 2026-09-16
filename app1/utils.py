import math
import os
import traceback
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

def apply_rating(product):
    raw_rating = float(product.productrating or 4.0)
    product.rating = raw_rating
    full_stars = math.floor(raw_rating)
    decimal = raw_rating - full_stars
    if raw_rating == 5.0:
        full_stars = 5
        half_stars = 0
    elif decimal > 0:
        half_stars = 1
    else:
        half_stars = 0
    empty_stars = max(0, 5 - full_stars - half_stars)
    product.full_stars_range = range(full_stars)
    product.half_stars_range = range(half_stars)
    product.empty_stars_range = range(empty_stars)
    
    # Yahan productmrp ki jagah productmrpprice kiya gaya hai
    if (
        product.productmrpprice
        and product.productprice
        and product.productmrpprice > product.productprice
    ):
        discount = (
            (product.productmrpprice - product.productprice)
            / product.productmrpprice
        ) * 100
        product.productdiscountrate = str(int(discount))
    else:
        product.productdiscountrate = "0"
    return product
def send_async_email(recipient_email, subject, html_content):
    try:
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        sender = {"name": "EiserShop", "email": os.getenv("DEFAULT_FROM_EMAIL")}
        to = [{"email": recipient_email}]
        
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            sender=sender,
            subject=subject,
            html_content=html_content
        )
        api_instance.send_transac_email(send_smtp_email)
        print(f"✅ Brevo API Email sent successfully to {recipient_email}")
    except ApiException as e:
        print("❌ Brevo API Error:", repr(e))
        traceback.print_exc()
    except Exception as e:
        print("❌ General Email Error:", str(e))
        traceback.print_exc()
def send_async_login_email(user, html_content):
    send_async_email(user.email, "Login Successful - EiserShop", html_content)
import base64
import json
import hashlib
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from course.models import Bucket



def generate_liqpay_data(bucket, user):
    amount = str(bucket.course.price * bucket.count)
    order_id = bucket.order_id
    print("order_id:", order_id)
    params = {
        "public_key": settings.LIQPAY_API,
        "version": "3",
        "action": "pay",
        "amount": amount,
        "currency": "UAH",
        "description": f"Оплата курсу {bucket.course.title}",
        "order_id": order_id,
        "sandbox": 0,
        "server_url": "http://127.0.0.1:8000/courses/payment/callback/",
        "result_url": "http://127.0.0.1:8000/courses/bucket",

    }

    json_data = json.dumps(params, separators=(',', ':'))
    data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')

    sign_string = settings.LIQPAY_API_SECRET + data + settings.LIQPAY_API_SECRET

    signature = base64.b64encode(
        hashlib.sha1(sign_string.encode('utf-8')).digest()
    ).decode('utf-8')

    return data, signature

#@csrf_exempt
#def liqpay_callback(request):
    data = request.POST.get("data")
    signature = request.POST.get("signature")

    sign_str = settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY
    expected_signature = base64.b64encode(
        hashlib.sha1(sign_str.encode()).digest()
    ).decode()

    if signature != expected_signature:
        return HttpResponse("Invalid signature")

    decoded = base64.b64decode(data).decode()
    payment_data = json.loads(decoded)

    order_id = payment_data.get("order_id")
    status = payment_data.get("status")
    print("order_id:", order_id)
    try:
        bucket = Bucket.objects.get(order_id=order_id)

        if status == "success":
            bucket.payment_status = "success"
            bucket.status = "B"
        else:
            bucket.payment_status = "failed"

        bucket.save()

    except Bucket.DoesNotExist:
        pass

    return HttpResponse("OK")
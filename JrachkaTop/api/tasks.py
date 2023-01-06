import base64
import json

import requests
from api.models import Check
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string


@shared_task(bind=True)
def render_template(self, payload):

    order_id = payload.get("order_id")
    check_id = payload.get("check_id")
    check_type = payload.get("type")
    rendered = render_to_string("check.html", payload)
    check = Check.objects.get(id=check_id)
    check.status = Check.STATUSES.RENDERED
    check.save()

    data_bytes = rendered.encode("ascii")
    base64_bytes = base64.b64encode(data_bytes)
    base64_data = base64_bytes.decode("ascii")
    data = {"contents": base64_data}
    headers = {
        "Content-Type": "application/json",
    }
    url = settings.WKHTMLTOPDF_URL
    response = requests.post(url, data=json.dumps(data), headers=headers)
    with open(f"media/pdf/{order_id}_{check_type}.pdf", "wb") as f:
        f.write(response.content)

    check.status = Check.STATUSES.PRINTED
    check.save()
    return rendered

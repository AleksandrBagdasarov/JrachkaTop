import base64
import json
import logging

import requests
from celery import shared_task
from django.template.loader import render_to_string

LOGGER = logging.getLogger("root")


@shared_task(bind=True)
def render_template(self):
    LOGGER.debug("render template")
    rendered = render_to_string("check.html", {"foo": "bar"})
    data_bytes = rendered.encode("ascii")
    base64_bytes = base64.b64encode(data_bytes)
    base64_data = base64_bytes.decode("ascii")
    headers = {
        "Content-Type": "application/json",
    }
    url = "http://localhost:5000/"
    response = requests.post(
        url, data=json.dumps(base64_data), headers=headers
    )
    with open("123.pdf", "wb") as f:
        f.write(response.content)
    return rendered

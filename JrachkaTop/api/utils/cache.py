import redis
from django.conf import settings

cache = redis.Redis(password=settings.REDIS_REQUIREPASS)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import Redirect


@api_view(['GET'])
def get_redirect(request, key):
  if cache.get(key):
    return Response(cache.get(key))
  else:
    response = Redirect.objects.filter(key=key)
    if response:
      for redirect in response:
        cache.set(key, {"key": key, "url": redirect.url}, 3600)
  return Response(cache.get(key))

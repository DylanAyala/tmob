from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import Redirect


@api_view(['GET'])
def get_redirect(request, key):
  # Retorno el registro de la cache
  if cache.get(key):
    return Response(cache.get(key))
  else:
    # Si no esta en la cache lo busco en la base de datos
    response = Redirect.objects.filter(key=key, active=True)
    if response:
      # Guardo en cache el registro
      for redirect in response:
        cache.set(key, {"key": key, "url": redirect.url}, 3600)
  return Response(cache.get(key))

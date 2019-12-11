from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Redirect
from django.core.cache import cache


@api_view(['GET'])
def get_redirect(request, key):
  return Response(cache.get(key))

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


class BaseManager(models.Manager):
  pass


class Redirect(models.Model):
  key = models.CharField(max_length=100, null=False)
  url = models.CharField(max_length=100, null=False)
  active = models.BooleanField(null=False, default=False)
  updated_at = models.DateTimeField(null=False, auto_now_add=True)
  created_at = models.DateTimeField(null=False, auto_now=True)
  objects = BaseManager()

  def __str__(self):
    return self.key


@receiver(post_save, sender=Redirect)
def save_redirect(sender, instance, **kwargs):
  # Verifico que el nuvo redirect tenga el paramentro active en True
  if instance.active:
    # Guardo o actualizo el registro en cache
    cache.set(instance.key, {"key": instance.key, "url": instance.url}, 3600)
  # Borro el registro de la cache si se desactiva el registro
  elif cache.get(instance.key):
    cache.delete(instance.key)


@receiver(post_delete, sender=Redirect)
def delete_redirect(sender, instance, **kwargs):
  # Borro el registro de la cache
  cache.delete(instance.key)

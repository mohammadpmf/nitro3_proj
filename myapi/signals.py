from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Staff

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_staff_profile_for_created_staff(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(user=instance)
        